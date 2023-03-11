
# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

Datos = pd.read_excel("Datos_Regresion_Lineal.xlsx")

X = Datos[["Reduccion de Solidos"]]
Y = Datos[["Reduccion de la demanda de oxigeno"]]

# Modelo

CLF = LinearRegression()

# Entrenamiento

CLF.fit(X, Y)

print(f"Valor de β0 y β1 {CLF.coef_}")
print(CLF.intercept_)

# Representacion Grafica

plt.scatter(X, Y)
plt.plot(X, CLF.predict(X))

plt.title("Regresion Lineal Simple")
plt.xlabel("Reduccion de Solidos")
plt.ylabel("Reduccion de la demanda de oxigeno")
plt.legend(["Y", "Predicciones"])
plt.grid()

plt.show()