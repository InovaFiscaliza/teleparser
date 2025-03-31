import logging
import traceback
from contextlib import suppress
from pathlib import Path
import os
from teleparser.main import main, setup_logging, DECODERS
import typer


def process_cdrs():
    app = typer.Typer()

    @app.command()
    def cli(
        entrada: str = typer.Argument(
            ..., help="Caminho para um arquivo CDR único ou diretório"
        ),
        saída: str = typer.Argument(..., help="Caminho para o diretório de saída"),
        tipo_cdr: str = typer.Option(
            "ericsson_voz",
            "--tipo",
            "-t",
            help=f"Tipo de CDR para processar. Opções: {', '.join(DECODERS.keys())}",
        ),
        workers: int = typer.Option(
            os.cpu_count(),
            "--nucleos",
            "-n",
            help="Número de núcleos para processamento paralelo, máximo é o número de núcleos da CPU",
        ),
        log_level: str = typer.Option(
            "INFO",
            "--log",
            help="Nível de log. Opções: DEBUG, INFO, WARNING, ERROR, CRITICAL",
        ),
    ):
        """Processa arquivos CDR do caminho de entrada (arquivo/pasta) e salva resultados no caminho de saída em formato .csv.gzip.\n
        O formato esperado é um arquivo ou pasta com um ou mais arquivos gzip.\n
        Se os arquivos gzip estiverem em um arquivo ZIP, eles serão extraídos primeiro.
        O modo padrão é processamento paralelo utilizando múltiplos núcleos da CPU.
        """
        # Create output directory if it doesn't exist
        output_dir = Path(saída)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Set log level based on command line argument
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            print(f"[bold red]Nível de log inválido: {log_level}[/bold red]")
            numeric_level = logging.INFO

        try:
            main(Path(entrada), output_dir, tipo_cdr, workers, numeric_level)
        except Exception as e:
            # At this point, logger might not be initialized yet, so we print to console
            error_details = traceback.format_exc()
            print(f"[bold red]Fatal Error: {str(e)}[/bold red]")

            # Try to log to file if possible
            with suppress(Exception):
                temp_logger = setup_logging(output_dir, logging.ERROR)
                temp_logger.critical(
                    f"Exception untreated in main process: {str(e)}\n{error_details}"
                )
            raise

    app()


if __name__ == "__main__":
    import multiprocessing

    multiprocessing.freeze_support()
    process_cdrs()
