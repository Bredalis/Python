
def Uso_Arroba(Email):

	Arroba = Email.count('@')

	if (Arroba != 0 or Email.rfind('@') == (len(Email) + 1) or Email.find('@') == 0):

		return True

	else:
		
		return False

print(Uso_Arroba("@"))