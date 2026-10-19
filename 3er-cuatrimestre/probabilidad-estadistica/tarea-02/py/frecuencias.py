def frecuencia_absoluta(numeros: list[int]) -> dict[int, int]:
    """Determina las frecuencias absolutas."""
    numeros = numeros.copy()
    numeros.sort()
    conteo: dict[int, int] = {}
    for num in set(numeros):
        conteo[num] = numeros.count(num)
    return conteo

def frecuencia_acumulada(numeros: list[int]) -> dict[int, int]:
    """Determina la frecuencia acumulada."""
    conteo: dict[int, int] = frecuencia_absoluta(numeros)
    f_acumulada: int = 0
    for k, v in conteo.items():
        conteo[k] = v + f_acumulada
        f_acumulada += v
    return conteo

def frecuencia_relativa(numeros: list[int]) -> dict[int, float]:
    """Determina la frecuencia relativa."""
    frecuencia_total: int = len(numeros)
    frecuencias: dict[int, int] = frecuencia_absoluta(numeros)
    conteo: dict[int, float] = {}
    for k, v in frecuencias.items():
        conteo[k] = v / frecuencia_total
    return conteo

def frecuencia_relativa_acumulada(numeros: list[int]) -> dict[int, float]:
    """Determina la frecuencia relativa acumulada."""
    conteo: dict[int, float] = frecuencia_relativa(numeros)
    f_r_acumulada: float = 0
    for k, v in conteo.items():
        conteo[k] = v + f_r_acumulada
        f_r_acumulada += v
    return conteo

if __name__ == "__main__":
    # Variables principales
    datos: list[int] = [12, 15, 18, 20, 15, 17, 18, 16, 19, 20, 18, 17, 16, 15, 18]
    frecuencias_absolutas: dict[int, int] = {}
    frecuencias_acumuladas: dict[int, int] = {}
    frecuencias_relativas: dict[int, float] = {}
    frecuencias_relativas_acumuladas: dict[int, float] = {}

    # Frecuencia absoluta
    frecuencias_absolutas = frecuencia_absoluta(datos)

    # Frecuencia acumulada
    frecuencias_acumuladas = frecuencia_acumulada(datos)

    # Frecuencia relativa
    frecuencias_relativas = frecuencia_relativa(datos)

    # Frecuencia relativa acumulada
    frecuencias_relativas_acumuladas = frecuencia_relativa_acumulada(datos)

    # Resultado
    print("\n" + "="*81 + "\n|" +
        "Numero".center(15) + "|" +
        "F. abs.". center(15) + "|" +
        "F. abs. acum.".center(15) + "|" +
        "F. rel.".center(15) + "|" +
        "F. rel. acum.".center(15) + "|" +
        "\n" + "="*81)
    for dato in sorted(set(datos)):
        a, b, c, d = frecuencias_absolutas[dato], frecuencias_acumuladas[dato], frecuencias_relativas[dato], frecuencias_relativas_acumuladas[dato]
        print("|" + f"{dato}".center(15) + "|" +
        f"{a}". center(15) + "|" +
        f"{b}".center(15) + "|" +
        f"{round(c, 2)}".center(15) + "|" +
        f"{round(d, 2)}".center(15) + "|")
    print("="*81 + "\n")