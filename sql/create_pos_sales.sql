CREATE TABLE pos_sales (
    Transaction_ID VARCHAR(20) PRIMARY KEY,
    Store_ID VARCHAR(20) NOT NULL,
    Transaction_Date DATE NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Brand VARCHAR(100) NOT NULL,
    Units_Sold INT NOT NULL,
    Sales_Value DECIMAL(12,2) NOT NULL,
    Promotion_Flag VARCHAR(3) NOT NULL
);