
import matplotlib.pyplot as plt

Fig, Grafica = plt.subplots()

# Lineas

Grafica.plot([1, 2, 3, 4], [1, 2, 4, 3], label = 'Linea Azul')
Grafica.plot([1, 2, 3, 4], [4, 5, 6, 4], label = 'Linea Naranja')

# Circulos

Grafica.scatter([1, 2, 3, 4], [1.5, 5, 4.5, 5.6], label = 'Puntos')

Grafica.text(

	x = 2.5, y = 2.5, s = 'Ubicacion de Texto',
	fontsize = 10, color = 'green',
	bbox = dict(

		facecolor = 'pink', edgecolor = '#003430',
		alpha = 0.8, boxstyle = 'larrow'
	)
)

# Crear cubos de mensajes

Grafica.annotate(

	'Nuevo Texto', (1.3, 2), xytext = (2, 1),
	arrowprops = dict(arrowstyle = 'simple', facecolor = 'yellow', edgecolor = 'k')
)

Grafica.legend(loc = 'upper center', shadow = 0, fontsize = 'x-large', facecolor = 'pink')

plt.show()