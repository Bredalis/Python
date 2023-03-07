
import re

class Expresiones_Regulares():

	def __init__(self):

		self.Cadena = "Hola, Esta es una cadena de caracteres"
		self.Texto_Buscar = input("Texto que quieres buscar : ")
		self.Texto_Encontrado = re.search(self.Texto_Buscar, self.Cadena)

	def Buscar(self):

		if re.search(self.Texto_Buscar, self.Cadena) is not None:

			print("Hemos encontrado el texto")

		else:

			print("No hemos encontrado el texto")

	def Imprimir(self):

		print(re.search('cadena', self.Cadena))
  
		print(len(re.findall(self.Texto_Buscar, self.Cadena)))

Clase_Objeto = Expresiones_Regulares()
Clase_Objeto.Buscar()
Clase_Objeto.Imprimir()