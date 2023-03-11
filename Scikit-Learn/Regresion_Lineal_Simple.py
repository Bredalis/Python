
# Librerias

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Datos = pd.read_excel("Datos_Regresion_Lineal.xlsx")

X = Datos[["Reduccion de Solidos"]]
Y = Datos[["Reduccion de la demanda de oxigeno"]]

Matriz = Datos.to_numpy()

# Regresion Lineal

N = len(Matriz)

Sumatoria_X = np.sum(Matriz[:, 0])
Sumatoria_Y = np.sum(Matriz[:, 1])

Sumatoria_Producto = np.sum(Matriz[:, 0] * Matriz[:, 1])
Sumatoria_Cuadrado_X = np.sum(Matriz[:, 0] * Matriz[:, 0])

B1 = (N*Sumatoria_Producto - Sumatoria_X*Sumatoria_Y) / (N*Sumatoria_Cuadrado_X - Sumatoria_X * Sumatoria_X)
B0 = (Sumatoria_Y - B1*Sumatoria_X) / N

print("N :", N)
print("Sumatoria X :", Sumatoria_X)
print("Sumatoria Y :", Sumatoria_Y)
print("Sumatoria XY :", Sumatoria_Producto)
print("Sumatoria X^Y :", Sumatoria_Cuadrado_X)

print("B1 :", B1)
print("B2 :", B0)

# Modo Graficado

plt.scatter(X, Y)
plt.plot(X, X)

plt.title("Modelo De Regresion Lineal Simple")
plt.xlabel("Reduccion de Solidos")
plt.ylabel("Reduccion de la demanda de oxigeno")
plt.grid()

plt.show()