
# Librerias

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Datos = pd.read_excel("Datos_Regresion_Lineal.xlsx")

X = Datos[["Reduccion de Solidos"]]
Y = Datos[["Reduccion de la demanda de oxigeno"]]

Matriz = Datos.to_numpy()

print(Matriz)

# Formula de Regresion Lineal

N = len(Matriz)

Sumatoria_X = np.sum(Matriz[:, 0])
Sumatoria_Y = np.sum(Matriz[:, 1])

Sumatoria_Producto = np.sum(Matriz[:, 0] * np.sum(Matriz[:, 1]))
Sumatoria_Cuadrado_X = np.sum(Matriz[:, 0] * Matriz[:, 0])

print('n :', N)
print('Sumatoria X :', Sumatoria_X)
print('Sumatoria Y :', Sumatoria_Y)
print('Sumatoria XY :', Sumatoria_Producto)
print('Sumatoria X^2 :', Sumatoria_Cuadrado_X)

B1 = (N*Sumatoria_Producto - Sumatoria_X*Sumatoria_Y) / (N*Sumatoria_Cuadrado_X - Sumatoria_X*Sumatoria_X)
B0 = (Sumatoria_Y - B1*Sumatoria_X) / N

print("B1 :", B1)
print("B0 :", B0)

# Graficar Datos

plt.scatter(X, Y)

plt.xlabel("Reduccion de Solidos")
plt.ylabel("Reduccion de la demanda de oxigeno")
plt.grid()

plt.show()