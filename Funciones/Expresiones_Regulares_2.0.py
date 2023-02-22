import re

class Expresiones_Regulares():

	def __init__(self):

		self.nombre  = "Sandra López"
		self.numeros = "78990"
		self.cadena = nombre + str(numeros)

		# Metodos para buscar

	def Nombre(self):

		if re.match(".a", self.nombre, re.IGNORECASE):

			print(self.nombre)

		else:

			print("No hemos encontrado el nombre")

	def Numeros(self):

		if re.match("\d", self.numeros):

			print("Hemos encontrado el numero")

		else:

			print("No lo hemos encontrado")

		if re.search("7", self.numeros, re.IGNORECASE):

			print("Hemos encontrado el numero")

		else:

			print("No hemos encontrado el numero")

objeto_clase = Expresiones_Regulares()
objeto_clase.Buscar_Nombre()
objeto_clase.Buscar_Numeros()