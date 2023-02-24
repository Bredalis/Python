
import tkinter as tk
import math  

Ventana = tk.Tk()
Ventana.geometry('450x448') 
Ventana.title("CALCULATOR")
Ventana.resizable(0,0)

Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\Calculadora.ico')

def Clean():
	Mi_Entry.delete(0, tk.END)

def Reclick(Valor):
	
	Anterior = Mi_Entry.get()

	Mi_Entry.delete(0, tk.END)
	Mi_Entry.insert(0, str(Anterior + str(Valor)))

def Binario():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = int(Numero_1)

	Operacion = 'B'

def Suma():

    global Numero_1
    global Operacion

    Numero_1 = Mi_Entry.get()
    Numero_1 = float(Numero_1)

    Mi_Entry.delete(0, tk.END)

    Operacion = '+'

def Resta():

	global Numero_1 
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '-'

def Multiplicacion():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '*'

def Division():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '/'

def Potencia():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '^'
	
def Resultado():

	global Numero_2
	
	Numero_2 = Mi_Entry.get()
	Numero_2 = float(Numero_2)

	Mi_Entry.delete(0, tk.END)

	if Operacion == '+' :

		Mi_Entry.insert(0, Numero_1 + Numero_2)

	if Operacion == '-' :

		Mi_Entry.insert(0, Numero_1 - Numero_2)

	if Operacion == '*' :

		Mi_Entry.insert(0, Numero_1 * Numero_2)

	if Operacion == '^' :
		
		Mi_Entry.insert(0, Numero_1 ** Numero_2)

	if Operacion == 'B':

		Mi_Entry.insert(0, bin(Numero_1)[2:])

	if Operacion == '/':

		try:

			Mi_Entry.insert(0, Numero_1 / Numero_2)

		except ZeroDivisionError:

			Mi_Entry.insert(0, "Error")

Texto = tk.IntVar().set("")
Numero_1 = ""
Numero_2 = ""
Operacion = ""

Mi_Entry = tk.Entry(Ventana, textvariable = Texto, width = 50, justify = 'right')
Mi_Entry.grid(column = 0, row = 0, columnspan = 5)

tk.Button(Ventana, text = '1', bg = '#E0E0E0', cursor = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(1)).grid(column = 1, row = 1)
tk.Button(Ventana, text = '2', bg = '#E0E0E0', cursor = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(2)).grid(column = 2, row = 1)
tk.Button(Ventana, text = '3', bg = '#E0E0E0', cursor = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(3)).grid(column = 3, row = 1)

tk.Button(Ventana, text = '4', bg = '#E0E0E0', cursor = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(4)).grid(column = 1, row = 2)
tk.Button(Ventana, text = '5', bg = '#66BB6A', cursor = 'hand2', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(5)).grid(column = 2, row = 2)
tk.Button(Ventana, text = '6', bg = '#66BB6A', cursor = 'hand2', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(6)).grid(column = 3, row = 2)

tk.Button(Ventana, text = '7', bg = '#E0E0E0', cursor = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(7)).grid(column = 1, row = 3)
tk.Button(Ventana, text = '8', bg = '#66BB6A', cursor = 'hand2', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(8)).grid(column = 2, row = 3)
tk.Button(Ventana, text = '9', bg = '#66BB6A', cursor = 'hand2', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(9)).grid(column = 3, row = 3)

tk.Button(Ventana, text = '0', bg = '#E0E0E0', cursor  = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(0)).grid (column = 1, row = 4)
tk.Button(Ventana, text = '+', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = Suma).grid(column = 4, row = 1)
tk.Button(Ventana, text = 'x', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81',command = Multiplicacion).grid(column = 4, row = 2)

tk.Button(Ventana, text = '÷', bg = '#66BB6A', cursor = 'hand2', width = 15, height = 5, activebackground = '#F48FB1', command = Division).grid(column = 3, row = 4)
tk.Button(Ventana, text = '-', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = Resta).grid(column = 4, row = 3)
tk.Button(Ventana, text = 'π', bg = '#66BB6A', cursor  = 'hand2', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(math.pi)).grid(column = 2, row = 4)
tk.Button(Ventana, text = '=', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = Resultado).grid(column = 4, row = 4)

tk.Button(Ventana, text = 'B', bg = '#E0E0E0', cursor = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = Binario).grid(column = 1, row = 5)
tk.Button(Ventana, text = '.', bg = '#E0E0E0', cursor  = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick('.')).grid(column = 2, row = 5)
tk.Button(Ventana, text = '⌦', bg = '#E0E0E0', cursor  = 'hand2', width = 15, height = 5, activebackground = '#AB47BC', command = Clean).grid(column = 3, row = 5)
tk.Button(Ventana, text = '^', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = Potencia).grid(column = 4, row = 5)

Ventana.mainloop()