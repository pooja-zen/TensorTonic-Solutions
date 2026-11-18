-- Returns: name, price, vs_avg.
SELECT p.name, p.price, ROUND(p.price - (SELECT AVG(price) AS avg_price FROM products),2) AS vs_avg
    FROM products as p
    WHERE EXISTS (SELECT 1 FROM sales as s WHERE s.product_id = p.id )
    ORDER BY vs_avg DESC, name ASC