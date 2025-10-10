import subprocess
from fastcore.xtras import Path

root_source = Path("/data/cdr/cdr_bruto")
root_destination = Path("/data/cdr/cdr_traduzido")

START = 15
STOP = 59

source = []
destination = []
for i in range(START, STOP):
    source.extend(
        (root_source / f"Semana{i}/Claro").ls().filter(lambda x: "ERICSSON" in x.stem)
    )

    destination.append(root_destination / f"Semana{i}/claro/ericsson")

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
            "ericsson_voz_optimized",
            "-R",
        ]
    )
