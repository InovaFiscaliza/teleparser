from datetime import datetime, timezone
from pathlib import Path
import pytest
from teleparser.file_handling import CDRFileSetup, CDRFileManager


@pytest.fixture
def file_setup():
    return CDRFileSetup(
        input_path=Path(Path(__file__).parent / "data/input"),
        output_path=Path(Path(__file__).parent / "data/output"),
        carrier="carrier",
        cdr_type="cdr_type",
        timestamp=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"),
    )


@pytest.fixture
def file_manager(file_setup):
    return CDRFileManager(file_setup)


def test_file_manager_initialization(file_manager):
    assert file_manager.processed_files == set()
    assert file_manager.failed_files == set()


def test_setup_directories(file_manager):
    output_dir = file_manager.setup_directories()
    expected_path = (
        Path(__file__).parent / f"data/output/carrier_{file_manager.setup.timestamp}"
    )
    assert output_dir == expected_path
    assert output_dir.exists()


def test_get_input_gz_files(file_manager, tmp_path):
    # Create test files
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    test_gz = input_dir / "test.gz"
    test_gz.touch()

    file_manager.setup.input_path = input_dir
    gz_files = file_manager.input_gz_files

    assert len(gz_files) == 1
    assert gz_files[0] == test_gz


def test_cleanup(file_manager):
    temp_dir = file_manager.setup.output_path / "temp_extracted"
    temp_dir.mkdir(parents=True, exist_ok=True)
    file_manager.cleanup()
    assert not temp_dir.exists()
