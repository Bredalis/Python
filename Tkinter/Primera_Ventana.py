import tkinter as tk

class Primera_Ventana():

	def __init__(self):

		self.Mi_Frame = tk.Frame(Ventana, width = 100, height = 100, bd = 30, bg = '#FF66CC', relief = 'groove', cursor = 'hand2')
		self.Mi_Frame.pack()

		self.Mensage = tk.Label(self.Mi_Frame, text = "Mi Primera Ventana", font = (18), bg = 'green')
		self.Mensage.pack()

if __name__ == "__main__":

	Ventana = tk.Tk()
	Ventana.title("Primera Ventana")
	Ventana.resizable(0,0)
	
	Clase_Objeto = Primera_Ventana()

	Ventana.mainloop()