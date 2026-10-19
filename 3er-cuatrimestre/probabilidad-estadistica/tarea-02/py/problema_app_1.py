from math import sqrt

import frecuencias as fs
import tecnicas_agrupacion as ta

# Datos
ventas_del_dia: list[int] = [12, 15, 18, 20, 21, 19, 22, 25, 18, 17, 19, 20, 21, 23, 24, 18, 19, 20, 22, 24, 25, 26, 27, 28, 18, 19, 20, 21, 22, 23]
num_datos = len(ventas_del_dia)

# Distribucion de frecuencias
frecuencias_absolutas = fs.frecuencia_absoluta(ventas_del_dia)
frecuencias_acumuladas = fs.frecuencia_acumulada(ventas_del_dia)
frecuencias_relativas = fs.frecuencia_relativa(ventas_del_dia)
frecuencias_relativas_acumuladas = fs.frecuencia_relativa_acumulada(ventas_del_dia)

# Agrupacion en intervalos
rango: float = ta.rango(ventas_del_dia)
numero_clases: int = round(sqrt(num_datos))
amplitud: float = rango / numero_clases
clases_y_frecuencias: dict[str, int] = ta.frecuencia(ventas_del_dia)

# Resultado - Distribucion de frecuencias
print("\n" + "="*81 + "\n|" +
    "Numero".center(15) + "|" +
    "F. abs.". center(15) + "|" +
    "F. abs. acum.".center(15) + "|" +
    "F. rel.".center(15) + "|" +
    "F. rel. acum.".center(15) + "|" +
    "\n" + "="*81)
for dato in sorted(set(ventas_del_dia)):
    a, b, c, d = frecuencias_absolutas[dato], frecuencias_acumuladas[dato], frecuencias_relativas[dato], frecuencias_relativas_acumuladas[dato]
    print("|" + f"{dato}".center(15) + "|" +
    f"{a}". center(15) + "|" +
    f"{b}".center(15) + "|" +
    f"{round(c, 2)}".center(15) + "|" +
    f"{round(d, 2)}".center(15) + "|")
print("="*81 + "\n")

# Resultado - Agrupacion en intervalos
print(f"\nAmplitud de clase: {round(amplitud, 2)}")
print("="*33 + "\n|" +
      "Limites de clase".center(18) + "|" +
      "Frecuencia".center(12) + "|" +
      "\n" + "="*33)
for k, v in clases_y_frecuencias.items():
    print("|" + f"{k}".center(18) + "|" +
          f"{v}".center(12) + "|")
print("="*33 + "\n")