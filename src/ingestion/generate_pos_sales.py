import random
from pathlib import Path

import pandas as pd

# -----------------------------
# Configuration
# -----------------------------
random.seed(42)

INPUT_FILE = Path("data/raw/retail_universe.csv")
OUTPUT_FILE = Path("data/raw/pos_sales.csv")

# Product Categories and Brands
PRODUCTS = {
    "Beverages": ["Coca-Cola", "Pepsi", "Sprite"],
    "Biscuits": ["Parle-G", "Good Day", "Oreo"],
    "Shampoo": ["Clinic Plus", "Sunsilk", "Dove"],
    "Soap": ["Lux", "Lifebuoy", "Dove"],
    "Toothpaste": ["Colgate", "Closeup", "Pepsodent"]
}

# -----------------------------
# Read Store Master
# -----------------------------
stores = pd.read_csv(INPUT_FILE)

sales_data = []
transaction_no = 1

# Generate 10 transactions per store
for _, store in stores.iterrows():

    for _ in range(10):

        category = random.choice(list(PRODUCTS.keys()))
        brand = random.choice(PRODUCTS[category])

        units = random.randint(1, 20)
        price = random.randint(20, 500)

        sales_data.append({

            "Transaction_ID": f"T{transaction_no:08d}",
            "Store_ID": store["Store_ID"],
            "Transaction_Date": "2026-06-30",
            "Category": category,
            "Brand": brand,
            "Units_Sold": units,
            "Sales_Value": units * price,
            "Promotion_Flag": random.choice(["Yes", "No"])

        })

        transaction_no += 1

# -----------------------------
# Save Dataset
# -----------------------------
sales_df = pd.DataFrame(sales_data)

sales_df.to_csv(OUTPUT_FILE, index=False)

print("POS Sales Dataset Created Successfully")
print(f"Rows : {len(sales_df)}")
print(f"Output : {OUTPUT_FILE}")