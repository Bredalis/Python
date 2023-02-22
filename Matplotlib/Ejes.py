
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Limits_Scales():

	eje_x = np.linspace(0, 20, 200)
	eje_y = eje_x ** 3

	fig, grafico = plt.subplots()

	grafico.plot(eje_x, eje_y)
	grafico.set_yscale('log')
	grafico.set_ylim(0, 100000)

def Ticks():

	eje_x = np.linspace(0, 4*np.pi, 200)
	eje_y = np.cos(eje_x)

	fig, grafico = plt.subplots()

	grafico.plot(eje_x, eje_y)
	grafico.set_xticks(np.arange(0, 20, 4), ["Python", "JS", "CSS", "HTML", "Git"])

def Data_Frame():

	datos = {"Campo": ["Ingles", "Matematica", "Historia", "Lengua", "Fisica", "Biologia"], "Nivel": [6, 5, 4, 7, 5, 6]}

	df_datos = pd.DataFrame(datos)

	fig, grafico = plt.subplots(figsize = (10, 5))

	grafico.bar(df_datos.Campo, df_datos.Nivel)
	grafico.grid(axis = 'y')

	grafico.set_yticks(range(0, 11, 2))
	grafico.set_yticks(range(0, 11, 1), minor = True)

	grafico.set(ylim = (0, 10))
	
	grafico.yaxis.set_major_locator(MultipleLocator(1))
	grafico.yaxis.set_minor_locator(MultipleLocator(0.5))
	grafico.yaxis.set_minor_formatter('{x:.1f} puntos')

	grafico.tick_params(axis = 'y', which = 'major', labelsize = 14)
	grafico.tick_params(axis = 'y', which = 'minor', labelsize = 12)

	grafico.tick_params(axis = 'x', which = 'major', labelsize = 14, labelrotation = 15)

plt.show()