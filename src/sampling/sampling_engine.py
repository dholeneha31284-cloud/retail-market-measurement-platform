from pathlib import Path

import pandas as pd

# ---------------------------------
# Configuration
# ---------------------------------
INPUT_FILE = Path("data/raw/retail_universe.csv")
OUTPUT_DIR = Path("data/sampled")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "sampled_stores.csv"

SAMPLE_FRACTION = 0.10

# ---------------------------------
# Read Retail Universe
# ---------------------------------
stores = pd.read_csv(INPUT_FILE)

print("\nRetail Universe Columns:")
print(stores.columns.tolist())

# ---------------------------------
# Stratified Sampling by Channel
# ---------------------------------
sampled_df = (
    stores
    .groupby("Channel")
    .sample(frac=SAMPLE_FRACTION, random_state=42)
    .reset_index(drop=True)
)

print("\nSampled Dataset Columns:")
print(sampled_df.columns.tolist())

# ---------------------------------
# Save Sample
# ---------------------------------
sampled_df.to_csv(OUTPUT_FILE, index=False)

# ---------------------------------
# Summary
# ---------------------------------
print("\nSampling Completed Successfully")
print(f"Original Stores : {len(stores)}")
print(f"Sampled Stores  : {len(sampled_df)}")
print(f"Output File     : {OUTPUT_FILE}")