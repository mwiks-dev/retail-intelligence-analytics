import pandas as pd

from src.config import RAW_DIR


def load_csv(filename):
    """Load a raw CSV file."""
    file_path = RAW_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    return pd.read_csv(file_path)


def load_all_datasets():
    """Load every CSV in the raw data directory."""
    datasets = {}

    for file in sorted(RAW_DIR.glob("*.csv")):
        datasets[file.stem] = pd.read_csv(file)

    return datasets