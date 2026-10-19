def media(numeros: list[int]) -> float:
    """Calcula la media arimetica de una lista de numeros."""
    return sum(numeros) / len(numeros)

def mediana(numeros: list[int]) -> float | int:
    """Calcula la mediana, el valor central de una lista de numeros."""
    numeros = numeros.copy()
    numeros.sort()
    n: int = len(numeros)
    if n % 2 == 0:
        num_pre_centro: int = numeros[(n - 1) // 2]
        num_pos_centro: int = numeros[((n - 1) // 2) + 1]
        return media([num_pre_centro, num_pos_centro])
    return numeros[(n - 1) // 2]

def moda(numeros: list[int]) -> dict[int, int]:
    """Calcula las repeticiones de cada entero, el (o los) primero(s) del
    diccionario son la moda."""
    numeros = numeros.copy()
    numeros.sort()
    conteo: dict[int, int] = {}
    for num in set(numeros):
        conteo[num] = numeros.count(num)
    ordenar_por_valores_desc = dict(sorted(conteo.items(), key=lambda item: item[1], reverse=True))
    return ordenar_por_valores_desc

def rango(numeros: list[int]) -> float | int:
    """Obtiene el rango de una lista de numeros."""
    return max(numeros) - min(numeros)

def varianza(numeros: list[int]) -> float:
    """Calcula la varianza de una lista de numeros."""
    sigma: float = 0
    for num in numeros:
        sigma += (num - media(numeros)) ** 2
    return round(sigma / len(numeros), 2)

def desviacion_estandar(numeros: list[int]) -> float:
    """Calcula la desviacion estandar de una lista de numeros."""
    import math
    return round(math.sqrt(varianza(numeros)), 2)

if __name__ == "__main__":
    # Variables principales
    calificaciones_estudiantes: list[int] = [70, 75, 80, 85, 90, 85, 80, 95, 100, 80]
    valor_media: float | None = None
    valor_mediana: float | int | None = None
    valores_moda: dict[int, int] = {}
    valor_rango: float | int | None = None
    valor_varianza: float | None = None
    valor_desviacion_estandar: float | None = None

    # Media
    valor_media = media(calificaciones_estudiantes)

    # Mediana
    valor_mediana = mediana(calificaciones_estudiantes)

    # Moda
    valor_moda = moda(calificaciones_estudiantes)

    # Rango
    valor_rango = rango(calificaciones_estudiantes)

    # Varianza
    valor_varianza = varianza(calificaciones_estudiantes)

    # Desviacion estandar
    valor_desviacion_estandar = desviacion_estandar(calificaciones_estudiantes)

    # Resultados
    print(f"\nMedia: {valor_media}\n" +
        f"Mediana: {valor_mediana}\n" +
        f"Rango: {valor_rango}\n" +
        f"Varianza: {valor_varianza}\n" +
        f"Desviacion estandar: {valor_desviacion_estandar}\n" +
        f"Conteo para obtener moda: {valor_moda}\n")