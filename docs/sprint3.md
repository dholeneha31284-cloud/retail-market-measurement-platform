# Sprint 3 – Data Quality Framework

## Business Problem

Retail sales data is collected from multiple stores. Before this data can be used for sampling, market estimation, or reporting, its quality must be verified.

Poor-quality data can lead to incorrect business decisions and inaccurate market estimates.

This sprint focuses on validating the POS sales data generated in Sprint 2.

---

# Why is this Module Needed?

Real-world datasets often contain problems such as:

* Duplicate transactions
* Missing store information
* Missing product details
* Invalid quantities
* Invalid sales values

These issues must be identified before performing any statistical analysis.

---

# Objective

Validate the POS sales dataset and create a clean dataset that can be used in the next stages of the project.

---

# Input

```
data/raw/pos_sales.csv
```

---

# Output

Validated Dataset

```
data/validated/pos_sales_valid.csv
```

Validation Report

```
data/validated/validation_report.csv
```

---

# Validation Rules

The following checks are performed:

| Validation               | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| Duplicate Transaction_ID | Ensure every transaction is unique       |
| Missing Store_ID         | Every transaction must belong to a store |
| Missing Category         | Product category is required             |
| Missing Brand            | Brand information is required            |
| Units_Sold > 0           | Quantity cannot be zero or negative      |
| Sales_Value > 0          | Sales value cannot be zero or negative   |

---

# Implementation

### Python

**File**

```
src/validation/validate_pos_sales.py
```

Responsibilities:

* Read POS sales data.
* Perform validation checks.
* Remove invalid records.
* Generate a validation report.
* Save the validated dataset.

---

### SQL

**File**

```
sql/validation_queries.sql
```

Contains SQL queries to identify duplicate, missing, and invalid records when the data is stored in a relational database.

---

### Unit Testing

**File**

```
tests/test_validate_pos_sales.py
```

The tests verify:

* Validated dataset exists.
* Validation report exists.
* Transaction IDs are unique.
* Store IDs are present.
* Units sold are positive.
* Sales values are positive.

---

# Expected Output

After running the validation process:

* Clean POS dataset
* Validation report
* Successful unit test execution

---

# Key Learning

Data validation is an essential step before sampling, statistical estimation, and reporting.

High-quality input data leads to more reliable business insights.

---

# What's Next?

In **Sprint 4**, we will build the **Sampling Engine**.

Instead of analysing every retail store, we will select a representative sample of stores for market measurement.
