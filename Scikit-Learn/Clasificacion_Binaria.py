
# Librerias

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, precision_score,
  recall_score, f1_score, classification_report)
     
# Datasets con numeros de muestra

X, Y = make_moons(n_samples = (150, 50))

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y)
     
# Modelo

CLF = MLPClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

CLF.score(X_Test, Y_Test) # Rendimiento   

Y_Pred = CLF.predict(X_Test)

print("Prediccion", Y_Pred)
     
Exactitud = accuracy_score(Y_Test, Y_Pred)

print("Exactitud", Exactitud)
     
Matriz_Confusion = confusion_matrix(Y_Test, Y_Pred)

print("Matriz de confucion", Matriz_Confusion)
     
Precision = precision_score(Y_Test, Y_Pred)

print("Precision", Precision)
     
Recall = recall_score(Y_Test, Y_Pred)

print("Recordar", Recall)
     
F1 = f1_score(Y_Test, Y_Pred)

print(F1)

Report = classification_report(Y_Test, Y_Pred)

print("Informe", Report)

# Modo Grafica

plt.scatter(X[:,0], X[:,1], c = Y)
plt.grid()

plt.show()