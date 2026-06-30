from pathlib import Path

import pandas as pd

# ---------------------------------
# File Paths
# ---------------------------------
INPUT_FILE = Path("data/raw/pos_sales.csv")
OUTPUT_DIR = Path("data/validated")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VALID_FILE = OUTPUT_DIR / "pos_sales_valid.csv"
REPORT_FILE = OUTPUT_DIR / "validation_report.csv"

# ---------------------------------
# Read POS Sales Data
# ---------------------------------
df = pd.read_csv(INPUT_FILE)

# ---------------------------------
# Validation Checks
# ---------------------------------
validation_report = {
    "Total_Records": len(df),
    "Duplicate_Transactions": df["Transaction_ID"].duplicated().sum(),
    "Missing_Store_ID": df["Store_ID"].isna().sum(),
    "Missing_Category": df["Category"].isna().sum(),
    "Missing_Brand": df["Brand"].isna().sum(),
    "Invalid_Units_Sold": (df["Units_Sold"] <= 0).sum(),
    "Invalid_Sales_Value": (df["Sales_Value"] <= 0).sum(),
}

# ---------------------------------
# Keep Only Valid Records
# ---------------------------------
valid_df = df.copy()

valid_df = valid_df.drop_duplicates(subset=["Transaction_ID"])

valid_df = valid_df.dropna(
    subset=[
        "Store_ID",
        "Category",
        "Brand",
    ]
)

valid_df = valid_df[
    (valid_df["Units_Sold"] > 0)
    & (valid_df["Sales_Value"] > 0)
]

# ---------------------------------
# Save Outputs
# ---------------------------------
valid_df.to_csv(VALID_FILE, index=False)

report_df = pd.DataFrame([validation_report])

report_df.to_csv(REPORT_FILE, index=False)

# ---------------------------------
# Summary
# ---------------------------------
print("Data Validation Completed")
print(f"Input Records      : {len(df)}")
print(f"Valid Records      : {len(valid_df)}")
print(f"Validation Report  : {REPORT_FILE}")
print(f"Validated Dataset  : {VALID_FILE}")