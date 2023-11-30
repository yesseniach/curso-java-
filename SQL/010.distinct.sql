-- distinct
use sakila;
select * from actor;

select first_name from actor; -- 200
select first_name from actor order by first_name;
select distinct first_name from actor; -- 128

-- cuantos años tenemos de peliculas

select distinct release_year from film;
