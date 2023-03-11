
import numpy as np

Matriz_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def Funciones_Estadisticas():

	print("Mayor elemento de filas", np.amax(Matriz_2D, 0))
	print("Mayor elemento de columnas", np.amin(Matriz_2D, 1))

	print("Rango de columnas", np.ptp(Matriz_2D, axis = 1))
	print("Rango de filas", np.ptp(Matriz_2D, axis = 0))

def Formulas():

	print("Percectil de filas", np.percentile(Matriz_2D, 50, axis = 0))
	print(np.median(Matriz_2D))
	
	print("Media Aritmetica", np.mean(Matriz_2D))
	print("Promedio Ponderado", np.average(Matriz_2D))
	print("Desviacion Estandar", np.std(Matriz_2D))

print(Matriz_2D)
print(Funciones_Estadisticas(), Formulas())