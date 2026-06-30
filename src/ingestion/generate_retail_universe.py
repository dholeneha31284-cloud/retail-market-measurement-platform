import random
from pathlib import Path

import pandas as pd
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_STORES = 10000

CHANNELS = [
    "Kirana",
    "Supermarket",
    "Hypermarket",
    "Pharmacy",
    "Convenience Store"
]

OWNER_TYPES = [
    "Independent",
    "Chain"
]

STORE_STATUS = [
    "Active",
    "Closed"
]

LOCATIONS = [
    ("Maharashtra", "Mumbai", "Mumbai"),
    ("Maharashtra", "Pune", "Pune"),
    ("Karnataka", "Bengaluru", "Bengaluru Urban"),
    ("Tamil Nadu", "Chennai", "Chennai"),
    ("Telangana", "Hyderabad", "Hyderabad"),
    ("Delhi", "New Delhi", "New Delhi"),
    ("Gujarat", "Ahmedabad", "Ahmedabad"),
    ("West Bengal", "Kolkata", "Kolkata")
]

rows = []

for i in range(1, NUM_STORES + 1):

    state, city, district = random.choice(LOCATIONS)

    rows.append({
        "Store_ID": f"S{i:06d}",
        "Store_Name": fake.company(),
        "Channel": random.choice(CHANNELS),
        "State": state,
        "City": city,
        "District": district,
        "Pincode": fake.postcode(),
        "Latitude": round(random.uniform(8.0, 37.0), 6),
        "Longitude": round(random.uniform(68.0, 97.0), 6),
        "Opening_Date": fake.date_between("-20y", "today"),
        "Store_Status": random.choice(STORE_STATUS),
        "Owner_Type": random.choice(OWNER_TYPES)
    })

df = pd.DataFrame(rows)

output_file = OUTPUT_DIR / "retail_universe.csv"

df.to_csv(output_file, index=False)

print(f"Dataset created successfully.")
print(f"Rows: {len(df)}")
print(f"Saved to: {output_file}")