
# Librerias

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Dataset

Iris = load_iris()

print(Iris)

print("Cantidad de datos", Iris.data.shape)
print("Datos", Iris.data)

print("Cantidad de etiquetas", Iris.target.shape)
print("Etiquetas", Iris.target)

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Iris.data, Iris.target, test_size = 0.3, shuffle = True) # Revolver

print("Cantidad X de entrenamiento", X_Train.shape)
print("Cantidad X de prueba", X_Test.shape)

print("Cantidad Y de entrenamiento", Y_Train.shape)
print("Cantidad Y de prueba", Y_Test.shape)

print("Datos X de entrenamiento", X_Train)
print("Datos X de prueba", X_Test)

print("Datos Y de entrenamiento", Y_Train)
print("Datos Y de prueba", Y_Test)