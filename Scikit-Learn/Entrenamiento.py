
# Librerias 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

Iris = load_iris()

print("Datasets", Iris)

print("Datos", Iris.data)
print("Etiquetas", Iris.target)

print("Cantidad de datos", Iris.data.shape)
print("Cantidad de etiquetas", Iris.target.shape)

# Lectura de datos

X_Train, Y_Train, X_Test, Y_Test = train_test_split(Iris.data, Iris.target)

print("X entrenamiento", X_Train)
print("Y entrenamiento", Y_Train)
print("Cantidad de X entrenamiento", X_Train.shape)
print("Cantidad de Y entrenamiento", Y_Train.shape)

print("X prueba", X_Test)
print("Y prueba", Y_Test)

print("Cantidad de X prueba", X_Test.shape)
print("Cantidad de Y prueba", Y_Test.shape)