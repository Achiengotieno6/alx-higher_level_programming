-- displays the average temperature (Fahrenheit) by city ordered by temperature

SELECT city, AVG(Value) As avg_temp
	FROM temperatures
	GROUP BY city
	ORDER BY city
	ORDER avg_temp DESC;
