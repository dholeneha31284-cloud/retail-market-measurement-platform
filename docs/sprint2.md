# Sprint 2 – POS Sales Simulation

## Business Problem

After identifying the Retail Universe (Sprint 1), the next step is to collect sales data from retail stores.

Retail stores record every product sold at the billing counter. This information is known as **Point of Sale (POS) data**.

POS data forms the basis for market measurement, sales analysis, sampling, and market estimation.

---

# Why is this Module Needed?

Knowing which stores exist is not enough.

To understand market performance, we also need to know:

* What products were sold?
* How many units were sold?
* What was the sales value?
* Which brands are performing well?

This information is captured through POS transactions.

---

# Objective

Generate a synthetic POS sales dataset for the stores created in Sprint 1.

Each transaction represents a product sale made by a retail store.

---

# Input

Retail Universe dataset:

```
data/raw/retail_universe.csv
```

---

# Output

```
data/raw/pos_sales.csv
```

Dataset fields:

| Column           | Description                   |
| ---------------- | ----------------------------- |
| Transaction_ID   | Unique transaction identifier |
| Store_ID         | Store identifier              |
| Transaction_Date | Date of transaction           |
| Category         | Product category              |
| Brand            | Product brand                 |
| Units_Sold       | Quantity sold                 |
| Sales_Value      | Total sales amount            |
| Promotion_Flag   | Promotion indicator           |

---

# Implementation

### Python

**File**

```
src/ingestion/generate_pos_sales.py
```

Responsibilities:

* Read the Retail Universe.
* Generate synthetic POS transactions.
* Assign product categories and brands.
* Calculate sales value.
* Export the dataset to CSV.

---

### SQL

**File**

```
sql/create_pos_sales.sql
```

Defines the database table for storing POS sales transactions.

---

### Unit Testing

**File**

```
tests/test_generate_pos_sales.py
```

Validation performed:

* Transaction_ID is unique.
* Store_ID is not null.
* Category is not null.
* Brand is not null.
* Units_Sold is greater than zero.
* Sales_Value is greater than zero.
* Promotion_Flag contains only "Yes" or "No".

---

# Expected Output

* POS sales dataset.
* SQL table definition.
* Successful unit tests.
* Documentation.

---

# Key Learning

POS data is the primary source used to understand retail sales performance.

In the next sprint, this dataset will be validated to ensure it is complete, consistent, and suitable for statistical analysis.

---

# What's Next?

Sprint 3 focuses on **Data Quality**, where we will validate and clean the POS data before using it for sampling and market estimation.
