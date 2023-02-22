
import re

class Expresiones_Regulares:

	def __init__(self):

		self.cadena = "Vamos a aprender expresiones regulares con Python"
		self.texto_buscar = input("Escribe el texto que quieres buscar :")
		self.texto_encontrado = re.search(self.texto_buscar, self.cadena)

	def Buscar(self):

		if re.search(self.texto_buscar, self.cadena) is not None:

			print("He encontrado el texto")

		else:

			print("No he encontrado el texto")

	def Imprimir(self):

		print(re.search("aprender", self.cadena))

		print(self.texto_encontrado.start())
		print(self.texto_encontrado.end())
		print(self.texto_encontrado.span())

		print(len(re.findall(self.texto_buscar, self.cadena)))

objeto_clase = Expresiones_Regulares()
objeto_clase.Buscar()
objeto_clase.Imprimir()