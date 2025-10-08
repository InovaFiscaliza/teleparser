# Requirements: pip install duckdb
from __future__ import annotations
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union
import duckdb
import re

# -------------------------- small helpers --------------------------

def _escape_enum_val(v: str) -> str:
    return v.replace("'", "''")

def _safe_ident(name: str) -> str:
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        return name
    return f'"{name}"'

def _as_duck_list_literal(paths: Sequence[Path]) -> str:
    # DuckDB accepts list-literal of strings: ['a', 'b']
    items = ", ".join(f"'{p.as_posix().replace(\"'\", \"''\")}'" for p in paths)
    return f"[{items}]"

def _expand_inputs(
    inputs: Union[str, Path, Iterable[Union[str, Path]]],
    pattern: str = "*.parquet",
    recursive: bool = True,
) -> List[Path]:
    """
    Accepts:
      - a single file
      - a single directory (expanded with pattern)
      - a glob string ('/data/**/*.parquet')
      - an iterable of any of the above
    Returns a de-duplicated, sorted list of Path objects that exist.
    """
    def expand_one(x: Union[str, Path]) -> Iterable[Path]:
        p = Path(x)
        if "*" in str(p):
            yield from (Path(s) for s in p.parent.glob(p.name)) if not recursive else p.parent.rglob(p.name)
        elif p.is_dir():
            yield from (p.rglob(pattern) if recursive else p.glob(pattern))
        else:
            yield p

    seen = set()
    out: List[Path] = []
    if isinstance(inputs, (str, Path)):
        inputs = [inputs]

    for obj in inputs:
        for p in expand_one(obj):
            if p.exists() and p.suffix.lower() == ".parquet":
                if p not in seen:
                    seen.add(p)
                    out.append(p)

    return sorted(out)

# --------------------- core detection/import logic ---------------------

def detect_enum_candidates_multi(
    con: duckdb.DuckDBPyConnection,
    files: Sequence[Path],
    include_types: Tuple[str, ...] = ("VARCHAR",),
    max_levels: int = 500,
    max_ratio: float = 0.5,
    min_rows_for_ratio: int = 1000,
    explicit_whitelist: Optional[List[str]] = None,
    explicit_blacklist: Optional[List[str]] = None,
    union_by_name: bool = True,
) -> Dict[str, List[str]]:
    """
    Inspect the UNION of all files, return {col: sorted_distinct_values}
    for columns that qualify as categorical → ENUM.
    """
    explicit_whitelist = set(explicit_whitelist or [])
    explicit_blacklist = set(explicit_blacklist or [])

    if not files:
        return {}

    duck_list = _as_duck_list_literal(files)

    # Describe schema once (after name-union alignment if requested)
    schema_sql = (
        f"DESCRIBE SELECT * FROM read_parquet({duck_list}, union_by_name={str(union_by_name).lower()})"
    )
    schema = con.execute(schema_sql).fetchall()
    cols = [(r[0], r[1]) for r in schema]

    # Count total rows across all files
    total_rows = con.execute(
        f"SELECT COUNT(*) FROM read_parquet({duck_list}, union_by_name={str(union_by_name).lower()})"
    ).fetchone()[0]
    if total_rows == 0:
        return {}

    enum_map: Dict[str, List[str]] = {}

    for col, typ in cols:
        if col in explicit_blacklist:
            continue

        consider = (typ in include_types) or (col in explicit_whitelist)
        if not consider:
            continue

        k = con.execute(
            f"SELECT COUNT(DISTINCT {_safe_ident(col)}) "
            f"FROM read_parquet({duck_list}, union_by_name={str(union_by_name).lower()})"
        ).fetchone()[0]

        is_whitelisted = col in explicit_whitelist
        ratio_ok = (k / total_rows) <= max_ratio if total_rows >= min_rows_for_ratio else True
        levels_ok = k <= max_levels

        if is_whitelisted or (levels_ok and ratio_ok):
            vals = con.execute(
                f"SELECT DISTINCT {_safe_ident(col)} "
                f"FROM read_parquet({duck_list}, union_by_name={str(union_by_name).lower()}) "
                f"WHERE {_safe_ident(col)} IS NOT NULL "
                f"ORDER BY {_safe_ident(col)}"
            ).fetchall()
            enum_vals = [str(v[0]) for v in vals]
            if enum_vals:
                enum_map[col] = enum_vals

    return enum_map

def import_parquet_multi_as_enums(
    inputs: Union[str, Path, Iterable[Union[str, Path]]],
    table_name: str,
    *,
    duckdb_path: Optional[Union[str, Path]] = None,
    pattern: str = "*.parquet",
    recursive: bool = True,
    include_types: Tuple[str, ...] = ("VARCHAR",),
    max_levels: int = 500,
    max_ratio: float = 0.5,
    min_rows_for_ratio: int = 1000,
    explicit_whitelist: Optional[List[str]] = None,
    explicit_blacklist: Optional[List[str]] = None,
    replace: bool = True,
    union_by_name: bool = True,
) -> Tuple[duckdb.DuckDBPyConnection, Dict[str, List[str]], List[Path]]:
    """
    Expand inputs to a list of parquet files, infer enum candidates from the UNION,
    create stable ENUM types, and materialize the table with casts applied.
    Returns (connection, enum_map, file_list).
    """
    files = _expand_inputs(inputs, pattern=pattern, recursive=recursive)
    if not files:
        raise FileNotFoundError("No .parquet files found from the provided inputs.")

    con = duckdb.connect(str(duckdb_path)) if duckdb_path else duckdb.connect()

    enum_map = detect_enum_candidates_multi(
        con=con,
        files=files,
        include_types=include_types,
        max_levels=max_levels,
        max_ratio=max_ratio,
        min_rows_for_ratio=min_rows_for_ratio,
        explicit_whitelist=explicit_whitelist,
        explicit_blacklist=explicit_blacklist,
        union_by_name=union_by_name,
    )

    duck_list = _as_duck_list_literal(files)

    if replace:
        con.execute(f"DROP TABLE IF EXISTS {_safe_ident(table_name)}")

    # (Re)create per-column enum types with namespaced identifiers
    for col, levels in enum_map.items():
        type_name = _safe_ident(f"{table_name}_{col}_enum")
        try:
            con.execute(f"DROP TYPE IF EXISTS {type_name}")
        except Exception:
            pass
        levels_sql = ", ".join(f"'{_escape_enum_val(v)}'" for v in levels)
        con.execute(f"CREATE TYPE {type_name} AS ENUM ({levels_sql})")

    # Build SELECT list with casts
    schema = con.execute(
        f"DESCRIBE SELECT * FROM read_parquet({duck_list}, union_by_name={str(union_by_name).lower()})"
    ).fetchall()
    colnames = [r[0] for r in schema]

    select_exprs = []
    for col in colnames:
        if col in enum_map:
            type_name = _safe_ident(f"{table_name}_{col}_enum")
            select_exprs.append(f"CAST({_safe_ident(col)} AS {type_name}) AS {_safe_ident(col)}")
        else:
            select_exprs.append(_safe_ident(col))

    select_sql = ",\n       ".join(select_exprs)
    con.execute(
        f"CREATE TABLE {_safe_ident(table_name)} AS\n"
        f"SELECT {select_sql}\n"
        f"FROM read_parquet({duck_list}, union_by_name={str(union_by_name).lower()})"
    )

    return con, enum_map, files

# ----------------------------- example -----------------------------

if __name__ == "__main__":
    # Examples of accepted inputs:
    #   inputs = "/data/parquet_dir"                 # directory (recursively reads *.parquet)
    #   inputs = "/data/**/*.parquet"                # glob pattern
    #   inputs = ["a.parquet", "b.parquet"]          # explicit files
    #   inputs = [Path("/data/2025"), Path("/data/2024/*.parquet")]
    inputs = "/data/**/*.parquet"
    table = "events_fact"
    db = Path("warehouse/my.duckdb")

    con, enum_map, files = import_parquet_multi_as_enums(
        inputs=inputs,
        table_name=table,
        duckdb_path=db,
        pattern="*.parquet",
        recursive=True,
        # tuning:
        max_levels=200,
        max_ratio=0.25,
        min_rows_for_ratio=5000,
        explicit_whitelist=["city", "state"],   # force-enum
        explicit_blacklist=["description"],     # never-enum
        replace=True,
        union_by_name=True,                     # align cols by name across files
    )

    print(f"Ingested {len(files)} files into table {table!r} at {db}")
    print("ENUM columns inferred:")
    for c, vals in enum_map.items():
        print(f"  - {c} ({len(vals)} levels)")
    print(con.execute(f"DESCRIBE {_safe_ident(table)}").df())
