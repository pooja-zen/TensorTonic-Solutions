-- Returns: name, salary.
SELECT name, salary
FROM employees
WHERE (department='Engineering' or department = 'Marketing') AND salary > 70000