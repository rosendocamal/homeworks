def promedio(a: int, b: int) -> float:
    """Calcula el promedio de dos enteros."""
    return (a + b) / 2

def max(a: int, b: int) -> int:
    """Calcula el numero maximo entre dos enteros."""
    return int(promedio(a, b) + abs(a - b)/2)

def min(a: int, b: int) -> int:
    """Calcula el numero minimo entre dos enteros."""
    return int(promedio(a, b) - abs(a - b)/2)

def rango(a: int, b: int) -> int:
    """Calcula el rango a traves de un minimo y un maximo."""
    if a < b:
        return b - a
    return a - b

def orden_ascendente(numeros: list[int]) -> list[int]:
    """Orden de menor a mayor los numeros de una lista de enteros."""
    n: int = len(numeros)
    for i in range(n):
        for j in range(n - i - 1):
            if numeros[j + 1] < numeros[j]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    return numeros

import random

# Variables principales
ventas_diarias: list[int] = [15, 18, 12, 20, 16, 22, 17]
valor_maximo: int = random.choice(ventas_diarias)
valor_minimo: int = random.choice(ventas_diarias)
valor_rango: int | None = None
ventas_asc: list[int] | None = None

# Valor maximo y minimo
for venta in ventas_diarias:
    valor_maximo = max(valor_maximo, venta)
    valor_minimo = min(valor_minimo, venta)

# Rango
valor_rango = rango(valor_minimo, valor_maximo)

# Ordenacion ascendente
ventas_asc = orden_ascendente(ventas_diarias.copy())

# Resultados
print(f"\nVentas diarias: {ventas_diarias}\n" +
      f"Valor maximo: {valor_maximo}\n" +
      f"Valor minimo: {valor_minimo}\n" +
      f"Rango: {valor_rango}\n" +
      f"Valores ordenados: {ventas_asc}\n")