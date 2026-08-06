-- Total number of orders
SELECT COUNT(*) FROM orders;

-- Total number of unique customer
SELECT COUNT(DISTINCT customer_unique_id)
FROM customers;

-- Date range of orders in the dataset
SELECT MIN(order_purchase_timestamp) AS first_order_date,
       MAX(order_purchase_timestamp) AS last_order_date
FROM orders;

-- Order Status Distribution
SELECT order_status, COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders;

-- Total Products
SELECT COUNT(product_id) AS total_products
FROM products;

-- Total sellers
SELECT COUNT(seller_id) AS total_sellers
FROM sellers;

-- Count of payment type
SELECT payment_type, COUNT(payment_type) AS total_payments
FROM order_payments
GROUP BY payment_type;

-- Average payment value
SELECT AVG(payment_value)
FROM order_payments;

-- Minimum and Maximum payment values
SELECT MIN(payment_value),
       MAX(payment_value)
FROM order_payments;

-- Top 10 product categories
SELECT product_category_name, COUNT(*) AS total_number
FROM products
WHERE product_category_name IS NOT NULL
GROUP BY product_category_name
ORDER BY total_number DESC
LIMIT 10;

-- Top 10 cities with most customers
SELECT customer_state, COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC
LIMIT 10;

-- Total Sales Value
SELECT SUM(price) AS total_sales
FROM order_items;

-- Average Product Price
SELECT AVG(price) AS average_product_price
FROM order_items;

-- -- Total freight cost
SELECT SUM(freight_value) AS total_freight_value
FROM order_items;

-- Top 10 highest revenue generating sellers
SELECT
   seller_id, SUM(price) AS total_revenue
FROM order_items
GROUP BY seller_id
ORDER BY total_revenue DESC
LIMIT 10;

-- EDA Completed 