
import matplotlib.pyplot as plt
import numpy as np

Grafica_X = np.linspace(0.1, 6)
Grafica_Y = np.sin(Grafica_X)

def Estilo_Puntos():

	plt.plot(Grafica_X, Grafica_Y, linewidth = 3, linestyle = '-')
	plt.show()

def Estilo_Stem():

	plt.stem(Grafica_X, Grafica_Y, linefmt = ('g', ':'), markerfmt = 'D', basefmt = 'C3--')
	plt.show()

def Estilo_Set():

	fig, Grafico = plt.subplots()

	Grafico.stem(Grafica_X, Grafica_Y, linefmt = ('p', ':'), markerfmt = 'D', basefmt = 'C3--')

	Grafico.spines['left'].set_color('blue')
	Grafico.spines['left'].set_linewidth(3)
	Grafico.spines['left'].set_alpha(0.8)
	Grafico.spines['left'].set_linestyle('dashed')
	Grafico.spines['left'].set_visible(True)

	Grafico.grid(True, linewidth = 2)
	plt.show()