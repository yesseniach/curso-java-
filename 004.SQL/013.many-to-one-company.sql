-- crear tabla company
CREATE TABLE IF NOT EXISTS company (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
cif VARCHAR(9) NOT NULL,
phone VARCHAR(12)
);
-- crear tabla employee, con foreign key a company
CREATE TABLE IF NOT EXISTS employee(
id  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nif VARCHAR(9) NOT NULL,
salary DECIMAL(12, 2),
id_company INT,
FOREIGN KEY (id_company) REFERENCES company(id)
);
-- Insert company
INSERT INTO company(cif, phone) 
VALUES 
('B23456789', '111111111'),
('B45678912', '222222222'),
('B87654321', '333333333');

select * from company;

-- insert employee
INSERT INTO employee(nif, salary, id_company)
VALUES
('11111111T',  null, 1),
('22222222E',  '25000.0', 1), 
('33333333C',  '35000.0', 1);

select * from employee;
-- DELETE company que tenga employees asociados y comprobar que no deja borrar
-- Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fail

-- contar el número de empleados
select count(*) as num_employees from employee group by id_company;

-- Para poder borrar la company 1 primero hay que poner a NULL el id_company en employees
UPDATE employee SET id_company = NULL where id = 1;
UPDATE employee SET id_company = NULL where id = 2;
UPDATE employee SET id_company = NULL where id = 3;
-- ahora deberia dejar borrar empresa porque hemos desasociado los employees
DELETE FROM company WHERE id = 1;





