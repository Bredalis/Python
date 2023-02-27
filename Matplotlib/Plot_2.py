
import matplotlib.pyplot as plt
from matplotlib.pyplot import Polygon
import numpy as np

Fig, Grafica = plt.subplots()

def Fun(X):

	return (X-3)*(X-5)*(X-7)+85

A, B = 2, 9

Eje_X = np.linspace(0, 10)
Eje_Y = Fun(Eje_X)

IX = np.linspace(A, B)
IY = Fun(IX)

Vertices = [(A, B), * zip(IX, IY), (B, 0)]

Poly = Polygon(Vertices, facecolor = '0.9', edgecolor = '0.5')

Grafica.plot(Eje_X, Eje_Y, 'r', linewidth = 2)
Grafica.set_ylim(bottom = 20)

Grafica.add_patch(Poly)

Grafica.text(

	0.5*(A+B), 30, r'$\int_a^B f(X)\mathrm{d}X$', 
	horizontalalignment = 'center', 
	fontsize = 20
)

Fig.text(0.9, 0.5, '$X$')
Fig.text(0.1, 0.9, '$Y$')

Grafica.xaxis.set_ticks_position('bottom')
Grafica.set_xticks([A, B], ['$A$', '$B$'])

plt.show()