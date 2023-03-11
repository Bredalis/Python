
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(12)
X2 = np.arange(13)

Y = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]
Y2 = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034, 24890]

# Tipos de estilos

print(plt.style.available)

plt.style.use('seaborn')

# Lineas

plt.plot(X, Y, label = 'Linea Negra', color = 'k', linestyle = 'dotted', marker = 'p')
plt.plot(X2, Y2, label = 'Linea Azul', color = 'b', linestyle = 'dotted', marker = 'o')

plt.xticks(X)

plt.tick_params(axis = 'both', width = 'both', top = 1, right = 1)

plt.title('Tema')
plt.xlabel('Etiqueta X')
plt.ylabel('Etiqueta Y')
plt.legend()

plt.show()