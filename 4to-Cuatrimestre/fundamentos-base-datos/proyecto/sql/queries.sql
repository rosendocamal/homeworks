-- OPERACIONES SOLICITADAS POR LA TIENDA
-- CONSULTA 1: Listado de todos los productos registrados.
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	CATEGORIES.category AS "CATEGORÍA"
FROM PRODUCTS
INNER JOIN CATEGORIES
ON PRODUCTS.categoryId = CATEGORIES.id
ORDER BY PRODUCTS.name asc;

-- CONSULTA 2: Búsqueda de productos por nombre o categoría.
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	CATEGORIES.category AS "CATEGORÍA"
FROM PRODUCTS
INNER JOIN CATEGORIES
ON PRODUCTS.categoryId = CATEGORIES.id
WHERE
	PRODUCTS.name = "REFRESCO COLA 600ML" -- Reemplazar valor de nombre.
ORDER BY PRODUCTS.name asc; -- Búsqueda por nombre.

SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	CATEGORIES.category AS "CATEGORÍA"
FROM PRODUCTS
INNER JOIN CATEGORIES
ON PRODUCTS.categoryId = CATEGORIES.id
WHERE
	CATEGORIES.category = "ALIMENTOS Y BEBIDAS" -- Reemplazar valor de categoría.
ORDER BY PRODUCTS.name asc; -- Búsqueda por categoría.

-- CONSULTA 3: Consulta de las ventas realizadas.
SELECT
	id AS "NO.",
	DAY(fullDate) AS "DÍA",
	fullDate AS "FECHA",
	amount AS "TOTAL"
FROM SALES
ORDER BY fullDate DESC
LIMIT 1000000; -- Límite modificable.

-- CONSULTA 4: Consulta de los productos más vendidos.
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	SUM(SALE_DETAIL.quantity) AS "CANTIDADES VENDIDAS",
	SUM(SALE_DETAIL.totalSale) AS "VENTAS ACUMULADAS (MXN)"
FROM SALE_DETAIL
INNER JOIN PRODUCTS
ON SALE_DETAIL.productId = PRODUCTS.id
GROUP BY PRODUCTS.id
ORDER BY SUM(SALE_DETAIL.quantity) DESC -- Lo más vendido no siempre es lo que más ingresos genera.
LIMIT 100; -- Se puede modificar este límite.

-- CONSULTA 5: Cálculo del total de ventas por periodo.
SELECT
	SUM(amount) AS "VENTAS DEL PERIODO (MXN)"
FROM SALES
WHERE fullDate >= "2026-01-01" AND fullDate < "2027-01-01"; -- Las fechas son entradas del usuario. La fecha final es excluyente, la fecha final es el día siguiente del fin de periodo.

-- CONSULTA 6: Identificación de productos con existencias bajas.
SELECT
	id AS "NO.",
	sku AS "SKU",
	name AS "PRODUCTO",
	stock AS "EXISTENCIAS"
FROM PRODUCTS
ORDER BY stock
LIMIT 100; -- Se puede modificar este límite.

-- CONSULTA 7: Consulta de ventas de un cliente específico.
SELECT -- Consulta por CUSTOMERS.id
	SALES.id AS "TICKET",
	SALES.fullDate AS "FECHA",
	SALES.amount AS "MONTO (MXN)"
FROM SALES
INNER JOIN CUSTOMERS
ON SALES.customerId = CUSTOMERS.id
WHERE
	CUSTOMERS.id = 1 -- Reemplazar valor de ID.
ORDER BY fullDate DESC
LIMIT 1000000;

SELECT -- Consulta por CUSTOMERS.name
	SALES.id AS "TICKET",
	SALES.fullDate AS "FECHA",
	SALES.amount AS "MONTO (MXN)"
FROM SALES
INNER JOIN CUSTOMERS
ON SALES.customerId = CUSTOMERS.id
WHERE
	CUSTOMERS.name = "PÚBLICO GENERAL" -- Reemplazar valor de nombre.
ORDER BY fullDate DESC
LIMIT 1000000;

-- RETO ADICIONAL: Generación de un reporte [no se especificarán los detalles aquí]
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	SUM(SALE_DETAIL.quantity) AS "CANTIDADES VENDIDAS",
	PRODUCTS.salePrice AS "PRECIO DE VENTA",
	SUM(SALE_DETAIL.totalSale) AS "VENTAS ACUMULADAS"
FROM PRODUCTS
INNER JOIN SALE_DETAIL
ON PRODUCTS.id = SALE_DETAIL.productId
GROUP BY PRODUCTS.id
ORDER BY PRODUCTS.name ASC
LIMIT 1000000; -- Límite modificable.