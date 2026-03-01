CREATE DATABASE priyanka_saas_intelligence;
USE priyanka_saas_intelligence;

CREATE TABLE saas_sales_raw (
    order_id VARCHAR(50),
    order_date DATE,
    date_key INT,
    contact_name VARCHAR(100),
    country VARCHAR(100),
    city VARCHAR(100),
    region VARCHAR(100),
    subregion VARCHAR(100),
    customer VARCHAR(150),
    customer_id VARCHAR(50),
    industry VARCHAR(100),
    segment VARCHAR(100),
    product VARCHAR(150),
    license VARCHAR(100),
    sales DECIMAL(12,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(12,2)
);

DROP TABLE IF EXISTS saas_sales_cleaned;

CREATE TABLE saas_sales_cleaned (
    row_id INT,
    order_id VARCHAR(50),
    order_date DATE,
    date_key INT,
    contact_name VARCHAR(100),
    country VARCHAR(100),
    city VARCHAR(100),
    region VARCHAR(100),
    subregion VARCHAR(100),
    customer VARCHAR(150),
    customer_id VARCHAR(50),
    industry VARCHAR(100),
    segment VARCHAR(100),
    product VARCHAR(150),
    license VARCHAR(100),
    sales DECIMAL(12,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(12,2),
    churn INT,
    churn_probability DECIMAL(6,4),
    revenue_risk DECIMAL(12,2),
    risk_category VARCHAR(50)
);

RENAME TABLE saas_sales_cleaned TO saas_sales_cleaned_old;
RENAME TABLE SaaS_Sales_With_Risk TO saas_sales_cleaned;

RENAME TABLE saas_sales_raw TO saas_sales_raw_old;
RENAME TABLE `saas-sales` TO saas_sales_raw;

SELECT COUNT(*) FROM saas_sales_cleaned;

-- Data Health Checking

SELECT 
    COUNT(*) AS total_rows,
    COUNT(DISTINCT `customer id`) AS unique_customers,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM saas_sales_cleaned;

SHOW COLUMNS FROM saas_sales_cleaned;

SELECT 
    churn,
    COUNT(*) AS customers
FROM saas_sales_cleaned
GROUP BY churn;

SELECT 
    `risk category`,
    COUNT(*) AS customers,
    SUM(revenue_risk) AS revenue_at_risk
FROM saas_sales_cleaned
GROUP BY `risk category`
ORDER BY revenue_at_risk DESC;

SHOW INDEX FROM saas_sales_cleaned;

SELECT 
    YEAR(`order date`) AS year,
    SUM(sales) AS revenue
FROM saas_sales_cleaned
GROUP BY year
ORDER BY revenue DESC
LIMIT 1;

ALTER TABLE saas_sales_cleaned
ADD COLUMN order_date_clean DATE;

SET SQL_SAFE_UPDATES = 0;

UPDATE saas_sales_cleaned
SET order_date_clean =
    CASE 
        WHEN `order date` LIKE '%/%' 
            THEN STR_TO_DATE(`order date`, '%m/%d/%Y')
        WHEN `order date` LIKE '%-%' 
            THEN STR_TO_DATE(`order date`, '%d-%m-%Y')
    END;
    
SET SQL_SAFE_UPDATES = 1;
DESCRIBE saas_sales_cleaned;

SELECT 
    YEAR(order_date_clean) AS year,
    SUM(sales) AS revenue
FROM saas_sales_cleaned
GROUP BY year
ORDER BY year;
