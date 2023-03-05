
from Regresion_Lineal_Simple import X, Y
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

CLF = LinearRegression()

CLF.fit(X, Y)

print(CLF.coef_)
print(CLF.intercept_)

# Predicciones

print(CLF.predict([[7]]))

plt.plot(X, Y)
plt.plot(X, CLF.predict(X))

plt.title("Regresion Lineal Simple")
plt.xlabel("Reduccion de Solidos")
plt.ylabel("Reduccion de la demanda de oxigeno")
plt.legend(["Y", "Predicciones"])
plt.grid()

plt.show()