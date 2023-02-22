
import numpy as np

matriz_1 = np.arange(24).reshape(4, 6)
matriz_2 = np.array([[2, 3, 4, 5, 6, 7]])

def Elaboraciones():

	# Posicion de elementos

	print(matriz_1[3, 4])

	print(np.concatenate((matriz_1, matriz_2)))

	print(np.array(matriz_2 >= 4))

def Metodos():

	matriz_1d = np.array([90, 7, 9, 4, 2, 1])
	
	print(np.power(matriz_1d, 2))
	print(np.sort(matriz_1d))

	print(matriz_2.max(), np.array(matriz_2.min()))

def Operaciones_Basicas():

	lista = [

	np.add(matriz_1, matriz_2), 
	np.subtract(matriz_1, matriz_2), 
	np.multiply(matriz_1, matriz_2), 
	np.divide(matriz_1, matriz_2),

	]

	return lista