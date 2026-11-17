-- Returns: name, salary, dept_name.
SELECT e.name, e.salary, d.dept_name
FROM employees AS e
INNER JOIN departments AS d
ON e.dept_id = d.id
ORDER BY name ASC NULLS LAST