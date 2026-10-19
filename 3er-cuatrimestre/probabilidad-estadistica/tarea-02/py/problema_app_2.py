import parametros_datos_agrupados as pda


def varianza_agrupada(datos: dict[tuple[int, int], int]) -> float:
    """Calcula la varianza agrupada."""
    n: int = sum(datos.values())
    x_bar: float = sum(
        (li + ls) / 2 * fi for (li, ls), fi in datos.items()
    ) / n
    suma: float = sum(
        fi * ((li + ls) / 2 - x_bar) ** 2 for (li, ls), fi in datos.items()
    )
    return round(suma / n, 2)

def desviacion_estandar_agrupada(datos: dict[tuple[int, int], int]) -> float:
    """Calcula la desviacion agrupada."""
    return round(varianza_agrupada(datos) ** 0.5, 2)

# Datos | Captura manual de datos
ventas_del_dia: dict[tuple[int, int], int] = {
    (12, 15): 1,
    (15, 18): 2,
    (18, 21): 12,
    (21, 24): 8,
    (24, 27): 5,
    (27, 30): 2
}

# Media, mediana y moda agrupadas
media: float = pda.media_agrupada(ventas_del_dia)
mediana: float = pda.mediana_agrupada(ventas_del_dia)
moda: float = pda.moda_agrupada(ventas_del_dia)

# Varianza y desviacion estandar agrupada
varianza: float = varianza_agrupada(ventas_del_dia)
desviacion_estandar: float = desviacion_estandar_agrupada(ventas_del_dia)

# Resultados
print(f"\nMedia agrupada: {round(media, 2)}\n" +
      f"Mediana agrupada: {round(mediana, 2)}\n" +
      f"Moda agrupada: {round(moda, 2)}\n" +
      f"Varianza (usando frecuencias absolutas): {round(varianza, 2)}\n" +
      f"Desviacion estandar (usando frecuencias absolutas): {round(desviacion_estandar, 2)}\n")