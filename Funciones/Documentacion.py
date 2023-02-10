
import doctest

doctest.testmod()

def Area_Triangulo(Base, Altura):

	""" 
    
	Calcula

	>>> Triangulo(3, 6)
	'El area es 9.0'


	"""

	return f"El area es {str((Base*Altura)/2)}"

def Arroba_Identificacion(Email):

	"""

	La Funcion

	>>> Arroba_Identificacion('bredalisgmail.com')
	False

	"""

	Arroba = Email.count('@')

	if (Arroba != 0 or Email.rfind('@') == (len(Email) + 1) or Email.find('@') == 0):

		return True

	else:
		
		return False

print(Area_Triangulo(4, 7))

print(Arroba_Identificacion("@"))