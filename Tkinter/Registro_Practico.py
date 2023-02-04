
import tkinter as tk

class Registro:

	def __init__(self):			

		self.Valor_Nombre = tk.StringVar()
		self.Valor_Apellido = tk.StringVar()
		self.Valor_Direccion  = tk.StringVar()
		self.Valor_Contraseña = tk.StringVar()

		self.Resultado = ""

	def Elaboracion_Frame(self):

		self.Mi_Frame = tk.Frame(Raiz, width = 1200, height = 600)
		self.Mi_Frame.pack()

	def Elaboracion_Entrys(self):

		self.Nombre = tk.Entry(self.Mi_Frame, textvariable = self.Valor_Nombre, width = 30, justify = "center", fg = "#6D4C41")
		self.Nombre.grid(row = 0, column = 1, sticky = "e", padx = 10, pady = 10)

		self.Apellido = tk.Entry(self.Mi_Frame, textvariable = self.Valor_Apellido, justify = "center", fg = "#6D4C41")
		self.Apellido.grid(row = 1, column = 1, sticky = "e", padx = 10, pady = 10)

		self.Direccion = tk.Entry(self.Mi_Frame, textvariable = self.Valor_Direccion, justify = "center", fg = "#6D4C41")
		self.Direccion.grid(row = 2, column = 1, sticky = "e", padx = 10, pady = 10)

		self.Contraseña = tk.Entry(self.Mi_Frame, textvariable = self.Valor_Contraseña, justify = "center", fg = "#6D4C41", show = "*")
		self.Contraseña.grid(row = 3, column = 1, sticky = "e", padx = 10, pady = 10)

	def Elaboracion_Etiquetas(self):

		self.Nombre = tk.Label(self.Mi_Frame, text = "Nombre: ")
		self.Nombre.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)		

		self.Apellido = tk.Label(self.Mi_Frame, text = "Apellido:")
		self.Apellido.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

		self.Direccion = tk.Label(self.Mi_Frame, text = "Direccion:")
		self.Direccion.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)

		self.Contraseña = tk.Label(self.Mi_Frame, text = "Contraseña:")
		self.Contraseña.grid(row = 3, column = 0, sticky = "e",padx = 10, pady = 10)

		self.Comentario = tk.Label(self.Mi_Frame, text = "Comentarios:")
		self.Comentario.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10)

	def Elaboracion_Scrollbar(self):

		self.Caja_Texto = tk.Text(self.Mi_Frame, width = 16, height = 5)
		self.Caja_Texto.grid(row = 4, column = 1, padx = 1, pady = 10)		

		self.Scroll_bar = tk.Scrollbar(self.Mi_Frame, command = self.Caja_Texto.yview)
		self.Scroll_bar.grid(row = 4, column = 2, sticky = "snw")	

		self.Caja_Texto.configure(yscrollcommand = self.Scroll_bar.set)

	def Elaboracion_Boton(self):

		self.Boton = tk.Button(Raiz, text = "Guardar", command = lambda: self.Guardado())
		self.Boton.pack()

	def Guardado(self):

		if(self.Valor_Nombre.get()):

			self.Resultado = self.Boton.config(text = "Guardado")

			self.Valor_Registrado = open("Registro_De_Interfas.txt", "a")
			self.Valor_Registrado.write(self.Valor_Nombre.get())
			self.Valor_Registrado.write("\n")
			self.Valor_Registrado.write(self.Valor_Apellido.get())
			self.Valor_Registrado.write("\n")
			self.Valor_Registrado.write(self.Valor_Contraseña.get())
			self.Valor_Registrado.write("\n")
			self.Valor_Registrado.write(self.Valor_Direccion.get())
			self.Valor_Registrado.close()

if __name__ == "__main__":

	Raiz = tk.Tk()
	Raiz.title("Registro")
	Raiz.resizable(0,0)

	Objeto_Clase = Registro()
	Objeto_Clase.Elaboracion_Frame()
	Objeto_Clase.Elaboracion_Entrys()
	Objeto_Clase.Elaboracion_Etiquetas()
	Objeto_Clase.Elaboracion_Scrollbar()
	Objeto_Clase.Elaboracion_Boton()

	Raiz.mainloop()