
# Color-Map y Color-Bar

import matplotlib.pyplot as plt
import numpy as np

Matriz = np.arange(36).reshape(6, 6)

fig, Grafico = plt.subplots()

Imagen = Grafico.imshow(

	Matriz, cmap = plt.cm.winter, 
	interpolation = 'bilinear', extent = [1, 10, 1, 10]
)

def Diagrama_De_Puntos():

	Matriz_Distancia = np.linspace(0, 2, 20)

	Grado = np.pi*Matriz_Distancia
	Colores = Grado

	fig, Grafico = plt.subplots(subplot_kw = dict(projection = 'polar'))
	Visualizacion = Grafico.scatter(Grado, Matriz_Distancia, c = Colores, s = 100, cmap = 'hsv')

	plt.colorbar(mappable = Visualizacion, location = 'left')

plt.show()