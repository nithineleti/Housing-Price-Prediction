Average House Price by Ocean Proximity
  
SELECT ocean_proximity, AVG(median_house_value) AS avg_price
FROM housing
GROUP BY ocean_proximity
ORDER BY avg_price DESC;


Top 10 Most Expensive Houses
SELECT *
FROM housing
ORDER BY median_house_value DESC
LIMIT 10;


Average Income by Location

SELECT ocean_proximity, AVG(median_income) AS avg_income
FROM housing
GROUP BY ocean_proximity;


Population vs Average House Price

SELECT population, AVG(median_house_value)
FROM housing
GROUP BY population
ORDER BY population;


