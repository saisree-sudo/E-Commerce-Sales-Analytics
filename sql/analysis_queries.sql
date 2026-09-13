USE ecommerce_analytics;

-- 1. Total sales
SELECT SUM(Sales) AS Total_Sales FROM orders;

-- 2. Total profit
SELECT SUM(Profit) AS Total_Profit FROM orders;

-- 3. Sales by category
SELECT Category, SUM(Sales) AS Sales
FROM orders
GROUP BY Category
ORDER BY Sales DESC;

-- 4. Profit by region
SELECT Region, SUM(Profit) AS Profit
FROM orders
GROUP BY Region
ORDER BY Profit DESC;

-- 5. Top products
SELECT Product, SUM(Sales) AS Sales
FROM orders
GROUP BY Product
ORDER BY Sales DESC
LIMIT 10;

-- 6. High-sales low-profit products
SELECT Product, SUM(Sales) AS Sales, SUM(Profit) AS Profit
FROM orders
GROUP BY Product
ORDER BY Sales DESC;

-- 7. Payment mode usage
SELECT Payment_Mode, COUNT(*) AS Orders
FROM orders
GROUP BY Payment_Mode
ORDER BY Orders DESC;
