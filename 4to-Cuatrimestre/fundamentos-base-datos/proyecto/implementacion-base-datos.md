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

# Consultas principales

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
	PRODUCTS.salePrice AS "PRECIO DE VENTA",
	SUM(SALE_DETAIL.totalSale) AS "VENTAS ACUMULADAS"
FROM PRODUCTS
INNER JOIN SALE_DETAIL
ON PRODUCTS.id = SALE_DETAIL.productId
GROUP BY PRODUCTS.id
ORDER BY PRODUCTS.name ASC
LIMIT 1000000; -- Límite modificable.
```

# Consultas secundarias

```sql
-- Vista de Productos
SELECT
	PRODUCTS.id AS "NO.",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	PRODUCTS.salePrice AS "PRECIO DE VENTA",
	PRODUCTS.stock AS "EXISTENCIAS",
	CATEGORIES.category AS "CATEGORÍA"
WHERE PRODUCTS
INNER JOIN CATEGORIES
ON PRODUCTS.categoryId = CATEGORIES.id
ORDER BY PRODUCTS.name ASC;

-- Vista de Proveedores
SELECT
	id AS "NO.",
	name AS "PROVEEDOR",
	email AS "CORREO ELECTRÓNICO",
	phoneNumber AS "TELEFÓNO"
WHERE SUPPLIERS
ORDER BY name ASC;

-- Vista de Recepciones
SELECT
	ENTRIES.id AS "NO. RECEPCIÓN",
	ORDERS.id AS "NO. PEDIDO",
	SUPPLIERS.id AS "NO. PROVEEDOR"
	SUPPLIERS.name AS "PROVEEDOR",
	ENTRIES.reference AS "REFERENCIA",
	DATE(ENTRIES.fullDate) AS "FECHA DE RECEPCIÓN",
	ENTRIES.costEntry AS "COSTO RECEPCIÓN (MXN)"
FROM ENTRIES
INNER JOIN ORDERS
ON ENTRIES.orderId = ORDERS.id
INNER JOIN SUPPLIERS
ON ORDERS.supplierId = SUPPLIERS.id
ORDER BY ENTRIES.fullDate DESC;
 
-- Vista de Pedidos
SELECT
	ORDERS.id AS "NO. PEDIDO",
	SUPPLIERS.id AS "NO. PROVEEDOR",
	SUPPLIERS.name AS "PROVEEDOR",
	DATE(ORDERS.fullDate) AS "FECHA DE PEDIDO",
	ORDERS.costOrder AS "COSTO PEDIDO (MXN)"
FROM ORDERS
INNER JOIN SUPPLIERS
ON ORDERS.supplierId = SUPPLIERS.id
ORDER BY ENTRIES.fullDate DESC;

-- Vista de Ventas
SELECT
	DAY(fullDate) AS "DÍA",
	DATE(fullDate) AS "FECHA",
	id AS "NO. TICKET",
	amount AS "TOTAL"
FROM SALES
ORDER BY fullDate DESC;

-- Vista de Clientes
SELECT
	id AS "NO. CLIENTE",
	name AS "NOMBRE",
	email AS "CORREO ELECTRÓNICO",
	phoneNumber AS "TELEFÓNO"
FROM CUSTOMERS
ORDER BY name ASC;

-- Vista de Categorías
SELECT
	id AS "NO.",
	category AS "CATEGORÍA"
FROM CATEGORIES;

-- Catálogo de proveedor
SELECT
	SUPPLIERS.id AS "NO. PROVEEDOR",
	SUPPLIERS.name AS "PROVEEDOR",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO",
	SUPPLIER_CATALOGO.unitCost AS "COSTO UNITARIO"
FROM SUPPLIER_CATALOGO
INNER JOIN SUPPLIERS
ON SUPPLIER_CATALOGO.supplierId = SUPPLIERS.id
INNER JOIN PRODUCTS
ON SUPPLIER_CATALOGO.productId = PRODUCTS.id
ORDER BY SUPPLIERS.name, PRODUCTS.name;

-- Detalles de recepciones
SELECT
	ENTRIES.id AS "NO. RECEPCIÓN",
	ORDERS.id AS "NO. PEDIDO",
	SUPPLIERS.id AS "NO. PROVEEDOR"
	SUPPLIERS.name AS "PROVEEDOR",
	ENTRIES.reference AS "REFERENCIA",
	DATE(ENTRIES.fullDate) AS "FECHA DE RECEPCIÓN",
	PRODUCTS.sku AS "SKU",
	PRODUCTS.name AS "PRODUCTO RECIBIDO",
	PRODUCTS.quantity AS "CANTIDAD RECIBIDA",
	ENTRY_DETAIL.unitCost AS "COSTO UNITARIO",
	ENTRY_DETAIL.totalCost AS "COSTO TOTAL"
FROM ENTRIES_DETAIL
INNER JOIN ORDERS
ON ENTRIES.orderId = ORDERS.id
INNER JOIN SUPPLIERS
ON ORDERS.supplierId = SUPPLIERS.id
INNER JOIN PRODUCTS
ON ENTRIES_DETAIL.productId = PRODUCTS.id
ORDER BY ENTRIES.fullDate DESC, SUPPLIERS.name, PRODUCTS.name;

-- Detalles de pedidos


-- Tickets

```

# Operaciones de inserción de datos

```sql
-- Ingreso de datos a categorías
-- Ingreso de datos de productos
-- Ingreso de datos de proveedores
-- Ingreso de datos de pedidos
-- Ingreso de datos de recepciones
-- Ingreso de datos de clientes
-- Ingreso de datos de ventas
-- Creación de catálogo de proveedor
-- Creación de detalles de recepción
-- Creación de detalles de pedido
-- Creación de detalles de venta
```

# Inserción fundamental de datos

```sql
-- Primera inserción de datos para dejar habilitada la base de datos y lista para su uso.
```

# Inserción masiva de datos

```sql
-- Inserción de 10 categorías de productos
-- Inserción de 10 productos
-- Inserción de 10 proveedores
-- Inserción de 10 pedidos
-- Inserción de 10 recepciones
-- Inserción de 10 clientes
-- Inserción de 10 ventas
-- Inserción de 10 catalogos de proveedor
-- Inserción de 10 detalles de recepciones
-- Inserción de 10 detalles de pedidos
-- Inserción de 10 detales de venta
```