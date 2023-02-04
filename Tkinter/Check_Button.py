
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

Second_Window = tk.Frame(root).pack()
Title = tk.Label(Second_Window, text = "Elige destinos", width = 20, bg = "pink").pack()

Option_Beach = tk.Checkbutton(Second_Window, text = "Playa" , variable = Beach, onvalue = 1, offvalue = 0, 

	command = lambda: Choose_Trip(), bg = "pink").pack()

Option_Mountain = tk.Checkbutton(Second_Window, text = "Motaña", variable = Mountain , onvalue = 1, offvalue = 0, 

	command = lambda: Choose_Trip(), bg = "pink").pack()

Option_Private = tk.Checkbutton(Second_Window, text = "Turismo Rural", variable = Private, onvalue = 1, offvalue = 0, 

	command = lambda: Choose_Trip(), bg = "pink").pack()

Label_Option = tk.Label(Second_Window, bg = "pink")
Label_Option.pack()

root.mainloop()