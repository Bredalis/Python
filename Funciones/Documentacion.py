
import doctest

doctest.testmod()

def Area_Triangulo(base, altura):

	""" 
    
	Calcula

	>>> Triangulo(3, 6)
	'El area es 9.0'


	"""

	return f"El area es {str((base*altura)/2)}"

def Arroba_Identificacion(email):

	"""

	La Funcion

	>>> Arroba_Identificacion('bredalisgmail.com')
	False

	"""

	Arroba = email.count('@')

	if (Arroba != 0 or email.rfind('@') == (len(email) + 1) or email.find('@') == 0):

		return True

	else:
		
		return False

print(Area_Triangulo(4, 7))

print(Arroba_Identificacion("@"))