
# Librerias

import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

X, Y = make_classification(n_samples = 200)

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y)

# Modelo

CLF = KNeighborsClassifier()

# Entrenamiento

CLF.fit(X, Y)

# Predicciones

Y_Pred = CLF.predict(X_Test)

print("Predicciones", Y_Pred)

print("Rendimiento", CLF.score(X_Test, Y_Test))

Matriz_Confusion = confusion_matrix(Y_Pred, Y_Test)

print("Matriz Confusion", Matriz_Confusion)

# Modo Grafica

plt.scatter(X_Train[:, 0], X_Train[:, 1], c = Y_Train)
plt.scatter(X_Test[1, 1], X_Test[1, 1], s = 100)
plt.grid()

plt.show()