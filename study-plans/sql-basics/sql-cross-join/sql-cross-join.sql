-- Returns: segment_name, metric_name.
SELECT s.segment_name, m.metric_name 
FROM segments as s 
CROSS JOIN metrics as m
ORDER BY s.segment_name ASC NULLS LAST, m.metric_name ASC NULLS LAST