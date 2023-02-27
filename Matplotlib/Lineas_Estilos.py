
import matplotlib.pyplot as plt
import numpy as np

Fig, Grafica = plt.subplots()

Eje_X = np.linspace(0.1, 6)
Eje_Y = np.sin(Eje_X)

# Stem

Grafica.stem(Eje_X, Eje_Y, linefmt = ('k', ':'), markerfmt = 'D', basefmt = 'C3--')

# Set

Grafica.spines['left'].set_color('blue')
Grafica.spines['right'].set_color('red')

Grafica.spines['left'].set_linewidth(1)
Grafica.spines['right'].set_linewidth(1)

Grafica.spines['left'].set_alpha(0.5)
Grafica.spines['right'].set_alpha(0.5)

Grafica.spines['left'].set_linestyle('dashed')
Grafica.spines['right'].set_linestyle('dashed')

Grafica.spines['left'].set_visible(1)
Grafica.spines['right'].set_visible(1)

Grafica.grid(1, linewidth = 1)

plt.show()