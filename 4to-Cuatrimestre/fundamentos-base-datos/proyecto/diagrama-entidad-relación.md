```mermaid
---
title: Diagrama Entidad-Relación
---
erDiagram
	VENTAS }o--|| CLIENTES : "realizado a"
	VENTAS }|--o{ PRODUCTOS : "se despacha"
	PRODUCTOS }o--|| CATEGORÍAS : "clasificado como"
	PROVEEDORES }|--|{ PRODUCTOS : "oferta"
	PEDIDOS }o--|{ PRODUCTOS : "se pide"
	RECEPCIONES }o--|{ PRODUCTOS : "se recibe"
	PEDIDOS }o--|| PROVEEDORES : "solicita a"
	RECEPCIONES }o--|| PROVEEDORES : "le realiza a"
	RECEPCIONES ||--o| PEDIDOS : "ligado a"
```