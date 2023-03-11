
# Librerias

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix 

Iris = load_iris()

print("Cantidad de datos", Iris.data.shape)
print("Cantidad de etiquetas", Iris.target.shape)

print("Datos", Iris.data)
print("Etiquetas", Iris.target)

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Iris.data, Iris.target)

print("Cantidad de X entrenamiento", X_Train.shape)
print("Cantidad de Y entrenamiento", Y_Train.shape)
print("X prueba", X_Test)
print("Y prueba", Y_Test)

# Modelo

CLF = LogisticRegression()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

# Predicciones

Y_Pred = CLF.predict(X_Test)

print("Predicciones", Y_Pred)

Matriz_Confusion = confusion_matrix(Y_Pred, Y_Test)

print("Matriz de confucion", Matriz_Confusion)