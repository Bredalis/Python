
import tkinter as tk

root = tk.Tk()
root.title("Places to travel")
root.config(bg = "pink")
root.resizable(0,0)

Beach = tk.IntVar()
Mountain = tk.IntVar()
Private = tk.IntVar()

def Choose_Trip():

	Option = ""

	if(Beach.get() == 1):

		Option += "Playa  "

	if (Mountain.get() == 1):

		Option += "Montaña  "

	if (Private.get() == 1):
		
		Option += "Turismo Rural"

	Label_Option.config(text = Option)

My_Frame = tk.Frame(root).pack()
Title = tk.Label(My_Frame, text = "Elige destinos", width = 20, bg = "pink").pack()

Option_Beach = tk.Checkbutton(My_Frame, text = "Playa" , variable = Beach, onvalue = 1, offvalue = 0, 

	command = lambda: Choose_Trip(), bg = "pink").pack()

Option_Mountain = tk.Checkbutton(My_Frame, text = "Motaña", variable = Mountain , onvalue = 1, offvalue = 0, 

	command = lambda: Choose_Trip(), bg = "pink").pack()

Option_Private = tk.Checkbutton(My_Frame, text = "Turismo Rural", variable = Private, onvalue = 1, offvalue = 0, 

	command = lambda: Choose_Trip(), bg = "pink").pack()

Label_Option = tk.Label(My_Frame, bg = "pink")
Label_Option.pack()

root.mainloop()