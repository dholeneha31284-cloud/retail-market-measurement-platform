-- Total Records
SELECT COUNT(*) AS Total_Records
FROM pos_sales;

-- Duplicate Transaction IDs
SELECT
    Transaction_ID,
    COUNT(*) AS Duplicate_Count
FROM pos_sales
GROUP BY Transaction_ID
HAVING COUNT(*) > 1;

-- Missing Store ID
SELECT *
FROM pos_sales
WHERE Store_ID IS NULL;

-- Missing Category
SELECT *
FROM pos_sales
WHERE Category IS NULL;

-- Missing Brand
SELECT *
FROM pos_sales
WHERE Brand IS NULL;

-- Invalid Units Sold
SELECT *
FROM pos_sales
WHERE Units_Sold <= 0;

-- Invalid Sales Value
SELECT *
FROM pos_sales
WHERE Sales_Value <= 0;