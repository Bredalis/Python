
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, precision_score,
  recall_score, f1_score, classification_report)
     
# Datasets con numeros de muestra

X, Y = make_moons(n_samples = (150, 50))

# Modo Grafica

plt.scatter(X[:,0], X[:,1], c = Y)
plt.grid()

plt.show()
     
# Datos de entrenamiento

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y)
     
# Modelo

CLF = MLPClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

CLF.score(X_Test, Y_Test) # Rendimiento   

Y_Pred = CLF.predict(X_Test)

print(Y_Pred)
     
Accuracy = accuracy_score(Y_Test, Y_Pred)

print(Accuracy)
     
Matriz_Confusion = confusion_matrix(Y_Test, Y_Pred)

print(Matriz_Confusion)
     
Precision = precision_score(Y_Test, Y_Pred)

print(Precision)
     
Recall = recall_score(Y_Test, Y_Pred)

print(Recall)
     
F1 = f1_score(Y_Test, Y_Pred)

print(F1)

Report = classification_report(Y_Test, Y_Pred)

print(Report)