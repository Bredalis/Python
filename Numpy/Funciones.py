
import numpy as np

matriz = np.arange(15).reshape(3, 5)

def Funciones():

	print(matriz.shape) # Cantidades Filas y Columnas
	print(matriz.ndim) # Dimension
	print(matriz.size) # Cantidad de la Matriz

def Tipos_Matrices():

	ceros = np.zeros((3, 4))	
	unos = np.ones((3, 4))

	matriz_1d = np.arange(10)
	matriz_3d = np.arange(27).reshape(3, 3, 3)
	
	rapida = np.linspace(99, 88, 25)

	return(

		f'''Matriz de unos: {unos}
			Matriz de Ceros: {ceros} \n 
			Matriz 1D: {matriz_1d} \n
			Matriz Rapida: {rapida} \n
			Matriz 3D: {matriz_3d}'''
		)