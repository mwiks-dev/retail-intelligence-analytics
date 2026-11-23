from src.config import PROCESSED_DIR
from src.data_ingestion import load_all_datasets
from src.data_cleaning import clean_dataset


def main():
    datasets = load_all_datasets()

    for name, df in datasets.items():
        cleaned = clean_dataset(df)

        output_file = PROCESSED_DIR / f"{name}.csv"

        cleaned.to_csv(output_file, index=False)

        print(
            f"{name}: {len(df)} rows -> "
            f"{len(cleaned)} rows"
        )


if __name__ == "__main__":
    main()