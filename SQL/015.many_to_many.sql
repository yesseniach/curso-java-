DROP SCHEMA IF EXISTS many_to_many;
CREATE SCHEMA many_to_many;
USE many_to_many;

-- Crear tabla libro
CREATE TABLE book(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
title VARCHAR (100),
author VARCHAR (100),
num_pages INT
);

-- Crear tabla categoria
CREATE TABLE category(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
min_age INT
);

-- Crear tabla libro_categoria
CREATE TABLE book_category(
id_book INT,
id_category INT,
PRIMARY KEY (id_book, id_category),-- clave primaria compuesta
FOREIGN KEY (id_book) REFERENCES book(id),
FOREIGN KEY (id_category) REFERENCES category(id)
);