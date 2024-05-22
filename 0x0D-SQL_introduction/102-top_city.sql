-- Displays the top 3 hottest Cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE MONTH IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
