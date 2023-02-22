
import tkinter as tk

class Menssage:

	def __init__(self):

		self.my_frame = tk.Frame(roof, bg= '#FF66CC', width= 100, height= 100, bd= 35, relief= 'groove', cursor= 'pirate').pack()
		self.menssage = tk.Label(self.my_frame, text= "Mi Primera Ventana", bg= '#76FF03', font= (25)).pack()

if __name__ == "__main__":

	roof = tk.Tk()
	roof.title("Primera Ventana")
	roof.geometry('400x150')
	roof.config(bg= '#76FF03')
	roof.resizable(0,0)
	roof.attributes('-alpha', 0.9)

	class_object = Menssage()
	
	roof.mainloop()