
import matplotlib.pyplot as plt
import numpy as np

Eje_X = np.linspace(0, 2, 100)

plt.figure(figsize = (5, 3), layout = 'constrained')

plt.plot(Eje_X, Eje_X, label = 'Linea Azul')
plt.plot(Eje_X, Eje_X ** 2, label = 'Linea Naranja')
plt.plot(Eje_X, Eje_X ** 3, label = 'Linea Verde')

plt.title('Tema')
plt.ylabel('Etiqueta Y')
plt.xlabel('Etiqueta X')
plt.legend()

plt.show()