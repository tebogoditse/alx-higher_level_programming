-- Displays the average temperature (Fahrenheit) by city
SELECT city, AGV(value) AS avg_temp 
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
