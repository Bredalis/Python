
import matplotlib.pyplot as plt
import numpy as np

# Tamaño de la grafica

Fig, Grafica = plt.subplots(figsize = (6, 6))

X = np.arange(6)
Y = np.arange(6)

# Lineas

Grafica.plot(

	X, Y, marker = 'D',
	markerfacecolor = '#ffff00', markeredgecolor = 'k',
	fillstyle = 'left', markersize = 20,
	markerfacecoloralt = 'green'
)

plt.show()