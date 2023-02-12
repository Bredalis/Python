
import matplotlib.pyplot as plt
import numpy as np

Eje_X = np.linspace(0.1, 6)
Eje_Y = np.sin(Eje_X)

def Estilo_Puntos():

	plt.plot(Eje_X, Eje_Y, linewidth = 3, linestyle = '-')

def Estilo_Stem():

	plt.stem(Eje_X, Eje_Y, linefmt = ('g', ':'), markerfmt = 'D', basefmt = 'C3--')

def Estilo_Set():

	fig, Grafico = plt.subplots()

	Grafico.stem(Eje_X, Eje_Y, linefmt = ('p', ':'), markerfmt = 'D', basefmt = 'C3--')

	Grafico.spines['left'].set_color('blue')
	Grafico.spines['left'].set_linewidth(3)
	Grafico.spines['left'].set_alpha(0.8)
	Grafico.spines['left'].set_linestyle('dashed')
	Grafico.spines['left'].set_visible(True)

	Grafico.grid(True, linewidth = 2)

plt.show()