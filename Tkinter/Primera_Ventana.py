
import tkinter as tk

class Menssage:

	def __init__(self):

		self.My_Frame = tk.Frame(roof, bg = '#FF66CC', width = 100, height = 100, bd = 35, relief = 'groove', cursor = 'pirate').pack()

		self.Menssage = tk.Label(self.My_Frame, text = "Mi Primera Ventana", bg = '#76FF03', font = (25)).pack()

if __name__ == "__main__":

	roof = tk.Tk()
	roof.title("Primera Ventana")
	roof.iconbitmap()
	roof.geometry('400x150')
	roof.config(bg = '#76FF03')
	roof.resizable(0,0)
	roof.attributes('-alpha', 0.9)

	Class_Object = Menssage()
	
	roof.mainloop()