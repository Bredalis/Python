Numeros = [17, 24, 7, 3, 8, 51, 92]

def Edades_Menores(Edades):

	return Edades <= 18

print(list(filter(Edades_Menores, Numeros)))