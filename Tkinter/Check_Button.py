
import tkinter as tk

roof = tk.Tk()
roof.title("Places to travel")
roof.config(bg = 'pink')
roof.resizable(0,0)

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

My_Frame = tk.Frame(roof).pack()

tk.Label(My_Frame, text = "Elige destinos", width = 20, bg = 'pink').pack()

tk.Checkbutton(My_Frame, text = "Playa", variable = Beach, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Choose_Trip()).pack()
tk.Checkbutton(My_Frame, text = "Motaña", variable = Mountain, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Choose_Trip()).pack()
tk.Checkbutton(My_Frame, text = "Turismo Rural", variable = Private, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Choose_Trip()).pack()

Label_Option = tk.Label(My_Frame, bg = 'pink')
Label_Option.pack()

roof.mainloop()