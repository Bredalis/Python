
# Librerias

import numpy as np
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Datasets

Wine = load_wine()

print(Wine.data.shape, Wine.target.shape)

print("Caracteristicas", Wine.feature_names)
print("Nombres de etiquetas", Wine.target_names)

Clases_Cantidad = len(np.unique(Wine.target))

print(f"Cantidad clases de etiquetas {Clases_Cantidad}")

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Wine.data, Wine.target)

# Modelo

CLF = KNeighborsClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

