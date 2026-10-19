-- Maquetacion de la base de datos en SQLite
-- Sintaxis para introducir datos

INSERT INTO carreras(id, carrera)
VALUES (?, ?);

INSERT INTO planteles(id, plantel)
VALUES (?, ?);

INSERT INTO oferta_academica(id, id_plantel, id_carrera)
VALUES (?, ?, ?);

INSERT INTO aspirantes(curp, aspirante)
VALUES (?, ?);

INSERT INTO asignaciones(folio, id_aspirante, id_oferta_asignada)
VALUES (?, ?, ?);