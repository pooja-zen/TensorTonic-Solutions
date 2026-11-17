-- Returns: avg_daily_orders, avg_daily_revenue, busiest_day_orders.
SELECT ROUND(AVG(daily_orders),2) AS avg_daily_orders, ROUND(AVG(daily_revenue),2) AS avg_daily_revenue, MAX(daily_orders) AS busiest_day_orders
FROM(
    SELECT COUNT(*) AS daily_orders, SUM(amount) AS daily_revenue
    FROM orders
    GROUP bY order_date)
