import re

class Regulares():

	def __init__(self):

		self.Nombre  = "Sandra López"
		self.Numeros = "78990"
		self.Cadena = "sandia 7kkhjijijijijiji"

	def Buscar_Nombre(self):

		if re.match(".a", self.Nombre, re.IGNORECASE):

			print(self.Nombre)

		else:

			print("No hemos encontrado el nombre")

	def Buscar_Numeros(self):

		if re.match("\d", self.Numeros):

			print("Hemos encontrado el numero")

		else:

			print("No lo hemos encontrado")

		if re.search("7", self.Numeros, re.IGNORECASE):

			print("Hemos encontrado el numero")

		else:

			print("No hemos encontrado el numero")

Objeto_Clase = Regulares()
Objeto_Clase.Buscar_Nombre()
Objeto_Clase.Buscar_Numeros()