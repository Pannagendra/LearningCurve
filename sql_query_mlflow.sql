'''SQL query to list the 5 latest successful model runs with accuracy > 90%.'''
SELECT run_id, experiment_id, metrics->>'accuracy' AS accuracy, end_time
FROM mlflow.runs
WHERE status = 'FINISHED'
AND CAST(metrics->>'accuracy' AS FLOAT) > 0.9
ORDER BY end_time DESC
LIMIT 5;
