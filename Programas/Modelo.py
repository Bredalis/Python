
# Librerias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 

Datos = pd.read_excel("C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Python\\Scikit-Learn\\Datos_Regresion_Lineal.xlsx")

X = Datos[["Reduccion de Solidos"]]
Y = Datos[["Reduccion de la demanda de oxigeno"]]

# Modelo

CLF = LinearRegression()

# Lectura de datos 

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, shuffle = True, test_size = 16)

# Entrenamiento

CLF.fit(X_Train, Y_Train)

# Modo Grafica

plt.scatter(Y_Train, X_Train)
plt.plot(X_Train, CLF.predict(X_Train))

plt.title("Regresion Lineal Simple")
plt.xlabel("Reduccion de Solidos")
plt.ylabel("Reduccion de la demanda de oxigenos")
plt.legend(["Y", "Predicciones"])
plt.grid()

plt.show()