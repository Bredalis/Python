
def Decorador(Funcion_Parametro):                                                           
	def Funcion_Interna(*args, **kwargs):
		
		print("Inicio \n")

		Funcion_Parametro(*args, **kwargs)

		print("\n Final")
		
	return Funcion_Interna

@Decorador
def Potencia(Base, Exponente):
	
	print(pow(Base, Exponente))

Potencia(Base = 3, Exponente = 56)