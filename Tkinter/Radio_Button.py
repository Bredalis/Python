
import tkinter as tk

root = tk.Tk()
root.resizable(False,False)

Opcion = tk.IntVar()

def Eleccion():
	
	if Opcion.get() == 1:

		Genero.config(text = "Has elegido masculino")

	elif Opcion.get() == 2:

	    Genero.config(text = "Has elegido femenina")

	else:		

		Genero.config(text = "Has elegido otros")

tk.Label(root, text = "Genero :").pack()

Maculino = tk.Radiobutton(root, text = "Masculino", variable = Opcion, value = 1, command = lambda: Eleccion()).pack()
Femenino = tk.Radiobutton(root, text = "Femenino" , variable = Opcion, value = 2, command = lambda: Eleccion()).pack()
Otros = tk.Radiobutton(root, text = "Otras opciones", variable = Opcion, value = 3, command = lambda: Eleccion()).pack()

Genero = tk.Label(root)
Genero.pack()

root.mainloop()