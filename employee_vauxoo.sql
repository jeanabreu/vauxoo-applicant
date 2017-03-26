-- Your sql code in this file
-- NOTE: Please, don't add sentence to create database in this script file.
--       You can create database locally to test it.
--       Consider add ';' at end sentence.


CREATE TABLE employee (
	id bigserial primary key,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL
);

CREATE TABLE employee_department (
	id bigserial primary key,
	name varchar(50) NOT NULL,
	description text NOT NULL
); 

INSERT INTO employee (first_name, last_name)
VALUES	('Jean','Abreu'),
		('Jose','Perez'),
		('Maria','Matinez'),
		('Julia','Peralta');	

INSERT INTO employee_department (name, description)
VALUES	('Logistica','Departamento de Operaciones y Logistica'),
		('Tecnologia','Departamento de Tecnologia de la Informacion'),
		('RRHH','Departamento de Recursos Humanos'),
		('Mercadeo','Departamento de Mercadeo'),
		('Finanzas','Departamento de Contabilidad y Finanzas'),
		('Servicios','Departamento de Servicios Generales');

INSERT INTO employee_department (name, description)
VALUES	('Sin Asignar','Empleado sin Departamento asignado');

ALTER TABLE employee ADD COLUMN department_id smallint NOT NULL DEFAULT 7;

UPDATE employee SET department_id = 5 WHERE id = 1;	
UPDATE employee SET department_id = 2 WHERE id = 2;	
UPDATE employee SET department_id = 5 WHERE id = 3;	
UPDATE employee SET department_id = 3 WHERE id = 4;	

SELECT e.id, e.first_name, e.last_name, d.description as department
FROM employee e, employee_department d
WHERE e.department_id = d.id
ORDER BY e.id ASC ;


--sql2 

CREATE TABLE employee_hobby (
	id bigserial primary key,
	name varchar(20) NOT NULL,
	description text NOT NULL
); 

INSERT INTO employee_hobby (name, description)
VALUES	('Soccer','Futbol Soccer y relacionados'),
		('Natacion','Natacion, Deportes Acuaticos y relacionados'),
		('Musica','Composicion, Canto y relacionados');

CREATE TABLE employee_hobby_rel (
	id bigserial primary key,
	employee_id int NOT NULL,
	hobby_id int NOT NULL
); 


INSERT INTO employee_hobby_rel (employee_id, hobby_id)
VALUES	(1,1),(1,2),
		(2,2),(2,1),
		(3,1),(3,3),
		(4,2),(4,3);
		
SELECT e.id, e.first_name, e.last_name, h.description as hobby
FROM employee e, employee_hobby h, employee_hobby_rel hl
WHERE e.id = hl.employee_id and h.id = hl.hobby_id
ORDER BY e.id ASC ;

-- ...
