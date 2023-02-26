
import tkinter as tk

class Registro():

	def __init__(self):			

		self.Valor_Nombre = tk.StringVar()
		self.Valor_Apellido = tk.StringVar()
		self.Valor_Direccion  = tk.StringVar()
		self.Valor_Contraseña = tk.StringVar()

	def Etiquetas(self):

		self.Nombre = tk.Label(Ventana, text = "Nombre: ")
		self.Nombre.grid(row = 0, column = 0, sticky = 'e', padx = 10, pady = 10)		

		self.Apellido = tk.Label(Ventana, text = "Apellido:")
		self.Apellido.grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Direccion = tk.Label(Ventana, text = "Direccion:")
		self.Direccion.grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Contraseña = tk.Label(Ventana, text = "Contraseña:")
		self.Contraseña.grid(row = 3, column = 0, sticky = 'e', padx = 10, pady = 10)

		self.Comentario = tk.Label(Ventana, text = "Comentarios:")
		self.Comentario.grid(row = 4, column = 0, sticky = 'e', padx = 10, pady = 10)

	def Entrys(self):

		self.Nombre = tk.Entry(Ventana, textvariable = self.Valor_Nombre, width = 30, justify = 'center', fg = '#6D4C41')
		self.Nombre.grid(row = 0, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Apellido = tk.Entry(Ventana, textvariable = self.Valor_Apellido, justify = 'center', fg = '#6D4C41')
		self.Apellido.grid(row = 1, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Direccion = tk.Entry(Ventana, textvariable = self.Valor_Direccion, justify = 'center', fg = '#6D4C41')
		self.Direccion.grid(row = 2, column = 1, sticky = 'e', padx = 10, pady = 10)

		self.Contraseña = tk.Entry(Ventana, textvariable = self.Valor_Contraseña, justify = 'center', fg = '#6D4C41', show = "*")
		self.Contraseña.grid(row = 3, column = 1, sticky = 'e', padx = 10, pady = 10)

	def Scrollbar(self):

		self.Caja_Texto = tk.Text(Ventana, width = 16, height = 5) 
		self.Caja_Texto.grid(row = 4, column = 1, padx = 1, pady = 10)		

		self.Scroll_Bar = tk.Scrollbar(Ventana, command = self.Caja_Texto.yview)
		self.Scroll_Bar.grid(row = 4, column = 2, sticky = 'snw')	

		self.Caja_Texto.configure(yscrollcommand = self.Scroll_Bar.set)

	def Boton(self):

		self.Boton = tk.Button(Ventana, text = "Guardar", command = lambda: self.Guardado())
		self.Boton.grid(row = 5, column = 1)

	def Guardado(self):

		if(self.Valor_Nombre.get() and self.Valor_Direccion.get() and self.Valor_Contraseña.get()):

			self.Boton.config(text = "Guardado")

			self.Datos_Registro = open("Registro_De_Usuario.txt", 'a')

			self.Datos_Registro.write("Datos del Registro")

			self.Datos_Registro.write("\n\n")
			self.Datos_Registro.write("Nombre: ")
			self.Datos_Registro.write(self.Valor_Nombre.get())
			self.Datos_Registro.write("\n\n")
			self.Datos_Registro.write("Apellido: ")
			self.Datos_Registro.write(self.Valor_Apellido.get())
			self.Datos_Registro.write("\n\n")
			self.Datos_Registro.write("Contraseña: ")
			self.Datos_Registro.write(self.Valor_Contraseña.get())
			self.Datos_Registro.write("\n\n")
			self.Datos_Registro.write("Direccion: ")
			self.Datos_Registro.write(self.Valor_Direccion.get())
			self.Datos_Registro.write("\n\n")
			
			self.Datos_Registro.close()

			[self.Valor_Nombre.set(""), self.Valor_Apellido.set(""),self.Valor_Contraseña.set(""), self.Valor_Direccion.set("")]

if __name__ == "__main__":

	Ventana = tk.Tk()
	Ventana.title("Registro")
	Ventana.resizable(0,0)

	Clase_Objeto = Registro()
	Clase_Objeto.Etiquetas()
	Clase_Objeto.Entrys()
	Clase_Objeto.Scrollbar()
	Clase_Objeto.Boton()

	Ventana.mainloop()