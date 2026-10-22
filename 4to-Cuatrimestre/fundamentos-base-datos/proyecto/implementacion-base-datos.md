# Gestión de base de datos

```sql
SHOW DATABASES; -- Ver bases de datos existentes en el servidor.

CREATE DATABASE IF NOT EXISTS PURCHASE_SALE_MANAGEMENT; -- Crear la base de datos.

USE PURCHASE_SALE_MANAGEMENT; -- Seleccionar la base de datos anteriormente creada.

SELECT DATABASE(); -- Verificamos que base de datos tenemos seleccionada.

SHOW TABLES; -- Verificamos las tablas que contiene nuestra base de datos.
```

# Definición de tablas

```sql
-- Tabla de Categorías
CREATE TABLE IF NOT EXISTS CATEGORIES (
	id INT AUTO_INCREMENT,
	category VARCHAR(50) NOT NULL UNIQUE,
	
	PRIMARY KEY (id)
);

-- Tabla de Productos
CREATE TABLE IF NOT EXISTS PRODUCTS (
	id INT AUTO_INCREMENT,
	sku VARCHAR(30) NOT NULL UNIQUE,
	name VARCHAR(50) NOT NULL,
	salePrice DECIMAL(10, 2) NOT NULL CHECK (salePrice >= 0),
	stock INT NOT NULL,
	categoryId INT NOT NULL,
	
	PRIMARY KEY (id),
	FOREIGN KEY (categoryId) REFERENCES CATEGORIES(id)
);

-- Tabla de Proveedores
CREATE TABLE IF NOT EXISTS SUPPLIERS (
	id INT AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	phoneNumber VARCHAR(20) NOT NULL UNIQUE,
	
	PRIMARY KEY (id)
);

-- Tabla de Pedidos
CREATE TABLE IF NOT EXISTS ORDERS (
	id INT AUTO_INCREMENT,
	supplierId INT NOT NULL,
	fullDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	costOrder DECIMAL(10, 2) NOT NULL CHECK (costOrder >= 0),
	
	PRIMARY KEY (id),
	FOREIGN KEY (supplierId) REFERENCES SUPPLIERS(id)
);

-- Tabla de Recepciones
CREATE TABLE IF NOT EXISTS ENTRIES (
	id INT AUTO_INCREMENT,
	orderId INT NOT NULL,
	reference VARCHAR(36) NOT NULL,
	fullDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	costEntry DECIMAL(10, 2) NOT NULL CHECK (costEntry >= 0),
	
	PRIMARY KEY (id),
	FOREIGN KEY (orderId) REFERENCES ORDERS(id)
);

-- Tabla de Clientes
CREATE TABLE IF NOT EXISTS CUSTOMERS (
	id INT AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	phoneNumber VARCHAR(20) NOT NULL UNIQUE,
	
	PRIMARY KEY (id)
);

-- Tabla de Ventas
CREATE TABLE IF NOT EXISTS SALES (
	id INT AUTO_INCREMENT,
	fullDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	customerId INT NOT NULL,
	amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 0),
	
	PRIMARY KEY (id),
	FOREIGN KEY (customerId) REFERENCES CUSTOMERS(id)
);

-- Catálogo de Proveedor
CREATE TABLE IF NOT EXISTS SUPPLIER_CATALOGO (
	supplierId INT,
	productId INT,
	unitCost DECIMAL(10, 2) NOT NULL CHECK (unitCost >= 0),
	
	PRIMARY KEY (supplierId, productId),
	FOREIGN KEY (supplierId) REFERENCES SUPPLIERS(id),
	FOREIGN KEY (productId) REFERENCES PRODUCTS(id)
);

-- Detalle de Recepción
CREATE TABLE IF NOT EXISTS ENTRY_DETAIL (
	entryId INT,
	productId INT,
	quantity INT NOT NULL CHECK (quantity >= 0),
	unitCost DECIMAL(10, 2) NOT NULL CHECK (unitCost >= 0),
	totalCost DECIMAL(10, 2) NOT NULL CHECK (totalCost >= 0),
	
	PRIMARY KEY (entryId, productId),
	FOREIGN KEY (entryId) REFERENCES ENTRIES (id),
	FOREIGN KEY (productId) REFERENCES PRODUCTS (id)
);

-- Detalle de Pedido
CREATE TABLE IF NOT EXISTS ORDER_DETAIL (
	orderId INT,
	productId INT,
	quantity INT NOT NULL CHECK (quantity >= 0),
	unitCost DECIMAL(10, 2) NOT NULL CHECK (unitCost >= 0),
	totalCost DECIMAL(10, 2) NOT NULL CHECK (totalCost >= 0),
	
	PRIMARY KEY (orderId, productId),
	FOREIGN KEY (orderId) REFERENCES ORDERS (id),
	FOREIGN KEY (productId) REFERENCES PRODUCTS (id)
);

-- Detalle de Venta
CREATE TABLE IF NOT EXISTS SALE_DETAIL (
	ticket INT,
	productId INT,
	quantity INT NOT NULL CHECK (quantity >= 0),
	unitPrice DECIMAL(10, 2) NOT NULL CHECK (unitPrice >= 0),
	totalSale DECIMAL(10, 2) NOT NULL CHECK (totalSale >= 0),
	
	PRIMARY KEY (ticket, productId),
	FOREIGN KEY (ticket) REFERENCES SALES(id),
	FOREIGN KEY (productId) REFERENCES PRODUCTS(id)
);
```

# Consultas

```sql
-- Listado de todos los productos registrados.
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	CATEGORIES.category AS "CATEGORÍA"
FROM PRODUCTS
INNER JOIN CATEGORIES
ON PRODUCTS.categoryId = CATEGORIES.id
ORDER BY PRODUCTS.name asc;

-- Búsqueda de productos por nombre o categoría.
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	CATEGORIES.category AS "CATEGORÍA"
FROM PRODUCTS
INNER JOIN CATEGORIES
ON PRODUCTS.categoryId = CATEGORIES.id
WHERE
	PRODUCTS.name = "NAME_INPUT" OR -- Reemplazar NAME_INPUT.
	CATEGORIES.category = "CATEGORY_INPUT" -- Reemplazar CATEGORY_INPUT.
ORDER BY PRODUCTS.name asc;

-- Consulta de las ventas realizadas.
SELECT
	id AS "NO.",
	DAY(fullDate) AS "DÍA",
	fullDate AS "FECHA",
	amount AS "TOTAL"
FROM SALES
ORDER BY fullDate DESC
LIMIT 1000000; -- Límite modificable.

-- Consulta de los productos más vendidos.
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

-- Cálculo del total de ventas por periodo.
SELECT
	SUM(amount) AS "VENTAS DEL PERIODO (MXN)"
FROM SALES
WHERE fullDate >= "YYYY-MM-DD" AND fullDate < "YYYY-MM-DD"; -- Las fechas son entradas del usuario. La fecha final es excluyente, la fecha final es el día siguiente del fin de periodo.

-- Identificación de productos con existencias bajas.
SELECT
	id AS "NO.",
	sku AS "SKU",
	name AS "PRODUCTO",
	stock AS "EXISTENCIAS"
FROM PRODUCTS
ORDER BY stock
LIMIT 100; -- Se puede modificar este límite.

-- Consulta de ventas de un cliente específico.
SELECT -- Consulta por CUSTOMERS.id
	SALES.id AS "TICKET",
	SALES.fullDate AS "FECHA",
	SALES.amount AS "MONTO (MXN)"
FROM SALES
INNER JOIN CUSTOMERS
ON SALES.customerId = CUSTOMERS.id
WHERE
	CUSTOMERS.id = INT_INPUT -- Reemplazar INT_INPUT.
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
	CUSTOMERS.name = "NAME_INPUT" -- Reemplazar NAME_INPUT.
ORDER BY fullDate DESC
LIMIT 1000000;

-- Generación de un reporte [no se especificarán los detalles aquí]
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	SUM(SALE_DETAIL.quantity) AS "CANTIDADES VENDIDAS",
	AVG(SALE_DETAIL.unitPrice) AS "PRECIO DE VENTA PROMEDIO", -- Precio de venta promedio.
	SUM(SALE_DETAIL.totalSale) AS "VENTAS ACUMULADAS"
FROM PRODUCTS
INNER JOIN SALE_DETAIL
ON PRODUCTS.id = SALE_DETAIL.productId
GROUP BY PRODUCTS.id
ORDER BY PRODUCTS.name ASC
LIMIT 1000000; -- Límite modificable.
```