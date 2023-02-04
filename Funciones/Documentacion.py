import doctest

doctest.testmod()

def Triangulo(base, altura):

	""" 
    
	Calcula

	>>> Triangulo(3, 6)
	'El area es 9.0'


	"""

	return f"El area es {str((base*altura)/2)}"

def Identifica_Arroba(email):

	"""

	La Funcion

	>>> Arroba('bredalisgmail.com')
	False

	"""

	arroba = email.count('@')

	if (arroba != 0 or email.rfind('@') == (len(email) + 1) or email.find('@') == 0):

		return True

	else:
		
		return False

print(Triangulo(4, 7))

print(Identifica_Arroba("@"))