def rango(numeros: list[int]) -> float:
    """Obtiene el rango de una lista de enteros."""
    return max(numeros) - min(numeros)

def amplitud(numeros: list[int]) -> float:
    """Calcula la amplitud de una lista de enteros."""
    num_clases: int = 5
    return rango(numeros) / num_clases

def intervalos(numeros: list[int]) -> list[tuple[int, int]]:
    """Calcula los intervalos o limites de clase."""
    n_min: int = min(numeros)
    n_max: int = max(numeros)
    n_amplitud: int = int(amplitud(numeros))
    limites: list[tuple[int, int]] = []
    for i in range(n_min, n_max, n_amplitud):
        limites.append((i, i + n_amplitud))
        # print(f"[{i}-{i + n_amplitud}{(']' if i + n_amplitud == n_max else ')')}")
    return limites

def frecuencia(numeros: list[int]) -> dict[str, int]:
    """Calcula la frecuencia mediante limites de clase dada una lista de enteros."""
    limites_clase: list[tuple] = intervalos(numeros)
    conteo: dict[str, int] = {}
    for i in enumerate(limites_clase):
        lim_inferior, lim_superior = i[1][0], i[1][1]
        if i[0] + 1 == len(limites_clase):
            key: str = f"[{lim_inferior}-{lim_superior}]"
            conteo[key] = 0
            for num in numeros:
                if lim_inferior <= num <= lim_superior:
                    conteo[key] += 1
        else:
            key: str = f"[{lim_inferior}-{lim_superior})"
            conteo[key] = 0
            for num in numeros:
                if lim_inferior <= num < lim_superior:
                    conteo[key] += 1
    return conteo

if __name__ == "__main__":
    # Variables principales
    estaturas: list[int] = [155, 158, 160, 162, 164, 165, 166, 167, 168, 170, 171, 172, 173, 174, 175, 176, 178, 180, 182, 185]
    amplitud_clase: float
    frecuencia_clase: dict[str, int]
    
    # Amplitud de clase
    amplitud_clase = amplitud(estaturas)
    
    # Limites y frecuencia de clases
    frecuencia_clase = frecuencia(estaturas)
    
    # Resultado
    print(f"\nAmplitud de clase: {amplitud_clase}")
    print("="*33 + "\n|" +
          "Limites de clase".center(18) + "|" +
          "Frecuencia".center(12) + "|" +
          "\n" + "="*33)
    for k, v in frecuencia_clase.items():
        print(f"{k}".center(19) + "|" +
              f"{v}".center(12) + "|")
    print("="*33 + "\n")