
import numpy as np

Matriz_1D = np.array([1, 1, 0])

def Conversion_Vertical():

	Matriz = np.array([[-3], [5], [-2]])

	return np.transpose(Matriz)

def Sistema_De_Ecuaciones():

	Matriz_1 = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
	Matriz_2 = np.array([[2, 7, 3], [2, 8, 2], [1, 3, 1]])

	Ecuacion_Matrices = np.linalg.solve(Matriz_1, Matriz_2)

	print(Ecuacion_Matrices)

    # se utiliza para comprovar si dos matrices son iguales 
    # en cuanto a elementos dentro de una tolerancia

	return np.allclose(np.dot(Matriz_1, Ecuacion_Matrices), Matriz_2)

print(Matriz_1D)
print(Conversion_Vertical(), Sistema_De_Ecuaciones())