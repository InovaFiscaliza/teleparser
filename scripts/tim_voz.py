import subprocess
from fastcore.xtras import Path

root_source = Path("/data/cdr/cdr_bruto")
root_destination = Path("/data/cdr/cdr_traduzido")

START = 14
STOP = 59

source = []
destination = []
for i in range(START, STOP):
    folder = root_source / f"Semana{i}/Tim/"
    if files := list(folder.glob("**/GSM/*.gz")):
        source.append(files[0].parent)
        destination.append(root_destination / f"Semana{i}/tim/ericsson")

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
