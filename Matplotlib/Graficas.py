
import matplotlib.pyplot as plt

Fig, Grafica = plt.subplots()

X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [3, 1, 1, 2, 5, 5, 7, 6]

def Diagrama_De_Barras():

	Fig, Grafica = plt.subplots()

	Letras = ['Alegrìa', 'Enojo', 'Tristesa', 'Miedo', 'Desagrado']
	Cantidad = [16, 5, 7, 10, 14]

	# Barras

	Grafica.bar(Letras, Cantidad, color = 'aqua')

	plt.title('Sustantivos Abstractos')

# Circulos

Grafica.scatter(X, Y, s = 200, color = '#ff0345', edgecolor = ('k'))

# Lineas

Grafica.plot(X, Y, color = 'b', linewidth = 5, zorder = 0)

print(Diagrama_De_Barras())

plt.show()