
import re
import math

class Algoritmos:

	def Manipular_Archivos(self, Archivo, Mensaje):

		self.Archivo = open(Archivo, 'w')

		self.Archivo.write(Mensaje)
		self.Archivo.close()

	def Leer_Archivo(self, Archivo):

		self.Archivo = open(Archivo, 'r')

		print(self.Archivo.read())

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

	def Orden_Inverso(self):

		self.Cosa = input("Cosa para invertir: ")

		print(self.Cosa[:: -1].capitalize())

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
			
			print("No encontramos la letra")

		else:

			print("La palabra esta aqui : ", self.Frase)

	def Raiz_Cuadrada(self):

		self.Numero = int(input("Numero para encontrarle la raiz cuadrada: "))

		print(math.sqrt(self.Numero))

	def Numero_Lineas(self):

		self.Numero = int(input("Numero de saltos de lineas: "))

		print("\n"*self.Numero)
				
Clase_Objeto = Algoritmos()