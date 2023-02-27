
import numpy as np

def Suma():

	Matriz_2D = np.array([[0, 1, 2], [4, 2, 3]])

	Filas = np.sum(Matriz_2D, axis = 0)	
	Columnas = np.sum(Matriz_2D, axis = 1)

	return f"Suma de Filas {Filas}, Columnas {Columnas}"

print(Suma())