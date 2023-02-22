
def Decorador(funcion_parametro):
	def Funcion_Interna():	

		print("Vamos a realizar un calculo: ")

		funcion_parametro()

		print("Hemos terminado el calculo")
		
	return Funcion_Interna

@Decorador
def Suma():
	print(34 + 56)

def Resta():
	print(34 - 56)

Suma()
Resta()