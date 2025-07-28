import subprocess
from fastcore.xtras import Path

root_source = Path("/data/cdr/cdr_bruto")
root_destination = Path("/data/cdr/cdr_processado_novo")
source = [
    s
    for i in range(55, 13, -1)
    for s in (root_source / f"Semana{i}/Claro").ls().filter(lambda x: "_4G_" in x.stem)
]
destination = [root_destination / f"Semana{i}/claro/volte" for i in range(55, 13, -1)]


for s, d in zip(source, destination):
    subprocess.run(
        [
            "uv",
            "run",
            "src/teleparser/cli.py",
            "--tipo",
            "ericsson_volte",
            "--nucleos",
            "2",
            "--log",
            "INFO",
            s,
            d,
        ]
    )
