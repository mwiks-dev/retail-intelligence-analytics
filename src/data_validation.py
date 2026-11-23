def check_unique_key(df, column):
    """Check that a key has no missing or duplicate values."""
    return (
        column in df.columns
        and df[column].notna().all()
        and df[column].is_unique
    )

def count_missing_values(df):
    """Count missing cells."""
    return int(df.isna().sum().sum())

def count_duplicate_rows(df):
    """Count exact duplicate rows."""
    return int(df.duplicated().sum())

def check_non_negative(df, column):
    """Check that a numeric column has no negative or null values."""
    if column not in df.columns:
        return False

    return (
        df[column].notna().all()
        and (df[column] >= 0).all()
    )