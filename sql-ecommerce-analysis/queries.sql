#Total revenue
SELECT SUM(amount) AS total_revenue FROM orders;

#Revenue by year
SELECT YEAR(order_date) AS year, SUM(amount) AS revenue
FROM orders
GROUP BY year;

#Top 5 customers
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;

#Monthly sales trend
SELECT MONTH(order_date) AS month, SUM(amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

#Repeat customers
SELECT customer_id, COUNT(*) AS orders_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;

#Average order value
SELECT AVG(amount) AS avg_order_value FROM orders;
