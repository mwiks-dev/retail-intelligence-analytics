import pandas as pd


def standardize_column_names(df):
    """Standardise column names."""
    cleaned = df.copy()

    cleaned.columns = (
        cleaned.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    return cleaned


def parse_date_columns(df):
    """Parse columns explicitly named as dates."""
    cleaned = df.copy()

    for column in cleaned.columns:
        if column == "date" or column.endswith("_date"):
            cleaned[column] = pd.to_datetime(
                cleaned[column],
                errors="coerce"
            )

    return cleaned


def clean_dataset(df):
    """Apply the initial cleaning operations."""
    cleaned = standardize_column_names(df)
    cleaned = parse_date_columns(cleaned)

    return cleaned