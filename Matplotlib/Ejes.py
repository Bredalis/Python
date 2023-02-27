
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
import pandas as pd

Fig, Grafica = plt.subplots()

Eje_X = np.linspace(0, 20, 200)
Eje_Y = Eje_X ** 3

Eje_X2 = np.linspace(0, 4*np.pi, 200)
Eje_Y2 = np.cos(Eje_X2)

def Data_Frame():

	Fig, Grafica = plt.subplots()

	Datos = {"Campos": ["Ingles", "Matematica", "Historia", "Lengua", "Fisica", "Biologia"], "Cantidades": [6, 5, 4, 7, 5, 6]}

	DF = pd.DataFrame(Datos)

	Grafica.bar(DF.Campos, DF.Cantidades)
	Grafica.grid(axis =  'y')

	Grafica.set_yticks(range(0, 11, 2))
	Grafica.set_yticks(range(0, 11, 1), minor = 1)

	Grafica.set(ylim = (0, 10))
	
	Grafica.yaxis.set_major_locator(MultipleLocator(1))
	Grafica.yaxis.set_minor_locator(MultipleLocator(0.5))
	Grafica.yaxis.set_minor_formatter('{x:.1f} puntos')

	Grafica.tick_params(axis = 'y', which = 'major', labelsize = 14)
	Grafica.tick_params(axis = 'x', which = 'minor', labelsize = 12)

	Grafica.tick_params(axis = 'x', which = 'major', labelsize = 14, labelrotation = 15)

# Limits Scales

Grafica.plot(Eje_X, Eje_Y) 
Grafica.set_yscale('log')
Grafica.set_ylim(0, 100000)

# Ticks

Grafica.set_xticks(np.arange(0, 20, 4), ['Android', 'SQL', 'Linux', 'Window', 'Mac'])

print(Data_Frame())

plt.show()