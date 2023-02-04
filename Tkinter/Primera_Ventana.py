
import tkinter as tk

class Ventana:

	def __init__(self):

		self.Segunda_Ventana = tk.Frame(root, bg = "#FF66CC", width = "100", height = "100", bd = 35, relief = "groove", 

			cursor = "pirate").pack()

		self.Mensaje = tk.Label(self.Segunda_Ventana, text = "Mi Primera Ventana", bg = "#76FF03", font = (25)).pack()

if __name__ == "__main__":

	root = tk.Tk()
	root.title("Primera Ventana")
	root.iconbitmap()
	root.geometry("400x150")
	root.config(bg = "#76FF03")
	root.resizable(0,0)
	root.attributes('-alpha', 0.6)

	Objeto_Clase = Ventana()
	root.mainloop()