
import tkinter as tk

class Registro():

	def __init__(self):

		self.Lados = 'center'
		self.Colores = ['#795548', '#80DEEA']

	def Etiquetas(self):

		self.Nombre = tk.Label(Ventana, text = "Nombre :", bg = self.Colores[1])
		self.Nombre.grid(row = 0, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Apellido = tk.Label(Ventana, text = "Apellido :", bg = self.Colores[1])
		self.Apellido.grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Direccion = tk.Label(Ventana, text = "Direccion :", bg = self.Colores[1])
		self.Direccion.grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Contraseña = tk.Label(Ventana, text = "Contraseña :", bg = self.Colores[1])
		self.Contraseña.grid(row = 3, column = 0, sticky = 'e', padx = 10, pady = 10)

	def Entrys(self):

		self.Nombre = tk.Entry(Ventana, justify = self.Lados, fg = self.Colores[0])
		self.Nombre.grid(row = 0, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Apellido = tk.Entry(Ventana, justify = self.Lados, fg = self.Colores[0])
		self.Apellido.grid(row = 1, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Direccion = tk.Entry(Ventana, justify = self.Lados, fg = self.Colores[0])
		self.Direccion.grid(row = 2, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Contraseña = tk.Entry(Ventana, justify = self.Lados, show = '*')
		self.Contraseña.grid(row = 3, column = 1, sticky = 'e', padx = 10, pady = 10)

if __name__ == "__main__":

	Ventana = tk.Tk()
	Ventana.title("Registro")
	Ventana.resizable(0,0)
	Ventana.config(bg = '#80DEEA')
		
	Clase_Objeto = Registro()
	Clase_Objeto.Etiquetas()
	Clase_Objeto.Entrys()

	Ventana.mainloop()	