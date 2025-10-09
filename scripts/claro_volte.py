import subprocess
from fastcore.xtras import Path

root_source = Path("/data/cdr/cdr_bruto")
root_destination = Path("/data/cdr/cdr_traduzido")

START = 42
STOP = 59
source = [
    (root_source / f"Semana{i}/Claro").ls().filter(lambda x: "_4G_" in x.stem)[0]
    for i in range(START, STOP)
]
destination = [
    root_destination / f"Semana{i}/claro/ericsson" for i in range(START, STOP)
]


for s, d in zip(source, destination):
    subprocess.run(
        [
            "uv",
            "run",
            "src/teleparser/cli.py",
            s,
            "-s",
            d,
            "-n",
            "1",
            "--tipo",
            "ericsson_volte",
            "-R",
        ]
    )
