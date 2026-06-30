CREATE TABLE retail_store_master (
    Store_ID VARCHAR(20) PRIMARY KEY,
    Store_Name VARCHAR(255) NOT NULL,
    Channel VARCHAR(50) NOT NULL,
    State VARCHAR(100) NOT NULL,
    City VARCHAR(100) NOT NULL,
    District VARCHAR(100),
    Pincode VARCHAR(10),
    Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6),
    Opening_Date DATE,
    Store_Status VARCHAR(20),
    Owner_Type VARCHAR(20)
);