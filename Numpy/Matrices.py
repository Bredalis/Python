
import numpy as np

def Elaboracion_Lista():

	Lista_Impar = [1, 3, 5]
	Lista_Impar.append(7)

	return "Lista Impar", Lista_Impar

def Elaboracion_Matriz():

	Matriz_Par = np.array([2, 4, 6])
	
	return "Suma de elementos con 8", Matriz_Par + np.array(8)

print(Elaboracion_Lista(), Elaboracion_Matriz())