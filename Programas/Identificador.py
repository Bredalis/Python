
# Programa de identificacion de Datos

def Valor(Dato):

	if type(Dato) == int:

		print("Entero")

	elif type(Dato) == str:

		print("Letras")

	elif type(Dato) == float:

		print("Decimal")

	else:

		print("No Identificado")

def Estructura_Datos(Dato):

	if type(Dato) == list:

		print("Lista")

	elif type(Dato) == tuple:

		print("Tupla")

	elif type(Dato) == dict:

		print("Diccionario")

	else:

		print("No Identificado")

def Numeros():

	Dato = int(input("Introduce el numero: "))

	if Dato % 2 == 0:

		print("Par")

	else:

		print("Impar")