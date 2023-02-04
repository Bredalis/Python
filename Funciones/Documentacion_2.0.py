import math
import doctest

doctest.testmod()

def Raiz_Cuadrada(numero):

	"""

	Raiz

	>>> lista=[]
	>>> for elemento in [4, 9, 16]:
	...     lista.append(elemento)
	>>> Raiz_Cuadrada(lista)
	[2.0, 3.0, 4.0]

	"""

	return [math.sqrt(elemento)for elemento in numero]

print(Raiz_Cuadrada([4, 9, 16]))