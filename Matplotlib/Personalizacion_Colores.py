
import matplotlib.pyplot as plt

Eje_X = [1, 2, 3, 4, 5, 6, 7, 8]
Eje_Y = [3, 1, 1, 2, 5, 5, 7, 6]
Eje_Y2 = [2, 5, 5, 8, 9, 2, 0, 1]

def Puntos():

	fig, Grafico = plt.subplots()

	Grafico.scatter(Eje_X, Eje_Y, s = 200, color = '#ff0345', edgecolor = ('k'))

def Lineas():

	fig, Grafico = plt.subplots()

	Grafico.plot(Eje_X, Eje_Y, color = 'r', linewidth = 5, zorder = 1) 
	Grafico.plot(Eje_X, Eje_Y2, color = 'k', linewidth = 5, zorder = 2)

def Diagrama_De_Barras():

	Eje_X = ['A', 'B', 'C', 'D', 'E']
	Eje_Y = [14, 7, 18, 9, 10]

	fig, Grafico = plt.subplots()
	Grafico.bar(Eje_X, Eje_Y, color = "pink")

plt.show()