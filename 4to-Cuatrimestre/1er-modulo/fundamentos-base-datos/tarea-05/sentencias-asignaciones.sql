-- GESTIÓN DE BASES DE DATOS
SHOW DATABASES; -- Ver bases de datos

CREATE DATABASE school; -- Crear la base de datos para las asignaciones de cursos

USE school; -- Seleccionamos la base de datos a administrar

SELECT DATABASE(); -- Para saber que base de datos está seleccionada

SHOW TABLES; -- Ver LAS tablas de una base de datos

-- DEFINICIÓN DE TABLAS
CREATE TABLE IF NOT EXISTS alumnos (
	id_alumno INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL UNIQUE 
);

CREATE TABLE IF NOT EXISTS cursos (
	id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    creditos FLOAT NOT NULL CHECK(creditos >= 0)
);

CREATE TABLE IF NOT EXISTS inscripciones (
	alumno INT NOT NULL,
    curso INT NOT NULL,
    calificacion FLOAT CHECK(calificacion >= 0 AND calificacion <= 10),
    fecha DATETIME NOT NULL,
    
    PRIMARY KEY (alumno, curso),
    
    FOREIGN KEY (alumno) REFERENCES alumnos(id_alumno),
    FOREIGN KEY (curso) REFERENCES cursos(id_curso)
);

-- MANIPULACIÓN DE DATOS

-- Introducción de datos de los alumnos
INSERT INTO alumnos (nombre, correo)
VALUES ("Alessia", "alessia@axiom.ia");

INSERT INTO alumnos (nombre, correo)
VALUES ("Alison", "alison@axiom.ia");

INSERT INTO alumnos (nombre, correo)
VALUES ("Angelina", "angelina@axiom.ia");

INSERT INTO alumnos (nombre, correo)
VALUES ("Bianca", "bianca@axiom.ia");

-- Introducción de los datos de los cursos
INSERT INTO cursos (nombre, creditos)
VALUES ("Inteligencia Artificial", 250);

INSERT INTO cursos (nombre, creditos)
VALUES ("Machine Learning", 343);

INSERT INTO cursos (nombre, creditos)
VALUES ("Machine Unlearning", 100);

INSERT INTO cursos (nombre, creditos)
VALUES ("Sistemas de Verificación Formal", 300);

INSERT INTO cursos (nombre, creditos)
VALUES ("Interpretabilidad de la IA", 100);

-- Datos de inscripciones

SELECT * FROM alumnos;
SELECT * FROM cursos;
