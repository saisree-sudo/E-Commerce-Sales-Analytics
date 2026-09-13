CREATE DATABASE ecommerce_analytics;
USE ecommerce_analytics;

CREATE TABLE orders (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    Product VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Sales DECIMAL(12,2),
    Discount DECIMAL(5,2),
    Cost DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Region VARCHAR(50),
    City VARCHAR(50),
    Payment_Mode VARCHAR(30)
);
