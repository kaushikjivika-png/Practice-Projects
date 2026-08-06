-- ============================================================
-- E-COMMERCE SALES ANALYSIS
-- DATA VALIDATION
-- Dataset: Olist Brazilian E-Commerce
-- Database: PostgreSQL
-- ============================================================


-- Customers: check null values
SELECT
    COUNT(*) - COUNT(customer_id) AS customer_id_nulls,
    COUNT(*) - COUNT(customer_unique_id) AS unique_id_nulls,
    COUNT(*) - COUNT(customer_zip_code_prefix) AS zip_code_nulls,
    COUNT(*) - COUNT(customer_city) AS city_nulls,
    COUNT(*) - COUNT(customer_state) AS state_nulls
FROM customers;


-- Check repeated customer unique IDs
SELECT customer_unique_id, COUNT(*)
FROM customers
GROUP BY customer_unique_id
HAVING COUNT(*) > 1;


-- Count repeated customer unique IDs
SELECT COUNT(*)
FROM (
    SELECT customer_unique_id
    FROM customers
    GROUP BY customer_unique_id
    HAVING COUNT(*) > 1
) AS duplicate_customers;


-- Orders: check null values
SELECT
    COUNT(*) - COUNT(order_id) AS order_id_nulls,
    COUNT(*) - COUNT(customer_id) AS customer_id_nulls,
    COUNT(*) - COUNT(order_status) AS status_nulls,
    COUNT(*) - COUNT(order_purchase_timestamp) AS purchase_date_nulls,
    COUNT(*) - COUNT(order_approved_at) AS approved_date_nulls,
    COUNT(*) - COUNT(order_delivered_carrier_date) AS carrier_date_nulls,
    COUNT(*) - COUNT(order_delivered_customer_date) AS customer_delivery_nulls,
    COUNT(*) - COUNT(order_estimated_delivery_date) AS estimated_delivery_nulls
FROM orders;


-- Check status of orders with missing delivery date
SELECT order_status, COUNT(*)
FROM orders
WHERE order_delivered_customer_date IS NULL
GROUP BY order_status
ORDER BY COUNT(*) DESC;


-- 8 delivered orders have missing customer delivery dates
SELECT *
FROM orders
WHERE order_delivered_customer_date IS NULL
AND order_status = 'delivered';


-- Products: check null values
SELECT
    COUNT(*) - COUNT(product_id) AS product_id_nulls,
    COUNT(*) - COUNT(product_category_name) AS category_nulls,
    COUNT(*) - COUNT(product_name_lenght) AS name_length_nulls,
    COUNT(*) - COUNT(product_description_lenght) AS description_length_nulls,
    COUNT(*) - COUNT(product_photos_qty) AS photos_nulls,
    COUNT(*) - COUNT(product_weight_g) AS weight_nulls,
    COUNT(*) - COUNT(product_length_cm) AS length_nulls,
    COUNT(*) - COUNT(product_height_cm) AS height_nulls,
    COUNT(*) - COUNT(product_width_cm) AS width_nulls
FROM products;


-- Check products with missing descriptive information
SELECT COUNT(*)
FROM products
WHERE product_category_name IS NULL
AND product_name_lenght IS NULL
AND product_description_lenght IS NULL
AND product_photos_qty IS NULL;


-- Sellers: check null values
SELECT
    COUNT(*) - COUNT(seller_id) AS seller_id_nulls,
    COUNT(*) - COUNT(seller_zip_code_prefix) AS zip_code_nulls,
    COUNT(*) - COUNT(seller_city) AS city_nulls,
    COUNT(*) - COUNT(seller_state) AS state_nulls
FROM sellers;


-- Order items: check null values
SELECT
    COUNT(*) - COUNT(order_id) AS order_id_nulls,
    COUNT(*) - COUNT(order_item_id) AS order_item_id_nulls,
    COUNT(*) - COUNT(product_id) AS product_id_nulls,
    COUNT(*) - COUNT(seller_id) AS seller_id_nulls,
    COUNT(*) - COUNT(shipping_limit_date) AS shipping_date_nulls,
    COUNT(*) - COUNT(price) AS price_nulls,
    COUNT(*) - COUNT(freight_value) AS freight_nulls
FROM order_items;


-- Payments: check null values
SELECT
    COUNT(*) - COUNT(order_id) AS order_id_nulls,
    COUNT(*) - COUNT(payment_sequential) AS sequential_nulls,
    COUNT(*) - COUNT(payment_type) AS payment_type_nulls,
    COUNT(*) - COUNT(payment_installments) AS installments_nulls,
    COUNT(*) - COUNT(payment_value) AS payment_value_nulls
FROM order_payments;


-- Geolocation: check null values
SELECT
    COUNT(*) - COUNT(geolocation_zip_code_prefix) AS zip_code_nulls,
    COUNT(*) - COUNT(geolocation_lat) AS latitude_nulls,
    COUNT(*) - COUNT(geolocation_lng) AS longitude_nulls,
    COUNT(*) - COUNT(geolocation_city) AS city_nulls,
    COUNT(*) - COUNT(geolocation_state) AS state_nulls
FROM geolocation;