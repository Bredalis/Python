
# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from keras.datasets import boston_housing
from sklearn.linear_model import Ridge, LinearRegression

# Lectura de datos

(X_Train, Y_Train), (X_Test, Y_Test) = boston_housing.load_data()

print("Cantidad X de entrenamiento", X_Train.shape)
print("Cantidad Y de entrenamiento", Y_Train.shape)
print("Datos X de prueba", X_Test)
print("Datos Y de prueba", Y_Test)

# Modelo

CLF = LinearRegression()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

Y_Pred = CLF.predict(X_Test)

print("Prediccion", Y_Pred)

# Datos de prueba

DF_Y_Test = pd.DataFrame(Y_Test, columns = ['Y_Test'])
DF_Y_Pred = pd.DataFrame(Y_Pred, columns = ['Y_Pred'])

print(pd.concat([DF_Y_Test, DF_Y_Pred], axis = 1))

# Modo Grafica

plt.plot(X_Test)
plt.plot(Y_Pred)

plt.xlabel("N_Casa")
plt.ylabel("Precio")
plt.title("Regresion Ridge")
plt.legend(["Y_Test", "Predicciones"])
plt.grid()

plt.show()