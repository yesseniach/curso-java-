-- Funciones 
use sakila;

-- count()
select * from customer;
select count(*) from customer;

-- utilizando un alias
select customer_id as id from customer;
select count(*) as num_customer from customer;


-- LA COLUMNA id ES OBLIGATORIA Y UNICA , SIEMPRE TIENE VALOR COUNT CONTARA TODAS LAS FILAS 
select count(customer_id) as num_customer from customer; -- 601 filas
-- LA COLUMNA email ES OPCIONAL, SI TIENE NULL ENTONCES COUNT NO CONTARA ESA FILA
select count(email) as num_customer from customer; -- 600 no cuenta los null


-- sum()
-- sumar todos los clientes active
select * from customer;
select sum(`active`)as num_active_customer from customer;-- probar a poner uno a 0 y

select count(*) as total, sum(`active`) as total_active from customer;

SELECT
count(*) AS total,
sum(`active`) AS total_active,
count(*) - sum(`active`) AS total_inactive 
FROM customer;

-- sumar todos los amount de payments
SELECT * FROM payment;
select count(payment_id) as num_payments FROM payment; -- 16k numero de transacciones
select sum(amount) FROM payment; -- 67k 



-- avg: Average, calcula la media

-- Ej 1: avg sobre amount en payment
SELECT sum(amount)/count(*) as avg_amount from payment;
select avg(amount) as avg_amount from payment;
select round(avg(amount), 2) as precio_medio from payment;

-- Ej 2: avg sobre length en tabla film
select * from film;
select avg(`length`) as duracion_media from film;
select round(avg(`length`), 0) as duracion_media from film;

-- min: obtener el valor minimo
select * from film;
select min(`length`) from film;
select min(`length`) as min_duration from film;
-- max: obtener el valor maximo
select * from film;
select max(`length`) as max_duration from film;

-- year: xtraer el año a partir de una fecha
-- Ej 1:sobre create_date de customer
select * from customer;
select 
year(create_date) as `año`,
month(create_date) as `nombre_mes`, -- 1 a 12
monthname(create_date) as `nombre_mes`,
week(create_date) as `semana`, -- 1 a 52
dayofyear(create_date) as `dia`, -- 1 a 365
dayofmonth(create_date) as `dia_mes`, -- 1 a 31
dayofweek(create_date) as `dia_semana` -- 1 a 7
from customer;

-- Ej 2: sobre payment_date de payment
select * from payment;
select 
payment_date as `fecha_original`,
date(payment_date) as `fecha_sin_tiempo`,
year(payment_date) as `año`,
month(payment_date) as `nombre_mes`,
monthname(payment_date) as `nombre_mes`,
week(payment_date) as `semana`,
dayofyear(payment_date) as `dia`,
dayofmonth(payment_date) as `dia_mes`,
dayofweek(payment_date) as `dia_semana`
from payment;

-- concat, length, upper, lower
select * from customer;

select concat(first_name, '_', last_name) as full_name from customer;

select  first_name, length(first_name) as `longuitud` from customer;

select lower(first_name) as `nombre`,length(first_name)as `longuitud` from customer;

-- desc
select  
 first_name, 
 length(first_name) as `longuitud`
order by length(first_name) desc;
