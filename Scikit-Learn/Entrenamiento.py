
# Librerias

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Dataset

Iris = load_iris()

print(Iris)

# Datos

print(Iris.data.shape)
print(Iris.data)

# Etiquetas

print(Iris.target.shape)
print(Iris.target)

# Datos y etiquetas de entrenamiento y prueba

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Iris.data, Iris.target, test_size = 0.3, shuffle = True) # Revolver

print(X_Train.shape)
print(X_Test.shape)

print(Y_Train.shape)
print(Y_Test.shape)

print(X_Train)
print(X_Test)

print(Y_Train)
print(Y_Test)