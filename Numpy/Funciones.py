
import numpy as np

Matriz = np.arange(15).reshape(3, 5)

def Funciones():

	print("Cantidades de filas y columnas", Matriz.shape)
	print("Dimension", Matriz.ndim)
	print("Cantidad de la Matriz", Matriz.size)

def Tipos_Matrices():

	Ceros = np.zeros((3, 4))	
	Unos = np.ones((3, 4))

	Matriz_1D = np.arange(10)
	Matriz_3D = np.arange(27).reshape(3, 3, 3)
	
	Rapida = np.linspace(99, 88, 25)

	print(

		f'''Matriz de Unos: {Unos}
			Matriz de Ceros: {Ceros} \n 
			Matriz 1D: {Matriz_1D} \n
			Matriz Rapida: {Rapida} \n
			Matriz 3D: {Matriz_3D}'''
		)

print(Matriz)
print(Funciones(), Tipos_Matrices())
