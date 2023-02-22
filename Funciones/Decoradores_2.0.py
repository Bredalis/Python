
def Decorador(funcion_parametro):                                                           
	def Funcion_Interna(*args, **kwargs):
		
		print("vamos a realizar un calculo: ")

		funcion_parametro(*args, **kwargs)

		print("Hemos terminado el calculo")
		
	return Funcion_Interna

@Decorador
def Potencia(base, exponente):
	print(pow(base, exponente))

Potencia(base= 3, exponente= 56)