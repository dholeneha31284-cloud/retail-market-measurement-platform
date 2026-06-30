import pandas as pd


def test_pos_sales():

    df = pd.read_csv("data/raw/pos_sales.csv")

    # Dataset should not be empty
    assert len(df) > 0

    # Transaction ID should be unique
    assert df["Transaction_ID"].is_unique

    # Required columns
    assert df["Store_ID"].notna().all()
    assert df["Category"].notna().all()
    assert df["Brand"].notna().all()

    # Sales validation
    assert (df["Units_Sold"] > 0).all()
    assert (df["Sales_Value"] > 0).all()

    # Promotion values
    assert set(df["Promotion_Flag"]).issubset({"Yes", "No"})