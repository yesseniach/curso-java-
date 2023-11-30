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
select max(`length`) from film;
select max(`length`) as max_duration from film;