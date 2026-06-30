# Sprint 1 – Retail Universe Generation

## Objective

Create a synthetic retail store master dataset that represents the retail universe. This dataset will be used in subsequent modules for sampling, universe estimation, and extrapolation.

## Deliverables

- Retail universe dataset
- SQL table definition
- Unit tests
- Documentation

## Dataset Schema

| Column | Description |
|---------|-------------|
| Store_ID | Unique store identifier |
| Store_Name | Store name |
| Channel | Retail channel |
| State | State |
| City | City |
| District | District |
| Pincode | Postal code |
| Latitude | Latitude |
| Longitude | Longitude |
| Opening_Date | Store opening date |
| Store_Status | Store status |
| Owner_Type | Independent or Chain |

## Output

```
data/raw/retail_universe.csv
```

## Sprint Outcome

A synthetic retail universe containing store master information that serves as the foundation for later statistical modules.