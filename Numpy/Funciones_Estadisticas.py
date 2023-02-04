
import numpy as np

Matriz_1D = np.array([1, 2, 3, 4, 5, 6])

Matriz_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def Funciones_Estadisticas():

	# Eleccion del elemento mayor de filas

	print(np.amax(Matriz_2D, 0))

	# Eleccion del elemento menor de columnas

	print(np.amin(Matriz_2D, 1))

	# Calcular el rango de columnas

	print(np.ptp(Matriz_2D, axis = 1))

	# Calcular el rango de filas

	print(np.ptp(Matriz_2D, axis = 0))

def Formulas():

	# Percectil de filas

	print(np.percentile(Matriz_2D, 50, axis = 0))

	print(np.median(Matriz_2D))

	# Media Aritmetica

	print(np.mean(Matriz_2D))

	# Promedio Ponderado

	print(np.average(Matriz_1D))

	# Desviacion Estandar

	print(np.std(Matriz_1D))