-- Returns: customer, order_count, total_spent.
WITH selected_customers AS 
    (SELECT customer, COUNT(*) AS order_count, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer)
SELECT customer, order_count, total_spent
FROM selected_customers
WHERE order_count > 1
ORDER BY total_spent DESC, customer ASC