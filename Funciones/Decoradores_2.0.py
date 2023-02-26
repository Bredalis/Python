
def Decorador(funcion_parametro):                                                           
	def Funcion_Interna(*args, **kwargs):
		
		print("vamos a realizar un calculo: ")

		funcion_parametro(*args, **kwargs)

		print("Hemos terminado el calculo")
		
	return Funcion_Interna

@Decorador
def Potencia(Base, Exponente):
	print(pow(Base, Exponente))

Potencia(Base = 3, Exponente = 56)