
import numpy as np

def Numeros_Aleatoreos():

	matriz_1 = np.random.randint(10, size = (3, 3))
	matriz_2 = np.random.choice([3, 5, 7, 8, 9, 4], size = (3, 3))

	matriz_decimal = np.random.rand(5)

	matriz_3 = np.random.choice([2, 4, 6], p = [0.5, 0.5, 0.0], size = (1))
	matriz_4 = np.random.choice([2, 4, 8, 10], p = [0.3, 0.1, 0.1, 0.5], size = (50))

	print(

		matriz_1, 
		matriz_2, 
		matriz_3, 
		matriz_decimal, 
		matriz_4
		
	)