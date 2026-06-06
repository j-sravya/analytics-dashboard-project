-- E-Commerce Sales Analytics SQL Queries
-- Table name assumed: ecommerce_sales

-- 1. Total revenue
SELECT
    ROUND(SUM(total_sales), 2) AS total_revenue
FROM ecommerce_sales;

-- 2. Monthly sales trend
SELECT
    STRFTIME('%Y-%m', order_date) AS sales_month,
    ROUND(SUM(total_sales), 2) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM ecommerce_sales
GROUP BY STRFTIME('%Y-%m', order_date)
ORDER BY sales_month;

-- 3. Top products
SELECT
    product_name,
    product_category,
    ROUND(SUM(total_sales), 2) AS revenue,
    SUM(quantity) AS units_sold
FROM ecommerce_sales
GROUP BY product_name, product_category
ORDER BY revenue DESC
LIMIT 10;

-- 4. Revenue by category
SELECT
    product_category,
    ROUND(SUM(total_sales), 2) AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM ecommerce_sales
GROUP BY product_category
ORDER BY revenue DESC;

-- 5. Customer segment analysis
SELECT
    customer_segment,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(total_sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM ecommerce_sales
GROUP BY customer_segment
ORDER BY revenue DESC;

-- 6. Top cities
SELECT
    city,
    state,
    ROUND(SUM(total_sales), 2) AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM ecommerce_sales
GROUP BY city, state
ORDER BY revenue DESC
LIMIT 10;

-- 7. Profit analysis
SELECT
    product_category,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(total_sales), 2) AS profit_margin_percent
FROM ecommerce_sales
GROUP BY product_category
ORDER BY total_profit DESC;

-- 8. Average order value
SELECT
    ROUND(SUM(total_sales) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM ecommerce_sales;

-- 9. Payment method distribution
SELECT
    payment_method,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(total_sales), 2) AS revenue
FROM ecommerce_sales
GROUP BY payment_method
ORDER BY orders DESC;

-- 10. Shipping analysis
SELECT
    shipping_type,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(AVG(delivery_days), 2) AS average_delivery_days,
    ROUND(SUM(total_sales), 2) AS revenue
FROM ecommerce_sales
GROUP BY shipping_type
ORDER BY orders DESC;
