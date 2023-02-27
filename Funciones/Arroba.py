
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

print(Arroba_Identificacion("@"))