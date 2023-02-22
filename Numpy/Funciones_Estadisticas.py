
import numpy as np

matriz_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def Funciones_Estadisticas():

	# Mayor elemento de filas

	print(np.amax(matriz_2d, 0))

	# Menor elemento de columnas

	print(np.amin(matriz_2d, 1))

	# Rango de columnas

	print(np.ptp(matriz_2d, axis = 1))

	# Rango de filas

	print(np.ptp(matriz_2d, axis = 0))

def Formulas():

	# Percectil de filas

	print(np.percentile(matriz_2d, 50, axis = 0))

	print(np.median(matriz_2d))

	# Media Aritmetica

	print(np.mean(matriz_2d))

	# Promedio Ponderado

	print(np.average(matriz_1d))

	# Desviacion Estandar

	print(np.std(matriz_1d))