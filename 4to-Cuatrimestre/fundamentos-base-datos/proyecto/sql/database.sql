-- BASES DE DATOS

CREATE DATABASE IF NOT EXISTS PURCHASE_SALE_MANAGEMENT; -- Crear la base de datos.

USE PURCHASE_SALE_MANAGEMENT; -- Seleccionar la base de datos anteriormente creada.

-- Tabla de Categorías
CREATE TABLE IF NOT EXISTS CATEGORIES (
	id INT AUTO_INCREMENT,
	category VARCHAR(50) NOT NULL UNIQUE,
	
	PRIMARY KEY (id)
);

-- TABLAS
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


-- CARGA DE DATOS
-- Registrar categorías, sola la categoría GENERAL es obligatoria al principio.
INSERT INTO CATEGORIES (category)
VALUES
	("ALIMENTOS Y BEBIDAS"),
	("ALIMENTOS FRESCOS"),
	("CUIDADO PERSONAL Y BELLEZA"),
	("LIMPIEZA DEL HOGAR"),
	("MODA, ROPA Y CALZADO"),
	("ELECTRÓNICA Y TECNOLOGÍA"),
	("ELECTRODOMÉSTICOS Y HOGAR"),
	("FARMACIA Y SALUD"),
	("MASCOTAS"),
	("JUGUETERÍA Y ENTRETENIMIENTO"),
	("GENERAL");

-- Registrar productos, aquí es necesario los productos para poder vender.
INSERT INTO PRODUCTS (sku, name, salePrice, stock, categoryId)
VALUES
	("AB-001", "REFRESCO COLA 600ML", 18.50, 0, 1),  
	("AB-002", "ARROZ EXTRA GRANO ENTERO 1KG", 24.00, 0, 1),  
	("FR-001", "PLATANO TABASCO KG", 29.90, 0, 2),  
	("FR-002", "LECHE ENTERA PASTEURIZADA 1L", 27.50, 0, 2),  
	("CP-001", "CHAMPU CONTROL CASPA 400ML", 65.00, 0, 3),  
	("CP-002", "PASTA DENTAL MAX FRESCURA 100ML", 32.50, 0, 3),  
	("LH-001", "DETERGENTE LIQ ROPA COLOR 1L", 48.00, 0, 4),  
	("LH-002", "PAPEL HIGIENICO MULTIROLLO 4PZ", 35.00, 0, 4),  
	("MR-001", "PLAYERA CABALLERO ALGODON G", 129.00, 0, 5),  
	("MR-002", "TENIS DEPORTIVO NEGRO MULTITALLA", 599.00, 0, 5),  
	("ET-001", "SMART TV LED 43 PULGADAS 4K", 4499.00, 0, 6),  
	("ET-002", "CABLE DE CARGA USB C A C 1M", 99.00, 0, 6),  
	("EH-001", "LICUADORA 2 VELOCIDADES VASO VIDRIO", 450.00, 0, 7),  
	("EH-002", "HORNO DE MICROONDAS 0.7P3 GRIS", 1399.00, 0, 7),  
	("FS-001", "PARACETAMOL TABLETAS 500MG 20PZ", 25.00, 0, 8),  
	("FS-002", "ALCOHOL GEL ANTIBACTERIAL 500ML", 42.00, 0, 8),  
	("PM-001", "ALIMENTO PERRO ADULTO RAZA MDA 2KG", 185.00, 0, 9),  
	("PM-002", "ARENA GATO CONTROL OLOR 5KG", 120.00, 0, 9),  
	("JE-001", "JUEGO DE MESA ESTRATEGIA FAMILIAR", 299.00, 0, 10),  
	("JE-002", "MUNECA ARTICULADA CON ACCESORIOS", 249.00, 0, 10);

-- Registrar proveedores.
INSERT INTO SUPPLIERS (name, email, phoneNumber)
VALUES
	("DISTRIBUIDORA DE ABARROTES SA", "contacto@distribuidora.abarrotes.com.mx", "525551111234"),  
	("ALIMENTOS FRESCOS DEL CAMPO", "ventas@alimentosfrescoscampo.com.mx", "525552222345"),  
	("PRODUCTOS DE BELLEZA CORPORAL", "info@bellezacorporal.com.mx", "525553333456"),  
	("QUIMICOS Y LIMPIEZA NACIONAL", "contacto@quimicoslimpieza.com.mx", "525554444567"),  
	("TEXTILES Y MODA MAYORISTA", "ventas@textilesymodamayorista.com", "525555555678"),  
	("TECNOLOGIA Y ELECTRONICA MX", "soporte@tecnologiamx.com.mx", "525556666789"),  
	("ELECTRODOMESTICOS DEL HOGAR", "comercial@electrodomesticoshogar.com", "525557777890"),  
	("FARMACEUTICA Y SALUD GLOBAL", "contacto@farmaceuticasalud.com.mx", "525558888901"),  
	("LOGISTICA Y NUTRICION ANIMAL", "ventas@nutricionanimal.com.mx", "525559999012"),  
	("DISTRIBUIDORA DE JUGUETES MEX", "info@juguetesmex.com.mx", "525550000123");
	
-- Registrar Catálogo de Proveedores, primero se debe tener a la mano los números de proveedor y su producto.
SELECT * FROM SUPPLIERS; -- Para ver identificadores de proveedor.
SELECT * FROM PRODUCTS; -- Para ver identificadores de producto.

INSERT INTO SUPPLIER_CATALOGO (supplierId, productId, unitCost)
VALUES
	(1, 1, 12.95),
	(1, 2, 16.80),
	(2, 3, 20.93),
	(2, 4, 19.25),
	(3, 5, 45.50),
	(3, 6, 22.75),
	(4, 7, 33.60),
	(4, 8, 24.50),
	(5, 9, 90.30),
	(5, 10, 419.30),
	(6, 11, 3149.30),
	(6, 12, 69.30),
	(7, 13, 315.00),
	(7, 14, 979.30),
	(8, 15, 17.50),
	(8, 16, 29.40),
	(9, 17, 129.50),
	(9, 18, 84.00),
	(10, 19, 209.30),
	(10, 20, 174.30);
	
-- Registrar Clientes, solo el cliente general es obligatorio.
INSERT INTO CUSTOMERS (name, email, phoneNumber)
VALUES
	("PÚBLICO GENERAL", "null@tiendacomercial.com", "000000000000"),
	("MARIA RODRIGUEZ LOPEZ", "maria.rodriguez@email.com", "525552345678"),
	("ALEJANDRO MARTINEZ DIAZ", "alejandro.martinez@email.com", "525553456789"),
	("ANA HERNANDEZ SILVA", "ana.hernandez@email.com", "525554567890"),  
	("CARLOS RAMIREZ TORRES", "carlos.ramirez@email.com", "525555678901"),  
	("LAURA FLORES CASTRO", "laura.flores@email.com", "525556789012"),  
	("REGINA SANCHEZ RUIZ", "regina.sanchez@email.com", "525557890123"),  
	("DIEGO ESPINOZA MEJIA", "diego.espinoza@email.com", "525558901234"),  
	("SOFIA MORALES ORTIZ", "sofia.morales@email.com", "525559012345"),
	("JAVIER GUTIERREZ REYES", "javier.gutierrez@email.com", "525550123456");

-- Realización de un pedido y generación de su detalle.
SELECT * FROM SUPPLIERS; -- Número de proveedor

INSERT INTO ORDERS (supplierId, fullDate, costOrder)
VALUES
	(1, NOW(), 0.00),
	(2, NOW(), 0.00),
	(3, NOW(), 0.00),
	(4, NOW(), 0.00),
	(5, NOW(), 0.00),
	(6, NOW(), 0.00),
	(7, NOW(), 0.00),
	(8, NOW(), 0.00),
	(9, NOW(), 0.00),
	(10, NOW(), 0.00); -- Se genera varios pedidos sin solicitar productos.

INSERT INTO ORDER_DETAIL (orderId, productId, quantity, unitCost, totalCost)
VALUES
	(1, 1, 10, 12.95, 129.50),
	(1, 2, 5, 16.80, 84.00),
	(2, 3, 15, 20.93, 313.95),
	(2, 4, 20, 19.25, 385.00),
	(3, 5, 8, 45.50, 364.00),
	(3, 6, 12, 22.75, 273.00),
	(4, 7, 6, 33.60, 201.60),
	(4, 8, 25, 24.50, 612.50),
	(5, 9, 15, 90.30, 1354.50),
	(5, 10, 4, 419.30, 1677.20),
	(6, 11, 2, 3149.30, 6298.60),
	(6, 12, 50, 69.30, 3465.00),
	(7, 13, 10, 315.00, 3150.00),
	(7, 14, 3, 979.30, 2937.90),
	(8, 15, 40, 17.50, 700.00),
	(8, 16, 30, 29.40, 882.00),
	(9, 17, 12, 129.50, 1554.00),
	(9, 18, 18, 84.00, 1512.00),
	(10, 19, 7, 209.30, 1465.10),
	(10, 20, 9, 174.30, 1568.70); -- Se añade productos a cada pedido, también es necesario primero utilizar las consultas secundarias para ver catálogo de productos.

UPDATE ORDERS
SET ORDERS.costOrder = (
	SELECT SUM(ORDER_DETAIL.totalCost)
	FROM ORDER_DETAIL
	WHERE ORDER_DETAIL.orderId = ORDERS.id
); -- Se actualiza los valores de los pedidos.

-- Recepción de mercancías.
INSERT INTO ENTRIES (orderId, reference, fullDate, costEntry)
VALUES
	(1, "923-123", NOW(), 0.00),
	(2, "ABC-ABC", NOW(), 0.00),
	(3, "ENT-444", NOW(), 0.00),
	(4, "ENT-456", NOW(), 0.00),
	(5, "AAA-AA5", NOW(), 0.00),
	(6, "ENT-AA6", NOW(), 0.00),
	(7, "888-008", NOW(), 0.00),
	(8, "123-008", NOW(), 0.00),
	(9, "133-999", NOW(), 0.00),
	(10, "999-QWE", NOW(), 0.00); -- Se genera varias recepciones.
	
INSERT INTO ENTRY_DETAIL (entryId, productId, quantity, unitCost, totalCost)
VALUES
	(1, 1, 10, 12.95, 129.50),
	(1, 2, 5, 16.80, 84.00),
	(2, 3, 15, 20.93, 313.95),
	(2, 4, 20, 19.25, 385.00),
	(3, 5, 8, 45.50, 364.00),
	(3, 6, 12, 22.75, 273.00),
	(4, 7, 6, 33.60, 201.60),
	(4, 8, 25, 24.50, 612.50),
	(5, 9, 15, 90.30, 1354.50),
	(5, 10, 4, 419.30, 1677.20),
	(6, 11, 2, 3149.30, 6298.60),
	(6, 12, 50, 69.30, 3465.00),
	(7, 13, 10, 315.00, 3150.00),
	(7, 14, 3, 979.30, 2937.90),
	(8, 15, 40, 17.50, 700.00),
	(8, 16, 30, 29.40, 882.00),
	(9, 17, 12, 129.50, 1554.00),
	(9, 18, 18, 84.00, 1512.00),
	(10, 19, 7, 209.30, 1465.10),
	(10, 20, 9, 174.30, 1568.70); -- Se añaden productos recibidos, también es necesario primero utilizar las consultas secundarias de pedido y catálogo de proveedores.
	
UPDATE ENTRIES
SET ENTRIES.costEntry = (
	SELECT SUM(ENTRY_DETAIL.totalCost)
	FROM ENTRY_DETAIL
	WHERE ENTRY_DETAIL.entryId = ENTRIES.id
); -- Se actualiza los costos de productos recibidos.

-- Actualización de mercancías.
UPDATE PRODUCTS
JOIN ENTRY_DETAIL
ON PRODUCTS.id = ENTRY_DETAIL.productId
SET PRODUCTS.stock = PRODUCTS.stock + ENTRY_DETAIL.quantity 
WHERE ENTRY_DETAIL.entryId IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10); -- Se actualiza el stock usando los números de recepción.

-- Se ejecuta varias ventas.
INSERT INTO SALES (fullDate, customerId, amount)
VALUES
	(NOW(), 1, 0.00),
	(NOW(), 1, 0.00),
	(NOW(), 1, 0.00),
	(NOW(), 8, 0.00),
	(NOW(), 1, 0.00),
	(NOW(), 1, 0.00),
	(NOW(), 1, 0.00),
	(NOW(), 2, 0.00),
	(NOW(), 5, 0.00),
	(NOW(), 1, 0.00); -- Se genera los tickets.

-- Se genera el detalle de venta.
INSERT INTO SALE_DETAIL (ticket, productId, quantity, unitPrice, totalSale)
VALUES
	(1, 1, 3, 18.50, 55.50),
	(1, 2, 2, 24.00, 48.00),
	(1, 3, 1, 29.90, 29.90),
	(2, 4, 4, 27.50, 110.00),
	(2, 6, 2, 32.50, 65.00),
	(2, 8, 1, 35.00, 35.00),
	(3, 1, 1, 18.50, 18.50),
	(3, 2, 1, 24.00, 24.00),
	(3, 7, 2, 48.00, 96.00),
	(4, 5, 1, 65.00, 65.00),
	(4, 12, 3, 99.00, 297.00),
	(5, 3, 2, 29.90, 59.80),
	(5, 15, 6, 25.00, 150.00),
	(5, 16, 2, 42.00, 84.00),
	(6, 2, 3, 24.00, 72.00),
	(6, 11, 1, 4499.00, 4499.00),
	(6, 13, 1, 450.00, 450.00),
	(7, 1, 4, 18.50, 74.00),
	(7, 4, 2, 27.50, 55.00),
	(7, 8, 3, 35.00, 105.00),
	(7, 18, 1, 120.00, 120.00),
	(8, 6, 2, 32.50, 65.00),
	(8, 9, 1, 129.00, 129.00),
	(8, 17, 2, 185.00, 370.00),
	(9, 7, 2, 48.00, 96.00),
	(9, 14, 1, 1399.00, 1399.00),
	(10, 15, 4, 25.00, 100.00),
	(10, 19, 1, 299.00, 299.00),
	(10, 20, 1, 249.00, 249.00); -- Se genera los detalles de las ventas.
	
UPDATE SALES
SET SALES.amount = (
	SELECT SUM(SALE_DETAIL.totalSale)
	FROM SALE_DETAIL
	WHERE SALE_DETAIL.ticket = SALES.id
); -- Se actualiza el monto de venta.

-- Actualización del stock.
UPDATE PRODUCTS
JOIN SALE_DETAIL
ON PRODUCTS.id = SALE_DETAIL.productId
SET PRODUCTS.stock = PRODUCTS.stock - SALE_DETAIL.quantity 
WHERE SALE_DETAIL.ticket IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10); -- Se actualiza el stock usando los tickets.