-- Group_by: agrupa datos por una o varias columnas
-- utilizando para agrupar una funcion de agregación (count, sum, avg, max)
use world;

select * from country;

select  Continent, count(*) as num_paises from country group by Continent;

select  Continent, sum(Population) as poblacion from country group by Continent;




