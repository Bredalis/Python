
# Librerias

import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

Wine = load_wine()

print("Datos", Wine.data)
print("Etiquetas", Wine.target)
print("Cantidad de datos", Wine.data.shape)
print("Cantidad de etiquetas", Wine.target.shape)

print("Caracteristicas", Wine.feature_names)

print("Nombres de etiquetas", Wine.target_names)

Clases_Cantidad = len(np.unique(Wine.target_names))

print("Cantidad de clases de etiquetas", Clases_Cantidad)

# Lectura de datos

X_Train, Y_Train, X_Test, Y_Test = train_test_split(Wine.data, Wine.target)

print("X entrenamiento", X_Train)
print("Y entrenamiento", Y_Train)
print("Cantidad de X entrenamiento", X_Train.shape)
print("Cantidad de Y entrenamiento", Y_Train.shape)

print("X prueba", X_Test)
print("Y prueba", Y_Test)
print("Cantidad de X prueba", X_Test.shape)
print("Cantidad de Y prueba", Y_Test.shape)

# Modelo

CLF = KNeighborsClassifier()