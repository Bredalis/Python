
import time as tm

def Age():

	Year  = int(input("Write your year : "))
	Operaction = Year - int(tm.strftime('%Y'))
	
	print(f"Have {Operaction} year old")

def Months():

	Month = int(input("Write your month : "))
	Operaction = Month - int(tm.strftime('%m'))

	print(f"Have {Operaction} months")

def Days():

	Date  = int(input("Write your date : "))
	Operaction = Date - int(tm.strftime('%d'))

	print(f"Have {Operaction} days of life")