
import tkinter as tk

class Registro:

	def __init__(self):

		self.lados = 'center'
		self.Colores = ['#795548', '#80DEEA']

	def Elaboracion_Frame(self):

		self.mi_frame = tk.Frame(raiz, width= 1200, height= 600, bg= self.Colores[1])
		self.mi_frame.pack()

	def Elaboracion_Entrys(self):

		self.nombre = tk.Entry(self.mi_frame, justify= self.lados, fg= self.Colores[0])
		self.nombre.grid(row= 0, column= 1, sticky= 'e', padx= 10, pady= 10)

		self.apellido = tk.Entry(self.mi_frame, justify= self.lados, fg= self.Colores[0])
		self.apellido.grid(row= 1, column= 1, sticky= 'e', padx= 10, pady= 10)

		self.direccion = tk.Entry(self.mi_frame, justify= self.lados, fg= self.Colores[0])
		self.direccion.grid(row= 2, column= 1, sticky= 'e', padx= 10, pady= 10)

		self.contraseña = tk.Entry(self.mi_frame, justify= self.lados, show= '*')
		self.contraseña.grid(row= 3, column= 1, sticky= 'e', padx= 10, pady= 10)

	def Elaboracion_Etiquetas(self):

		self.nombre = tk.Label(self.mi_frame, text= "Nombre: ", bg= self.Colores[1])
		self.nombre.grid(row= 0, column= 0, sticky= 'e', padx= 10, pady= 10)

		self.apellido = tk.Label(self.mi_frame, text= "Apellido:", bg= self.Colores[1])
		self.apellido.grid(row= 1, column= 0, sticky= 'e', padx= 10, pady= 10)

		self.direccion = tk.Label(self.mi_frame, text= "Direccion de casa:", bg= self.Colores[1])
		self.direccion.grid(row= 2, column= 0, sticky= 'e', padx= 10, pady= 10)

		self.contraseña = tk.Label(self.mi_frame, text= "Contraseña:", bg= self.Colores[1])
		self.contraseña.grid(row= 3, column= 0, sticky= 'e', padx= 10, pady= 10)

if __name__ == "__main__":

	raiz = tk.Tk()
	raiz.title("Registro De Interfaz")
	raiz.resizable(0,0)
		
	clase_objeto = Registro()
	clase_objeto.Elaboracion_Frame()
	clase_objeto.Elaboracion_Entrys()
	clase_objeto.Elaboracion_Etiquetas()

	raiz.mainloop()	