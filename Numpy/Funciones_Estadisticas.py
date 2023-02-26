
import numpy as np

Matriz_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def Funciones_Estadisticas():

	print(np.amax(Matriz_2D, 0)) # Mayor elemento de filas	
	print(np.amin(Matriz_2D, 1)) # Menor elemento de columnas

	print(np.ptp(Matriz_2D, axis = 1)) # Rango de columnas
	print(np.ptp(Matriz_2D, axis = 0)) # Rango de filas

def Formulas():

	print(np.percentile(Matriz_2D, 50, axis = 0)) # Percectil de filas
	print(np.median(Matriz_2D))
	
	print(np.mean(Matriz_2D)) # Media Aritmetica
	print(np.average(Matriz_1D)) # Promedio Ponderado
	print(np.std(Matriz_1D)) # Desviacion Estandar