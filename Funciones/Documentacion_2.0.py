
import math
import doctest

doctest.testmod()

def Raiz_Cuadrada(Numero):

	"""

	Raiz

	>>> lista=[]
	>>> for elemento in [4, 9, 16]:
	...     lista.append(elemento)
	>>> Raiz_Cuadrada(lista)
	[2.0, 3.0, 4.0]

	"""

	return [math.sqrt(Elemento) for Elemento in Numero]

print(Raiz_Cuadrada([4, 9, 16]))