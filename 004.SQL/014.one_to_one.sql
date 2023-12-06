-- crear base de datos one_to_one
DROP SCHEMA IF EXISTS one_to_one;
CREATE SCHEMA one_to_one;
USE one_to_one;

-- crear tabla address
CREATE TABLE address(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
street VARCHAR(250) not null,
postal_code VARCHAR(5),
city VARCHAR(50)
);

-- crear tabla user
CREATE TABLE `users`(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR (100),
id_address INT UNIQUE, -- restriccion de unicidad (único)
FOREIGN KEY (id_address) REFERENCES address(id)
);

select * from address;
select * from users;

INSERT INTO address (street, postal_code, city) VALUES
('Principe de Vergara', '28003', 'Madrid'),
('Rey Felipe 123', '48003', 'Sevilla'),
('Corazon de Maria', '28033', 'Madrid')
;
-- Error Code: 1062. Duplicate entry '1' for key 'user.id_address'
INSERT INTO users(first_name, last_name, email, id_address) VALUES
('Maria', 'Suarez', 'u1@email.com', 1),
('Pepa', 'Lopez', 'u2@email.com', 1),-- no deja guardar por la restriccion one to one
('Fran', 'Perez', 'u3@email.com', 3)
;
INSERT INTO users(first_name, last_name, email, id_address) VALUES
('Maria', 'Suarez', 'u1@email.com', 1),
('Pepa', 'Lopez', 'u2@email.com', 2),
('Fran', 'Perez', 'u3@email.com', 3)
;
