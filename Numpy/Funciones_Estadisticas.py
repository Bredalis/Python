
import numpy as np

matriz_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def Funciones_Estadisticas():

	print(np.amax(matriz_2d, 0)) # Mayor elemento de filas	
	print(np.amin(matriz_2d, 1)) # Menor elemento de columnas

	print(np.ptp(matriz_2d, axis = 1)) # Rango de columnas
	print(np.ptp(matriz_2d, axis = 0)) # Rango de filas

def Formulas():

	print(np.percentile(matriz_2d, 50, axis = 0)) # Percectil de filas
	print(np.median(matriz_2d))
	
	print(np.mean(matriz_2d)) # Media Aritmetica
	print(np.average(matriz_1d)) # Promedio Ponderado
	print(np.std(matriz_1d)) # Desviacion Estandar