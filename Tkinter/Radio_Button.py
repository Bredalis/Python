
import tkinter as tk

Ventana = tk.Tk()
Ventana.resizable(0,0)

Opcion = tk.IntVar()

def Eleccion():
	
	if Opcion.get() == 1:
		Genero.config(text = "Has elegido masculino")

	elif Opcion.get() == 2:
	    Genero.config(text = "Has elegido femenina")

	else:
		Genero.config(text = "Has elegido otros")

tk.Label(Ventana, text = "Genero :").pack()

tk.Radiobutton(Ventana, text = "Masculino", variable = Opcion, value = 1, command = lambda: Eleccion()).pack()
tk.Radiobutton(Ventana, text = "Femenino" , variable = Opcion, value = 2, command = lambda: Eleccion()).pack()
tk.Radiobutton(Ventana, text = "Otras opciones", variable = Opcion, value = 3, command = lambda: Eleccion()).pack()

Genero = tk.Label(Ventana)
Genero.pack()

Ventana.mainloop()