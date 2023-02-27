
def Decorador(funcion_parametro):
	def Funcion_Interna():	

		print("Vamos a realizar un calculo: ")

		funcion_parametro()

		print("Hemos terminado el calculo")
		
	return Funcion_Interna

@Decorador
def Suma(N1, N2):	
	return N1 + N2

def Resta(N1, N2):
	return N1 + N2

Suma(1, 1)
Resta(2, 2)