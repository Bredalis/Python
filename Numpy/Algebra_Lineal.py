
import numpy as np

matriz_1d = np.array([1, 1, 0])

def Combercion_Vertical():

	matriz = np.array([[-3], [5], [-2]])

	return np.transpose(matriz)

def Sistema_De_Ecuaciones():

	matriz_1 = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
	matriz_2 = np.array([[2, 7, 3], [2, 8, 2], [1, 3, 1]])

	ecuacion_matrices = np.linalg.solve(matriz_1, matriz_2)

	print(ecuacion_matrices)

    # se utiliza para comprovar si dos matrices son iguales en cuanto a elementos dentro de una tolerancia

	return np.allclose(np.dot(matriz_1, ecuacion_matrices), matriz_2)