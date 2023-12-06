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
INSERT INTO book (title, author, num_pages) VALUES
('Evaluna', 'Isabel Allende', 500),
('Cien años de soledad', 'Gabriel Garcia Marcos', 700),
('Doña Flor y sus dos maridos', 'Jorge Amado', 900);

INSERT INTO category (name, min_age) VALUES
('acción', 8),
('comedia', 7),
('romance', 7);

select * from book;
select * from category;
select * from book_category;
INSERT INTO book_category (id_book, id_category) VALUES 
(1, 1), -- Asocia acción a book1
(1, 2), -- Asocia comedia a book1
-- (1, 1) -- Asocia acción a book1 -- no se puede porque ya lo está
(3, 1)
;
-- Resultado:
-- El libro 1 tiene categorias acción y comedia
-- El libro 3 tiene categoría acción

-- Si se vuelve a ejecutar el insert tal cual da error porque no se puede duplicar
-- una categoría en un mismo libro
-- Error Code: 1062. Duplicate entry '1-1' for key 'book_category.PRIMARY'

