
import tkinter as tk

ventana = tk.Tk()
ventana.resizable(0,0)

opcion = tk.IntVar()

def Eleccion():
	
	if opcion.get() == 1:
		genero.config(text= "Has elegido masculino")

	elif opcion.get() == 2:
	    genero.config(text= "Has elegido femenina")

	else:
		genero.config(text= "Has elegido otros")

tk.Label(ventana, text= "Genero :").pack()

tk.Radiobutton(ventana, text= "Masculino", variable= opcion, value= 1, command= lambda: Eleccion()).pack()
tk.Radiobutton(ventana, text= "Femenino" , variable= opcion, value= 2, command= lambda: Eleccion()).pack()
tk.Radiobutton(ventana, text= "Otras opciones", variable= opcion, value= 3, command= lambda: Eleccion()).pack()

genero = tk.Label(ventana)
genero.pack()

ventana.mainloop()