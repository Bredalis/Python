
# Librerias

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

Iris = load_iris()

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Iris.data, Iris.target)

# Modelo

CLF = LogisticRegression()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

print(CLF.score(X_Test, Y_Test)) # Rendimiento

Y_Pred = CLF.predict(X_Test)

print("Prediccion", Y_Pred)

Matriz_Confusion = confusion_matrix(Y_Test, Y_Pred)

print("Matriz de confucion", Matriz_Confusion)