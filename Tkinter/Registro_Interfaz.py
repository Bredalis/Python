
import tkinter as tk

class Registro:

	def __init__(self):

		self.Lados = 'center'
		self.Colores = ['#795548', '#80DEEA']

	def Elaboracion_Frame(self):

		self.Mi_Frame = tk.Frame(raiz, width = 1200, height = 600, bg = self.Colores[1])
		self.Mi_Frame.pack()

	def Elaboracion_Entrys(self):

		self.Nombre = tk.Entry(self.Mi_Frame, justify = self.Lados, fg = self.Colores[0])
		self.Nombre.grid(row = 0, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Apellido = tk.Entry(self.Mi_Frame, justify = self.Lados, fg = self.Colores[0])
		self.Apellido.grid(row = 1, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Direccion = tk.Entry(self.Mi_Frame, justify = self.Lados, fg = self.Colores[0])
		self.Direccion.grid(row = 2, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Contraseña = tk.Entry(self.Mi_Frame, justify = self.Lados, show = '*')
		self.Contraseña.grid(row = 3, column = 1, sticky = 'e', padx = 10, pady = 10)

	def Elaboracion_Etiquetas(self):

		self.Nombre = tk.Label(self.Mi_Frame, text = "Nombre: ", bg = self.Colores[1])
		self.Nombre.grid(row = 0, column  = 0, sticky = 'e', padx = 10, pady = 10)

		self.Apellido = tk.Label(self.Mi_Frame, text = "Apellido:", bg = self.Colores[1])
		self.Apellido.grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Direccion = tk.Label(self.Mi_Frame, text = "Direccion de casa:", bg = self.Colores[1])
		self.Direccion.grid(row = 2, column  = 0, sticky = 'e', padx = 10, pady = 10)

		self.Contraseña = tk.Label(self.Mi_Frame, text = "Contraseña:", bg = self.Colores[1])
		self.Contraseña.grid(row = 3, column = 0, sticky = 'e', padx = 10, pady = 10)

if __name__ == "__main__":

	raiz = tk.Tk()
	raiz.title("Registro De Interfaz")
	raiz.resizable(0,0)
		
	Clase_Objeto = Registro()
	Clase_Objeto.Elaboracion_Frame()
	Clase_Objeto.Elaboracion_Entrys()
	Clase_Objeto.Elaboracion_Etiquetas()

	raiz.mainloop()	