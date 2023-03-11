
# Librerias

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, precision_score,
  recall_score, f1_score, classification_report)


Wine = load_wine()

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Wine.data, Wine.target)

# Modelo

CLF = MLPClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

CLF.score(X_Test, Y_Test) # Rendimiento

Y_Pred = CLF.predict(X_Test)

print("Prediccion", Y_Pred)
     
Accuracy = accuracy_score(Y_Test, Y_Pred)

print(Accuracy)
     
Matriz_Confusion = confusion_matrix(Y_Test, Y_Pred)

print("Matriz de confucion", Matriz_Confusion)
     
Precision = precision_score(Y_Test, Y_Pred, average = "macro")

print("Precision", Precision)
     
Recall = recall_score(Y_Test, Y_Pred, average = "macro")

print(Recall)
     
F1 = f1_score(Y_Test, Y_Pred, average = "macro")

print(F1)

Report = classification_report(Y_Test, Y_Pred)

print(Report)