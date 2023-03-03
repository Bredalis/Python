
import re
import math

class Algoritmos:

	def Prefijos_Sufijos(self):

		# Nombres Patos

		self.Prefijos = "JKLMOPQ"
		
		self.Sufijo = "ack"
		self.Sufijo_2 = "uack"

		for Letra in self.Prefijos:

			if Letra < self.Prefijos[4] or Letra == self.Prefijos[5]:

				print(Letra + self.Sufijo)

			else: 

				print(Letra + self.Sufijo_2)	

	def Ordena_Listas(self, Lista):

		print(Lista.sort())

	def Orden_Inverso(self, Cosa):

		print(Cosa[:: -1].capitalize())

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

	def Numero_Lineas(Numero):

		Contador = 0

		while Contador < Numero:

			print("\n")

			Contador =+ 1
				
Clase_Objeto = Algoritmos()