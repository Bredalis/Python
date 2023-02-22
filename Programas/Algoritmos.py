
import re
import math

class Algoritmos:	

	def Ordena_Listas(self, Lista):

		print(Lista.sort())

	def Ordena_Palabras(self, Palabras):

		print(Palabras[:: -1].capitalize())

	def Decorador(self, Separador):
		def Decorador_Interno():

			print("Inicio")

			Separador()

			print("¡Fin!")

		return Decorador_Interno

	def Expresiones_Regulares(self):

		print("Aqui podras buscar tus palabras o numeros\n")

		self.Frase = input("Escribe tu secuencia de palabras : ")
		self.Palabra_Buscar = input("Escribe la letra que quieres buscar : ")

		if re.match(self.Palabra_Buscar, self.Frase, re.IGNORECASE):
			
			print("La palabra esta aqui : ", self.Frase)

		else:

			print("No encontramos la letra")

	def Raiz_Cuadrada(self, Numero):

		print(math.sqrt(Numero))
				
Clase_Objeto = Algoritmos()