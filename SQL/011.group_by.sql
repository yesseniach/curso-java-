-- Group_by: agrupa datos por una o varias columnas
-- utilizando para agrupar una funcion de agregación (count, sum, avg, max)
use world;

select * from country;

-- Contar el número de paises de cad continente
select  Continent, count(*) as num_paises from country group by Continent;

-- Suma de poblacion en los paises agrupados por continente
select  Continent, sum(Population) as poblacion from country group by Continent;

-- Esperanza de vida media (MEDIA) LifeExpectancy agrupado por continente
SELECT Continent,
round(avg(LifeExpectancy),2) as esp_vida_media 
FROM country
GROUP BY Continent;

-- Esperanza de vida media (MEDIA) LifeExpectancy agrupado por region
SELECT Region, 
round(avg(LifeExpectancy),2) as esp_vida_media
FROM Country
GROUP BY Region
ORDER BY avg(LifeExpectancy) DEsC; -- desc

-- Número de idiomas por país countrylanguage
select * from countrylanguage;

select CountryCode, COUNT(Language) from countrylanguage group by CountryCode;

-- filtro sobre una agrupación con having
-- número de idiomas por país countrylanguage pero filtrando solo
-- los que tengan mas de 5 idiomas
select CountryCode, COUNT(Language)
from countrylanguage
group by COuntryCode
having Count(language) >5;


-- SAKILA GROUP BY

use sakila;
-- duracion media length agrupada por rating en tabla film
-- filtrando entre una lista de films ('PG', 'G', 'R')
select * from film;
SELECT rating, avg(Length) as duracion_media 
FROM film
WHERE rating = 'R' OR rating = 'PG' OR rating = 'G'
GROUP BY rating having duracion_media >= 100;

SELECT rating, avg(Length) as duracion_media 
FROM film
WHERE rating IN ('PG', 'G', 'R')
GROUP BY rating having duracion_media >= 100;




