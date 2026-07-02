from pathlib import Path

import pandas as pd


def test_sample_exists():
    assert Path("data/sampled/sampled_stores.csv").exists()


def test_sample_not_empty():
    df = pd.read_csv("data/sampled/sampled_stores.csv")
    assert len(df) > 0


def test_store_id_unique():
    df = pd.read_csv("data/sampled/sampled_stores.csv")
    assert df["Store_ID"].is_unique


def test_channel_exists():
    df = pd.read_csv("data/sampled/sampled_stores.csv")
    assert df["Channel"].notna().all()