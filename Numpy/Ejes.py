
import numpy as np

def Suma():

	matriz_2d = np.array([[0, 1, 2], [4, 2, 3]])

	filas = np.sum(matriz_2d, axis = 0)	
	columnas = np.sum(matriz_2d, axis = 1)

	return f"Suma de filas {filas}, columnas {columnas}"