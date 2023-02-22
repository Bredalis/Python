
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np

def Fun(x):

	return (x-3)*(x-5)*(x-7)+85

a, b = 2, 9

x = np.linspace(0, 10)
y = Fun(x)

fig, grafico = plt.subplots()

grafico.plot(x, y, 'r', linewidth = 2)
grafico.set_ylim(bottom = 20)

ix = np.linspace(a, b)
iy = Fun(ix)

vertices = [(a, b), *zip(ix, iy), (b, 0)]

Poly = Polygon(vertices, facecolor = '0.9', edgecolor = '0.5')

grafico.add_patch(Poly)

grafico.text(0.5*(a+b), 30, r'$\int_a^b f(x)\mathrm{d}x$', horizontalalignment = 'center', fontsize = 20)

fig.text(0.9, 0.5, '$x$')
fig.text(0.1, 0.9, '$y$')

grafico.xaxis.set_ticks_position('bottom')
grafico.set_xticks([a, b], ['$a$', '$b$'])

plt.show()