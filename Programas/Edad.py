
import time as tm

def Age():

	Year  = int(input("Write your year : "))
	Operation = int(tm.strftime('%Y')) - Year
	
	print(f"You're {Operation} years old")

print(Age())