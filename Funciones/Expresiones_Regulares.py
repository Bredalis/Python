
import re

class Regulares:

	def __init__(self):

		self.Cadena = "Vamos a aprender expresiones regulares con Python"
		self.Texto_Buscar = input("Escribe el texto que quieres buscar :")
		self.Texto_Encontrado = re.search(self.Texto_Buscar, self.Cadena)

	def Buscar(self):

		if re.search(self.Texto_Buscar, self.Cadena) is not None:

			print("He encontrado el texto")

		else:

			print("No he encontrado el texto")

	def Imprimicion(self):

		print(re.search("aprender", self.Cadena))

		print(self.Texto_Encontrado.start())
		print(self.Texto_Encontrado.end())
		print(self.Texto_Encontrado.span())

		print(len(re.findall(self.Texto_Buscar, self.Cadena)))

Objeto_Clase = Regulares()
Objeto_Clase.Buscar()
Objeto_Clase.Imprimicion()