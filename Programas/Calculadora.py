
import tkinter as tk
import math  

Ventana = tk.Tk()
Ventana.geometry('450x448')
Ventana.title("CALCULATOR")
Ventana.resizable(0,0)

Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\Calculadora.ico')

Texto = tk.IntVar()
Numero = ""
Numero_2 = ""
Operacion = ""

Mi_Entry = tk.Entry(Ventana, textvariable = Texto, width = 50, justify = 'right')
Mi_Entry.grid(column = 0, row = 0, columnspan = 5)

def Mensaje():
	
	Texto.set("Calculadora")

def Clean():

	Mi_Entry.delete(0, tk.END)

def Reclick(Valor):

	Texto.set("")
	
	Anterior = Mi_Entry.get()

	Mi_Entry.delete(0, tk.END)
	Mi_Entry.insert(0, str(Anterior + str(Valor)))

def Suma():

    global Numero
    global Operacion

    Numero = Mi_Entry.get()
    Numero = float(Numero)

    Mi_Entry.delete(0, tk.END)

    Operacion = '+'

def Resta():

	global Numero 
	global Operacion

	Numero = Mi_Entry.get()
	Numero = float(Numero)

	Mi_Entry.delete(0, tk.END)

	Operacion = '-'

def Multiplicacion():

	global Numero
	global Operacion

	Numero = Mi_Entry.get()
	Numero = float(Numero)

	Mi_Entry.delete(0, tk.END)

	Operacion = '*'

def Division():

	global Numero
	global Operacion

	Numero = Mi_Entry.get()
	Numero = float(Numero)

	Mi_Entry.delete(0, tk.END)

	Operacion = '/'

def Potencia():

	global Numero
	global Operacion

	Numero = Mi_Entry.get()
	Numero = float(Numero)

	Mi_Entry.delete(0, tk.END)

	Operacion = '^'
	
def Igual():

	global Numero_2
	
	Numero_2 = Mi_Entry.get()
	Numero_2 = float(Numero_2)

	Mi_Entry.delete(0, tk.END)

	if Operacion == '+' :

		Mi_Entry.insert(0, Numero + Numero_2)

	if Operacion == '-' :

		Mi_Entry.insert(0, Numero - Numero_2)

	if Operacion == '*' :

		Mi_Entry.insert(0, Numero * Numero_2)

	if Operacion == '^' :
		
		Mi_Entry.insert(0, Numero ** Numero_2)

	if Operacion == '/':

		try:

			Mi_Entry.insert(0, Numero / Numero_2)

		except ZeroDivisionError:

			Mi_Entry.insert(0, "Error")

tk.Button(Ventana, text = '1', bg = '#E0E0E0', cursor = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(1)).grid(column = 1, row = 1)
tk.Button(Ventana, text = '2', bg = '#E0E0E0', cursor = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(2)).grid(column = 2, row = 1)
tk.Button(Ventana, text = '3', bg = '#E0E0E0', cursor = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(3)).grid(column = 3, row = 1)

tk.Button(Ventana, text = '4', bg = '#E0E0E0', cursor = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(4)).grid(column = 1, row = 2)
tk.Button(Ventana, text = '5', bg = '#66BB6A', cursor = 'heart', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(5)).grid(column = 2, row = 2)
tk.Button(Ventana, text = '6', bg = '#66BB6A', cursor = 'heart', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(6)).grid(column = 3, row = 2)
tk.Button(Ventana, text = '7', bg = '#E0E0E0', cursor = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(7)).grid(column = 1, row = 3)
tk.Button(Ventana, text = '8', bg = '#66BB6A', cursor = 'heart', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(8)).grid(column = 2, row = 3)
tk.Button(Ventana, text = '9', bg = '#66BB6A', cursor = 'heart', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(9)).grid(column = 3, row = 3)

tk.Button(Ventana, text = '0', bg = '#E0E0E0', cursor  = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick(0)).grid (column = 1, row = 4)
tk.Button(Ventana, text = '+', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = lambda: Suma()).grid(column = 4, row = 1)
tk.Button(Ventana, text = 'x', bg = '#42A5F5', cursor = 'hand2', height = 5, activebackground = '#F4FF81', width = 15, command = lambda: Multiplicacion()).grid(column = 4, row = 2)

tk.Button(Ventana, text = '÷', bg = '#66BB6A', cursor = 'heart', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Division()).grid(column = 3, row = 4)
tk.Button(Ventana, text = '-', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = lambda: Resta()).grid(column = 4, row = 3)
tk.Button(Ventana, text = 'π', bg = '#66BB6A', cursor  = 'heart', width = 15, height = 5, activebackground = '#F48FB1', command = lambda: Reclick(math.pi)).grid(column = 2, row = 4)
tk.Button(Ventana, text = '=', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = lambda: Igual()).grid(column = 4, row = 4)

tk.Button(Ventana, text = 'M', width = 15, bg = '#E0E0E0', height = 5, activebackground = '#AB47BC', command = lambda: Mensaje(), cursor = 'pirate').grid(column = 1, row = 5)
tk.Button(Ventana, text = '.', bg = '#E0E0E0', cursor  = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Reclick('.')).grid(column = 2, row = 5)
tk.Button(Ventana, text = '⌦', bg = '#E0E0E0', cursor  = 'pirate', width = 15, height = 5, activebackground = '#AB47BC', command = lambda: Clean()).grid(column = 3, row = 5)
tk.Button(Ventana, text = '^', bg = '#42A5F5', cursor = 'hand2', width = 15, height = 5, activebackground = '#F4FF81', command = lambda: Potencia()).grid(column = 4, row = 5)

Ventana.mainloop()