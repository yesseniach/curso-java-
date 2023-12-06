
-- Limit
use world;

select * from city;

select * from city order by Population DESC;

select * from city order by Population DESC LIMIT 10;

-- Top 10 paises(country) de mayor surfacearea
select * from country order by SurfaceArea DESC limit 15; 
-- Top 10 paises(country) de mayor Population
select * from country order by Population DESC limit 15;

-- Paginacion, 20 primeros, 20 segundos, 20 terceros, 20 cuartos elementos

-- Opción 1: Primero va el offset y luego el limit cuando se pone 2 números
-- PRIMERA PAGINA
select * from country order by Population DESC LIMIT 20;-- de 1 a 20
-- SEGUNDA PAGINA
select * from country order by Population DESC LIMIT 20, 20;-- de 21 a 40
-- TERCERA PAGINA
select * from country order by Population DESC LIMIT 40, 20;-- de 41 a 60

-- Opción 2: utilizando palabra OFFSET
-- PRIMERA PAGINA
select * from country order by Population DESC LIMIT 20;-- de 1 a 20
-- SEGUNDA PAGINA
select * from country order by Population DESC LIMIT 20 OFFSET 20;-- de 21 a 40
-- TERCERA PAGINA
select * from country order by Population DESC LIMIT 20 OFFSET 40;-- de 41 a 60

