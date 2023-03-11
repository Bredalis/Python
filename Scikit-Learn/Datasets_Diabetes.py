
# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error

Datos = load_diabetes()

print("Datos", Datos.data)
print("Etiquetas", Datos.target)

print("Caracteristicas", Datos.feature_names)

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Datos.data, Datos.target)

# Modelo

CLF = KNeighborsClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

# Prediociones

Y_Pred = CLF.predict(X_Test)

DF_Y_Pred = pd.DataFrame(Y_Pred, columns = ["Y_Pred"])
DF_Y_Test = pd.DataFrame(Y_Test, columns = ["Y_Test"])

print(pd.concat([DF_Y_Pred, DF_Y_Test], axis = 1))

print("Error Cuadratico Medio", mean_squared_error(Y_Test, Y_Pred))

# Modo Grafica

plt.plot(DF_Y_Pred)
plt.plot(DF_Y_Test)

plt.xlabel("X")
plt.ylabel("Y")
plt.legend(["Y_Pred", "Predicciones"])
plt.grid()

plt.show()