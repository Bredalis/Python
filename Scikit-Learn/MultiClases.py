
# Librerias

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, precision_score,
  recall_score, f1_score, classification_report)

Wine = load_wine()

print("Datos", Wine.data)
print("Etiquetas", Wine.target)

print("Cantidad de datos", Wine.data.shape)
print("Cantidad de etiquetas", Wine.target.shape)

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Wine.data, Wine.target)

print("Datos de X entrenamiento", X_Train)
print("Etiquetas de Y entrenamiento", Y_Train)
print("Cantidad de X entrenamiento", X_Train.shape)
print("Cantidad de Y entrenamiento", Y_Train.shape)

print("Datos de X prueba", X_Test)
print("Etiquetas de Y prueba", Y_Test)
print("Cantidad de X prueba", X_Test.shape)
print("Cantidad de Y prueba", Y_Test.shape)

# Modelo

CLF = MLPClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

# Predicciones

Y_Pred = CLF.predict(X_Test)

print("Predicciones", Y_Pred)

Matriz_Confusion = confusion_matrix(Y_Test, Y_Pred)

print("Matriz de confucion", Matriz_Confusion)

Exactitud = accuracy_score(Y_Test, Y_Pred)

print("Exactitud", Exactitud)

print("Rendimiento", CLF.score(X_Test, Y_Test))

Precision = precision_score(Y_Test, Y_Pred, average = "macro")

print("Precision", Precision)
     
Recall = recall_score(Y_Test, Y_Pred, average = "macro")

print("Recordar", Recall)
     
F1 = f1_score(Y_Test, Y_Pred, average = "macro")

print(F1)

Report = classification_report(Y_Test, Y_Pred)

print("Informe", Report)