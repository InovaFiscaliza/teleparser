import subprocess
from fastcore.xtras import Path

root_source = Path("/data/cdr/cdr_bruto")
root_destination = Path("/data/cdr/cdr_processado_novo")
source = [
    (root_source / f"Semana{i}/Claro").ls().filter(lambda x: "ERICSSON" in x.stem)[0]
    for i in range(55, 13, -1)
]
destination = [
    root_destination / f"Semana{i}/claro/ericsson" for i in range(55, 13, -1)
]


for s, d in zip(source, destination):
    subprocess.run(
        [
            "uv",
            "run",
            "src/teleparser/cli.py",
            "--tipo",
            "ericsson_voz",
            "--nucleos",
            "4",
            "--reprocessar",
            "--log",
            "INFO",
            s,
            d,
        ]
    )
