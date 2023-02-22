
import time as tm

def Age():

	Year  = int(input("Write your year : "))
	Operation = Year - int(tm.strftime('%Y'))
	
	print(f"You're {Operation} years old")

def Months():

	Month = int(input("Write your month : "))
	Operation = Month - int(tm.strftime('%m'))

	print(f"Have {Operation} months")

def Days():

	Date  = int(input("Write your date : "))
	Operation = Date - int(tm.strftime('%j'))

	print(f"Have {Operation} days of life")