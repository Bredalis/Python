
import numpy as np

Matriz_1 = np.arange(24).reshape(4, 6)
Matriz_2 = np.array([[2, 3, 4, 5, 6, 7]])

def Elaboraciones():

	# Posicion de elementos

	print(Matriz_1[3, 4])

	print(np.concatenate((Matriz_1, Matriz_2)))

	print(np.array(Matriz_2 >= 4))

def Metodos():

	Matriz_1D = np.array([90, 7, 9, 4, 2, 1])
	
	print(np.power(Matriz_1D, 2))
	print(np.sort(Matriz_1D))

	print(Matriz_2.max(), np.array(Matriz_2.min()))

def Operaciones_Basicas():

	Operaciones = [

	np.add(Matriz_1, Matriz_2), 
	np.subtract(Matriz_1, Matriz_2), 
	np.multiply(Matriz_1, Matriz_2), 
	np.divide(Matriz_1, Matriz_2),

	]

	return Operaciones

print(Matriz_1, Matriz_2)
print(Elaboraciones(), Metodos(), Operaciones_Basicas())