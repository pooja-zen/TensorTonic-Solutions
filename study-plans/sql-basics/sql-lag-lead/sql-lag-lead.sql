-- Returns: month, revenue, prev_revenue, revenue_change.
SELECT month, revenue, LAG(revenue, 1, 0) OVER(ORDER BY month, id) AS prev_revenue, (revenue - prev_revenue) AS revenue_change
    FROM monthly_revenue
    ORDER BY month ASC, id ASC