
import tkinter as tk

class Registro:

	def __init__(self):			

		self.valor_nombre = tk.StringVar()
		self.valor_apellido = tk.StringVar()
		self.valor_direccion  = tk.StringVar()
		self.valor_contraseña = tk.StringVar()

	def Elaboracion_Frame(self):

		self.mi_frame = tk.Frame(raiz, width = 1200, height = 600)
		self.mi_frame.pack()

	def Elaboracion_Entrys(self):

		self.nombre = tk.Entry(self.mi_frame, textvariable= self.valor_nombre, width= 30, justify= 'center', fg= '#6D4C41')
		self.nombre.grid(row= 0, column= 1, sticky= 'e', padx= 10, pady= 10)

		self.apellido = tk.Entry(self.mi_frame, textvariable = self.valor_apellido, justify= 'center', fg= '#6D4C41')
		self.apellido.grid(row= 1, column= 1, sticky= 'e', padx= 10, pady= 10)

		self.direccion = tk.Entry(self.mi_frame, textvariable= self.valor_direccion, justify= 'center', fg= '#6D4C41')
		self.direccion.grid(row= 2, column= 1, sticky= 'e', padx= 10, pady = 10)

		self.contraseña = tk.Entry(self.mi_frame, textvariable= self.valor_contraseña, justify= 'center', fg= '#6D4C41', show= "*")
		self.contraseña.grid(row= 3, column = 1, sticky= 'e', padx = 10, pady= 10)

	def Elaboracion_Etiquetas(self):

		self.nombre = tk.Label(self.mi_frame, text= "Nombre: ")
		self.nombre.grid(row= 0, column= 0, sticky= 'e', padx= 10, pady= 10)		

		self.apellido = tk.Label(self.mi_frame, text= "Apellido:")
		self.apellido.grid(row= 1, column= 0, sticky= 'e', padx= 10, pady= 10)

		self.direccion = tk.Label(self.mi_frame, text= "direccion:")
		self.direccion.grid(row= 2, column= 0, sticky= 'e', padx= 10, pady= 10)

		self.contraseña = tk.Label(self.mi_frame, text= "Contraseña:")
		self.contraseña.grid(row= 3, column= 0, sticky= 'e',padx= 10, pady= 10)

		self.comentario = tk.Label(self.mi_frame, text= "Comentarios:")
		self.comentario.grid(row= 4, column= 0, sticky= 'e', padx= 10, pady= 10)

	def Elaboracion_Scrollbar(self):

		self.caja_texto = tk.Text(self.mi_frame, width= 16, height= 5)
		self.caja_texto.grid(row= 4, column= 1, padx= 1, pady= 10)		

		self.scrool_bal = tk.Scrollbar(self.mi_frame, command= self.caja_texto.yview)
		self.scrool_bal.grid(row= 4, column= 2, sticky= 'snw')	

		self.caja_texto.configure(yscrollcommand= self.scrool_bal.set)

	def Elaboracion_Boton(self):

		self.boton = tk.Button(raiz, text= "Guardar", command= lambda: self.Guardado())
		self.boton.pack()

	def Guardado(self):

		if(self.valor_nombre.get()):

			self.boton.config(text= "Guardado")

			self.registro_valor = open("Registro_De_Interfas.txt", 'a')

			self.registro_valor.write(self.valor_nombre.get())
			self.registro_valor.write("\n")
			self.registro_valor.write(self.valor_apellido.get())
			self.registro_valor.write("\n")
			self.registro_valor.write(self.valor_contraseña.get())
			self.registro_valor.write("\n")
			self.registro_valor.write(self.valor_direccion.get())
			
			self.registro_valor.close()

if __name__ == "__main__":

	raiz = tk.Tk()
	raiz.title("Registro")
	raiz.resizable(0,0)

	objeto_clase = Registro()
	objeto_clase.Elaboracion_Frame()
	objeto_clase.Elaboracion_Entrys()
	objeto_clase.Elaboracion_Etiquetas()
	objeto_clase.Elaboracion_Scrollbar()
	objeto_clase.Elaboracion_Boton()

	raiz.mainloop()