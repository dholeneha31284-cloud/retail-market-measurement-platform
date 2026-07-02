# Sprint 4 – Sampling Engine

## Business Problem

A retail market measurement company cannot collect data from every retail store.

Instead, it selects a representative sample of stores.

This process is called Sampling.

---

## Objective

Create a representative sample of stores from the Retail Universe.

---

## Input

data/raw/retail_universe.csv

---

## Output

data/sampled/sampled_stores.csv

---

## Sampling Method

Stratified Sampling

Grouping Variable:

- Retail Channel

Sampling Fraction:

- 10%

---

## Implementation

Python

- Read Retail Universe
- Group stores by Channel
- Randomly sample 10%
- Save sampled dataset

SQL

- Count stores
- Count sampled stores

Testing

- Output exists
- Sample not empty
- Unique Store IDs
- Channel available

---

## Key Learning

Sampling allows companies to estimate the entire market without visiting every retail store.

---

## Next Sprint

Universe Estimation