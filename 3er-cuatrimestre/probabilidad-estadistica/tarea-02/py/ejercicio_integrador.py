import frecuencias as fs
from histogramas import mostrar_histograma_terminal as histograma
from tendencia_central_dispersion import desviacion_estandar, media, mediana, moda

# Datos
tiempos: list[int] = [18, 20, 19, 22, 21, 23, 24, 20, 19, 21, 22, 23, 25, 24, 20]
tiempos.sort()

# Variables principales y asignacion de valores
valor_media: float = media(tiempos)
valor_mediana: int | float = mediana(tiempos)
valores_moda: dict[int, int] = moda(tiempos)
valor_desviacion_estandar: float = desviacion_estandar(tiempos)

frecuencias_absolutas = fs.frecuencia_absoluta(tiempos)
frecuencias_acumuladas = fs.frecuencia_acumulada(tiempos)
frecuencias_relativas = fs.frecuencia_relativa(tiempos)
frecuencias_relativas_acumuladas = fs.frecuencia_relativa_acumulada(tiempos)

# Resultados
print(f"\nDatos ordenados: {tiempos}")

print(f"Media: {valor_media}\n" +
    f"Mediana: {valor_mediana}\n" +
    f"Desviacion estandar: {valor_desviacion_estandar}\n" +
    f"Conteo para obtener moda: {valores_moda}")

print("="*81 + "\n|" +
    "Numero".center(15) + "|" +
    "F. abs.". center(15) + "|" +
    "F. abs. acum.".center(15) + "|" +
    "F. rel.".center(15) + "|" +
    "F. rel. acum.".center(15) + "|" +
    "\n" + "="*81)
for dato in sorted(set(tiempos)):
    a, b, c, d = frecuencias_absolutas[dato], frecuencias_acumuladas[dato], frecuencias_relativas[dato], frecuencias_relativas_acumuladas[dato]
    print("|" + f"{dato}".center(15) + "|" +
    f"{a}". center(15) + "|" +
    f"{b}".center(15) + "|" +
    f"{round(c, 2)}".center(15) + "|" +
    f"{round(d, 2)}".center(15) + "|")
print("="*81)

histograma(tiempos)