
# Librerias

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_curve, roc_auc_score 

X, Y = make_moons(n_samples = 128)

# Modo Grafico

plt.scatter(X[:, 0], X[:, 1], c = Y)
plt.grid()

plt.show()

# Lectura de datos

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y)

# Modelo

CLF = MLPClassifier()

# Entrenamiento

CLF.fit(X_Train, Y_Train)

print(CLF.score(X_Test, Y_Test))

Probabilidades = CLF.predict_proba(X_Test)

print(Probabilidades)

#Auc = roc_auc_score(Y_Test, Probabilidades)

#print(Auc)

#FPR, TPR, Thresholds = roc_curve(Y_Test, Probabilidades) 

#plt.plot(FPR, TPR, marker = ".", label = "MLP")

plt.xlabel("False Positivo Rate")
plt.ylabel("True Positivo Rate")
plt.legend()

plt.show()