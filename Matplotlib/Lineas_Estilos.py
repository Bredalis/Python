
import matplotlib.pyplot as plt
import numpy as np

eje_x = np.linspace(0.1, 6)
eje_y = np.sin(eje_x)

def Estilo_Puntos():

	plt.plot(eje_x, eje_y, linewidth = 3, linestyle = '-')

def Estilo_Stem():

	plt.stem(eje_x, eje_y, linefmt = ('g', ':'), markerfmt = 'D', basefmt = 'C3--')

def Estilo_Set():

	fig, grafico = plt.subplots()

	grafico.stem(eje_x, eje_y, linefmt = ('p', ':'), markerfmt = 'D', basefmt = 'C3--')

	grafico.spines['left'].set_color('blue')
	grafico.spines['left'].set_linewidth(3)
	grafico.spines['left'].set_alpha(0.8)
	grafico.spines['left'].set_linestyle('dashed')
	grafico.spines['left'].set_visible(True)

	grafico.grid(True, linewidth = 2)

plt.show()