
import matplotlib.pyplot as plt
import numpy as np

Eje_X = np.arange(12)
Eje_X2 = np.arange(13)

Eje_Y = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]
Eje_Y2 = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034, 24890]

# Tipos de estilos

print(plt.style.available)

plt.style.use('seaborn')

plt.plot(Eje_X, Eje_Y, label = 'Linea Negra', color = 'k', linestyle = 'dotted', marker = 'p')
plt.plot(Eje_X2, Eje_Y2, label = 'Linea Azul', color = 'b', linestyle = 'dotted', marker = 'o')

plt.xticks(Eje_X)

plt.tick_params(axis = 'both', width = 'both', top = 1, right = 1)

plt.title('Tema')
plt.xlabel('Etiqueta X')
plt.ylabel('Etiqueta Y')
plt.legend()

plt.show()