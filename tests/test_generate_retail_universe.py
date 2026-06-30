import pandas as pd


def test_retail_universe():
    df = pd.read_csv("data/raw/retail_universe.csv")

    # Dataset should not be empty
    assert len(df) > 0

    # Store_ID should be unique
    assert df["Store_ID"].is_unique

    # Required columns should not contain nulls
    assert df["Store_ID"].notna().all()
    assert df["Channel"].notna().all()
    assert df["State"].notna().all()
    assert df["City"].notna().all()