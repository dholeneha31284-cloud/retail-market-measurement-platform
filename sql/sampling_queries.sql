-- Total Stores
SELECT COUNT(*) AS Total_Stores
FROM retail_store_master;

-- Stores by Channel
SELECT
    Channel,
    COUNT(*) AS Store_Count
FROM retail_store_master
GROUP BY Channel;

-- Sampled Stores
SELECT
    Channel,
    COUNT(*) AS Sample_Count
FROM sampled_stores
GROUP BY Channel;