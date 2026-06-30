from pathlib import Path

import pandas as pd


def test_validated_dataset_exists():
    assert Path("data/validated/pos_sales_valid.csv").exists()


def test_validation_report_exists():
    assert Path("data/validated/validation_report.csv").exists()


def test_no_duplicate_transactions():
    df = pd.read_csv("data/validated/pos_sales_valid.csv")
    assert df["Transaction_ID"].is_unique


def test_no_missing_store_id():
    df = pd.read_csv("data/validated/pos_sales_valid.csv")
    assert df["Store_ID"].notna().all()


def test_positive_units_sold():
    df = pd.read_csv("data/validated/pos_sales_valid.csv")
    assert (df["Units_Sold"] > 0).all()


def test_positive_sales_value():
    df = pd.read_csv("data/validated/pos_sales_valid.csv")
    assert (df["Sales_Value"] > 0).all()