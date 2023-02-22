
# Color-Map y Color-Bar

import matplotlib.pyplot as plt
import numpy as np

matrix = np.arange(36).reshape(6, 6)

fig, grafico = plt.subplots()

imagen = grafico.imshow(

	matrix, cmap = plt.cm.winter, 
	interpolation = 'bilinear', extent = [1, 10, 1, 10]
)

def Diagrama_De_Puntos():

	matrix_distancia = np.linspace(0, 2, 20)

	grado = np.pi*matrix_distancia
	colores = grado

	fig, grafico = plt.subplots(subplot_kw = dict(projection = 'polar'))
	visualizacion = grafico.scatter(grado, matrix_distancia, c = colores, s = 100, cmap = 'hsv')

	plt.colorbar(mappable = visualizacion, location = 'left')

plt.show()