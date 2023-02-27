
def Decorador(Funcion_Parametro):
	def Funcion_Interna():	

		print("Inicio")

		Funcion_Parametro()

		print("Final")
		
	return Funcion_Interna

@Decorador
def Suma():
	print(34 + 56)

def Resta():
	print(34 - 56)

Suma()
Resta()