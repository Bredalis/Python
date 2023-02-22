
# Programa de identificacion de Datos

def Valor(*Datos):

	if type(Datos) == int:

		print("Entero")

	elif type(Datos) == str:

		print("Letras")

	elif type(Datos) == float:

		print("Decimal")

	else:

		print("No Identificado")

def Estructura_Datos(Datos):

	if type(Datos) == list:

		print("Lista")

	elif type(Datos) == tuple:

		print("Tupla")

	elif type(Datos) == dict:

		print("Diccionario")

	else:

		print("No Identificado")

def Numeros():

	Datos = int(input("Introduce el numero: "))

	if Datos % 2 == 0:

		print("Par")

	else:

		print("Impar")