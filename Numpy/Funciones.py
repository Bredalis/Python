
import numpy as np

Matriz = np.arange(15).reshape(3, 5)

def Funciones():

	# Cantidades Filas y Columnas

	print(Matriz.shape)

	# Dimension

	print(Matriz.ndim)

	# Cantidad de la Matriz

	print(Matriz.size)

def Tipos_Matrices():

	Ceros = np.zeros((3, 4))

	Unos = np.ones((3, 4))

	Matriz_1D = np.arange(10)

	Rapida = np.linspace(99, 88, 25)

	Matriz_3D = np.arange(27).reshape(3, 3, 3)

	return(

		f'''Matriz de unos: {Unos}
			Matriz de Ceros: {Ceros} \n 
			Matriz 1D: {Matriz_1D} \n
			Matriz Rapida: {Rapida} \n
			Matriz 3D: {Matriz_3D}'''
		)