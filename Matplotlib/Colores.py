
import matplotlib.pyplot as plt
import numpy as np

Fig, Grafica = plt.subplots()

Colores = np.arange(36).reshape(6, 6)

def Diagrama_De_Puntos():

	Fig, Grafica = plt.subplots(subplot_kw = dict(projection = 'polar'))

	Distancia = np.linspace(0, 2, 20)

	Grado = np.pi*Distancia
	Colores = Grado

	Visualizacion = Grafica.scatter(Grado, Distancia, c = Colores, s = 100, cmap = 'hsv')

	plt.colorbar(mappable = Visualizacion, location = 'left')

Grafica.imshow(

	Colores, cmap = plt.cm.winter,
	interpolation = 'bilinear', extent = [1, 10, 1, 10]
)

print(Diagrama_De_Puntos())

plt.show()