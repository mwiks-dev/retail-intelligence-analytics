import pandas as pd

from src.data_validation import (
    check_unique_key,
    count_missing_values,
    count_duplicate_rows,
    check_non_negative
)


def test_unique_key_passes():
    df = pd.DataFrame({
        "product_id": [1, 2, 3]
    })

    assert check_unique_key(df, "product_id")


def test_duplicate_key_fails():
    df = pd.DataFrame({
        "product_id": [1, 1, 3]
    })

    assert not check_unique_key(df, "product_id")


def test_missing_values():
    df = pd.DataFrame({
        "value": [10, None, 30]
    })

    assert count_missing_values(df) == 1


def test_duplicate_rows():
    df = pd.DataFrame({
        "value": [10, 10, 30]
    })

    assert count_duplicate_rows(df) == 1


def test_negative_quantity_fails():
    df = pd.DataFrame({
        "quantity": [2, -1, 4]
    })

    assert not check_non_negative(df, "quantity")