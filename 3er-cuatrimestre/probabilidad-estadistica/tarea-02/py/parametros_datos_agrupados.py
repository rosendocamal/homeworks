def amplitud_clase(numeros: dict[tuple[int, int], int]) -> float:
    """Calcula la amplitud de clases."""
    clases = list(numeros.keys())
    return clases[1][0] - clases[0][0]

def marca_clase(lim_inferior: int, lim_superior: int) -> float:
    """Calcula la marca de clase."""
    return (lim_inferior + lim_superior) / 2

def media_agrupada(numeros: dict[tuple[int, int], int]) -> float:
    """Calcula la media agrupada."""
    n: int = sum(numeros.values())
    numerador: float = 0
    for clase, frecuencia in numeros.items():
        lim_i: int = clase[0]
        lim_s: int = clase[1]
        numerador += frecuencia * marca_clase(lim_superior=lim_s,
                                              lim_inferior=lim_i)
    return numerador / n

def mediana_agrupada(numeros: dict[tuple[int, int], int]):
    """Calcula la mediana agrupada."""
    n: int = sum(numeros.values())
    clase_mediana: tuple[int, int] = (0, 0)
    frecuencia_acumulada_anterior: int = 0

    for clase, frecuencia in numeros.items():
        frecuencia_acumulada_anterior += frecuencia
        if frecuencia_acumulada_anterior >= (n/2):
            clase_mediana = clase
            frecuencia_acumulada_anterior -= frecuencia
            break

    lim_inferior_clase_mediana = clase_mediana[0]
    amplitud_clase_mediana = amplitud_clase(numeros)
    frecuencia_clase_mediana = numeros[clase_mediana]
    
    return lim_inferior_clase_mediana + (
        ((n/2) - frecuencia_acumulada_anterior) / frecuencia_clase_mediana
        ) *  amplitud_clase_mediana

def moda_agrupada(numeros: dict[tuple[int, int], int]) -> float:
    """Calcula la moda agrupada."""
    clases: list[tuple[int, int]] = list(numeros.keys())
    frecuencia_mayor: int = max(numeros.values())
    clase_modal: tuple[int, int] = clases[0]
    for clase, frecuencia in numeros.items():
        if frecuencia == frecuencia_mayor:
            clase_modal = clase
            break

    indice_clase_modal: int = clases.index(clase_modal)
    lim_inferior_clase_modal = clase_modal[0]
    amplitud_clase_modal = amplitud_clase(numeros)
    frecuencia_clase_modal = numeros[clase_modal]

    frecuencia_anterior: int = 0
    frecuencia_siguiente: int = 0

    if indice_clase_modal > 0:
        frecuencia_anterior = numeros[clases[indice_clase_modal - 1]]
    if indice_clase_modal < len(clases) - 1:
        frecuencia_siguiente = numeros[clases[indice_clase_modal + 1]]

    delta_1: int = frecuencia_clase_modal - frecuencia_anterior
    delta_2: int = frecuencia_clase_modal - frecuencia_siguiente

    return lim_inferior_clase_modal + (
        delta_1 / (delta_1 + delta_2)
    ) * amplitud_clase_modal

if __name__ == "__main__":
    # Datos
    edades: dict[tuple[int, int], int] = {
        (10, 19): 5,
        (20, 29): 8,
        (30, 39): 12,
        (40, 49): 10,
        (50, 59): 5
    }
    
    # Asignacion de valores
    valor_media_agrupada: float = media_agrupada(edades)
    valor_mediana_agrupada: float = mediana_agrupada(edades)
    valor_moda_agrupada: float = moda_agrupada(edades)
    
    # Resultado
    print(f"\nMedia agrupada: {round(valor_media_agrupada, 2)}\n" +
          f"Mediana agrupada: {round(valor_mediana_agrupada, 2)}\n" +
           f"Moda agrupada: {round(valor_moda_agrupada, 2)}\n")