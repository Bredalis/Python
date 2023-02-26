
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Limits_Scales():

	Eje_X = np.linspace(0, 20, 200)
	Eje_Y = Eje_X ** 3

	fig, Grafica = plt.subplots()

	Grafica.plot(Eje_X, Eje_Y)
	Grafica.set_yscale('log')
	Grafica.set_ylim(0, 100000)

def Ticks():

	Eje_X = np.linspace(0, 4*np.pi, 200)
	Eje_Y = np.cos(Eje_X)

	fig, Grafica = plt.subplots()

	Grafica.plot(Eje_X, Eje_Y)
	Grafica.set_xticks(np.arange(0, 20, 4), ["Python", "JS", "CSS", "HTML", "Git"])

def Data_Frame():

	Datos = {"Campo": ["Ingles", "Matematica", "Historia", "Lengua", "Fisica", "Biologia"], "Nivel": [6, 5, 4, 7, 5, 6]}

	DF_Datos = pd.DataFrame(Datos)

	fig, Grafica = plt.subplots(figsize = (10, 5))

	Grafica.bar(DF_Datos.Campo, DF_Datos.Nivel)
	Grafica.grid(axis = 'y')

	Grafica.set_yticks(range(0, 11, 2))
	Grafica.set_yticks(range(0, 11, 1), minor = True)

	Grafica.set(ylim = (0, 10))
	
	Grafica.yaxis.set_major_locator(MultipleLocator(1))
	Grafica.yaxis.set_minor_locator(MultipleLocator(0.5))
	Grafica.yaxis.set_minor_formatter('{x:.1f} puntos')

	Grafica.tick_params(axis = 'y', which = 'major', labelsize = 14)
	Grafica.tick_params(axis = 'y', which = 'minor', labelsize = 12)

	Grafica.tick_params(axis = 'x', which = 'major', labelsize = 14, labelrotation = 15)

plt.show()