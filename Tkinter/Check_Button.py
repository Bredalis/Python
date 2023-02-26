
import tkinter as tk

Window = tk.Tk()
Window.title("Places to travel")
Window.config(bg= 'pink')
Window.resizable(0,0)

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

tk.Label(Window, text = "Elige Destino", width = 20, bg = 'pink').pack()

Label_Option = tk.Label(Window, bg = 'pink')
Label_Option.pack(side = 'bottom')

tk.Checkbutton(Window, text = "Playa", variable = Beach, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Choose_Trip()).pack()
tk.Checkbutton(Window, text = "Motaña", variable = Mountain, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Choose_Trip()).pack()
tk.Checkbutton(Window, text = "Turismo Rural", variable = Private, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Choose_Trip()).pack()

Window.mainloop()