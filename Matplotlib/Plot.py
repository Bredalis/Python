
import matplotlib.pyplot as plt
import numpy as np

Fig, Grafica = plt.subplots()

Eje_X = np.linspace(0, 20, 10)
Eje_Y = Eje_X ** 2

Eje_X2 = np.linspace(21, 30, 10)
Eje_Y2 = Eje_X2 * 2

# Dos lineas

Grafica.plot(Eje_X, Eje_Y, 'rd-', Eje_X2, Eje_Y2, 'ko:')

np.arange(0, 450, 100)
np.arange(0, 450, 50)

# Lineas de fondo

Grafica.grid(axis = 'y', color = 'b', which = 'major', alpha = (0.5), linestyle = '--')
Grafica.grid(axis = 'x', color = 'b', which = 'major', alpha = (0.2), linestyle = '--')

# Tamano de los numeros

Grafica.tick_params(axis = 'y', which = 'major', labelsize = 10)

Grafica.legend(['Linea Roja', 'Linea Negra'])

plt.show()