# Sprint 1 – Retail Universe Generation

## Business Problem

A retail market measurement company wants to understand the performance of the retail market. However, it is not possible to collect sales data from every retail store in the country because there are millions of stores.

Before selecting stores for data collection or estimating market sales, the company must first know **which retail stores exist**. This complete list of stores is called the **Retail Universe** or **Store Master**.

This sprint focuses on creating that Retail Universe.

---

# Why is this Module Needed?

The Retail Universe is the foundation for all subsequent analysis.

Without a Store Master, the company cannot:

* Select a representative sample of stores.
* Estimate the total number of retail stores.
* Extrapolate sample sales to the total market.
* Analyze sales by region or retail channel.

In simple terms:

**No Retail Universe → No Sampling → No Market Estimation.**

---

# Objective

Create a synthetic Retail Universe dataset representing retail stores across different Indian states, cities, and retail channels.

The dataset should contain the basic information required for future statistical analysis.

---

# Input

No external dataset is used.

The Retail Universe is generated synthetically using Python and the Faker library.

---

# Output

Dataset:

```
data/raw/retail_universe.csv
```

The dataset contains the following fields:

| Column       | Description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| Store_ID     | Unique store identifier                                                        |
| Store_Name   | Retail store name                                                              |
| Channel      | Retail channel (Kirana, Supermarket, Hypermarket, Pharmacy, Convenience Store) |
| State        | State                                                                          |
| City         | City                                                                           |
| District     | District                                                                       |
| Pincode      | Postal code                                                                    |
| Latitude     | Latitude                                                                       |
| Longitude    | Longitude                                                                      |
| Opening_Date | Store opening date                                                             |
| Store_Status | Active or Closed                                                               |
| Owner_Type   | Independent or Chain                                                           |

---

# Implementation

This sprint includes the following components:

### Python

**File**

```
src/ingestion/generate_retail_universe.py
```

Responsibilities:

* Generate synthetic retail stores.
* Assign geographical information.
* Assign retail channels.
* Generate unique Store IDs.
* Save the dataset as a CSV file.

---

### SQL

**File**

```
sql/create_store_master.sql
```

Purpose:

Defines the Store Master table that can be created in a relational database before loading the Retail Universe data.

---

### Unit Testing

**File**

```
tests/test_generate_retail_universe.py
```

Validation performed:

* Store_ID is unique.
* Store_ID is not null.
* State is not null.
* City is not null.
* Channel is not null.

These checks ensure that the generated dataset is suitable for downstream processing.

---

# Project Structure

```
retail-market-measurement-platform/

├── data/
│   └── raw/
│       └── retail_universe.csv
│
├── src/
│   └── ingestion/
│       └── generate_retail_universe.py
│
├── sql/
│   └── create_store_master.sql
│
├── tests/
│   └── test_generate_retail_universe.py
│
└── docs/
    └── sprint1.md
```

---

# How to Run

Generate the Retail Universe:

```bash
python src/ingestion/generate_retail_universe.py
```

Run the unit tests:

```bash
pytest
```

---

# Expected Output

* A Retail Universe dataset with synthetic retail stores.
* SQL table definition for the Store Master.
* Successful unit test execution.
* Documentation describing the implementation.

---

# Key Learning

In retail market measurement, the first step is **not statistical analysis**.

The first step is identifying the complete population of retail stores.

This Store Master serves as the foundation for all subsequent processes, including:

* Sampling
* Universe Estimation
* Extrapolation
* Market Analysis

---

# What's Next?

In **Sprint 2**, we will generate **Point-of-Sale (POS) Sales Data** for the stores created in this sprint.

The combination of the Retail Universe and POS Sales data will form the basis for sampling and market estimation in the upcoming sprints.
