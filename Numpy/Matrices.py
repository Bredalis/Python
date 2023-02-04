
import numpy as np

def Elaboracion_Lista():

	Lista_Impares = [1, 3, 5]

	Lista_Impares.append(7)

	return Lista_Impares

def Elaboracion_Matriz():

	Matriz_Pares = np.array([2, 4, 6])
	
	return Matriz_Pares + np.array(8)

print(Elaboracion_Lista())