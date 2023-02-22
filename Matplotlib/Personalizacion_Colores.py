
import matplotlib.pyplot as plt

eje_x = [1, 2, 3, 4, 5, 6, 7, 8]
eje_y = [3, 1, 1, 2, 5, 5, 7, 6]
eje_y_2 = [2, 5, 5, 8, 9, 2, 0, 1]

def Puntos():

	fig, grafico = plt.subplots()

	grafico.scatter(eje_x, eje_y, s = 200, color = '#ff0345', edgecolor = ('k'))

def Lineas():

	fig, grafico = plt.subplots()

	grafico.plot(eje_x, eje_y, color = 'r', linewidth = 5, zorder = 1) 
	grafico.plot(eje_x, eje_y_2, color = 'k', linewidth = 5, zorder = 2)

def Diagrama_De_Barras():

	eje_x = ['A', 'B', 'C', 'D', 'E']
	eje_y = [14, 7, 18, 9, 10]

	fig, grafico = plt.subplots()
	
	grafico.bar(eje_x, eje_y, color = 'pink')

print(Puntos(), Lineas(), Diagrama_De_Barras())

plt.show()