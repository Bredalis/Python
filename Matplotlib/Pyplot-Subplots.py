
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 2, 100)

# Forma de la grafica

plt.figure(figsize = (5, 3), layout = 'constrained')

# Circulos

plt.plot(X, X, label = 'Linea Azul')
plt.plot(X, X ** 2, label = 'Linea Naranja')
plt.plot(X, X ** 3, label = 'Linea Verde')

plt.title('Tema')
plt.ylabel('Etiqueta Y')
plt.xlabel('Etiqueta X')
plt.legend()

plt.show()