import frecuencias as fs


def mostrar_histograma_terminal(datos: list[int]) -> None:
    """Muestra un histograma de frecuencias absolutas en la terminal."""
    frecuencias_absolutas = fs.frecuencia_absoluta(datos)
    if not frecuencias_absolutas:
        print("\nNo hay datos para mostrar en el histograma.")
        return
    max_frecuencia = max(frecuencias_absolutas.values())
    print("=" * 33 + "\n|" +
          "Frecuencias absolutas".center(31) + "|\n" +
          "=" * 33)
    for dato in sorted(set(datos)):
        longitud = int((frecuencias_absolutas[dato] / max_frecuencia) * 20)
        barra = "=" * longitud
        print(f"| {dato:>2} | {barra:<20} | {frecuencias_absolutas[dato]} |")
    print("=" * 33 + "\n")

if __name__ == "__main__":
    # Variables principales
    edades: list[int] = [18, 19, 20, 20, 21, 21, 22, 22, 22, 23, 24, 24, 25, 25, 26, 27, 28, 29]
    frecuencias_absolutas: dict[int, int] = {}
    frecuencias_acumuladas: dict[int, int] = {}
    frecuencias_relativas: dict[int, float] = {}
    frecuencias_relativas_acumuladas: dict[int, float] = {}

    # Frecuencia absoluta
    frecuencias_absolutas = fs.frecuencia_absoluta(edades)

    # Frecuencia acumulada
    frecuencias_acumuladas = fs.frecuencia_acumulada(edades)

    # Frecuencia relativa
    frecuencias_relativas = fs.frecuencia_relativa(edades)

    # Frecuencia relativa acumulada
    frecuencias_relativas_acumuladas = fs.frecuencia_relativa_acumulada(edades)

    # Resultado
    print("\n" + "="*81 + "\n|" +
          "Numero".center(15) + "|" +
          "F. abs.". center(15) + "|" +
          "F. abs. acum.".center(15) + "|" +
          "F. rel.".center(15) + "|" +
          "F. rel. acum.".center(15) + "|" +
          "\n" + "="*81)
    for dato in sorted(set(edades)):
        a, b, c, d = frecuencias_absolutas[dato], frecuencias_acumuladas[dato], frecuencias_relativas[dato], frecuencias_relativas_acumuladas[dato]
        print("|" + f"{dato}".center(15) + "|" +
          f"{a}". center(15) + "|" +
          f"{b}".center(15) + "|" +
          f"{round(c, 2)}".center(15) + "|" +
          f"{round(d, 2)}".center(15) + "|")
    print("="*81)

    # Histograma de frecuencias absolutas
    mostrar_histograma_terminal(edades)