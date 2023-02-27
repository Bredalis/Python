
import matplotlib.pyplot as plt
import numpy as np

Fig, Grafica = plt.subplots(figsize = (6, 6))

Eje_X = np.arange(6)
Eje_Y = np.arange(6)

Grafica.plot(

	Eje_X, Eje_Y, marker = 'D',
	markerfacecolor = '#ffff00', markeredgecolor = 'k',
	fillstyle = 'left', markersize = 20,
	markerfacecoloralt = 'green'
)

plt.show()