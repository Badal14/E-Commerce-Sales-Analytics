CREATE DATABASE ecommerce_analytics;
USE ecommerce_analytics;

show tables;

select * from superstore;

SELECT COUNT(*) AS total_records
FROM superstore;

desc superstore;
--------------------------------------------------------
-- Query 1 – Overall business performance
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT `Order ID`) AS Total_Orders,
    COUNT(DISTINCT `Customer ID`) AS Total_Customers,
    SUM(Quantity) AS Total_Quantity,
    ROUND(
        SUM(Profit) / SUM(Sales) * 100, 2
    ) AS Profit_Margin
FROM superstore;

--------------------------------------------------------
-- Query 2 – Category-wise sales and profit
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

--------------------------------------------------------
-- Query 3 – Regional performance
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

--------------------------------------------------------
-- Query 4 – Top 10 customers 
SELECT
    `Customer ID`,
    `Customer Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY `Customer ID`, `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

--------------------------------------------------------
-- Query 5 – Monthly sales analysis
SELECT
    YEAR(`Order Date`) AS Sales_Year,
    MONTH(`Order Date`) AS Sales_Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales
FROM superstore
GROUP BY
    YEAR(`Order Date`),
    MONTH(`Order Date`)
ORDER BY Sales_Year, Sales_Month; 

--------------------------------------------------------
-- Query 6 – Top 5 profitable sub-categories
SELECT
    `Sub-Category`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Total_Profit DESC
LIMIT 5;

--------------------------------------------------------
-- Query 7 – Ranking customers using Window Functions
SELECT
    `Customer ID`,
    `Customer Name`,
    Total_Sales,
    DENSE_RANK() OVER (
        ORDER BY Total_Sales DESC
    ) AS Sales_Rank
FROM (
    SELECT
        `Customer ID`,
        `Customer Name`,
        SUM(Sales) AS Total_Sales
    FROM superstore
    GROUP BY `Customer ID`, `Customer Name`
) AS customer_sales;

--------------------------------------------------------








