
import tkinter as tk

roof = tk.Tk()
roof.title("Places to travel")
roof.config(bg= 'pink')
roof.resizable(0,0)

beach = tk.IntVar()
mountain = tk.IntVar()
private = tk.IntVar()

def Choose_Trip():

	Option = ""

	if(beach.get() == 1):
		Option += "Playa  "

	if (mountain.get() == 1):
		Option += "Montaña  "

	if (private.get() == 1):		
		Option += "Turismo Rural"

	label_option.config(text= Option)

my_frame = tk.Frame(roof).pack()

tk.Label(my_frame, text= "Elige destinos", width= 20, bg= 'pink').pack()

tk.Checkbutton(my_frame, text= "Playa", variable= beach, onvalue= 1, offvalue= 0, bg= 'pink', command= lambda: Choose_Trip()).pack()
tk.Checkbutton(my_frame, text= "Motaña", variable= mountain, onvalue= 1, offvalue= 0, bg= 'pink', command= lambda: Choose_Trip()).pack()
tk.Checkbutton(my_frame, text= "Turismo Rural", variable= private, onvalue= 1, offvalue= 0, bg= 'pink', command= lambda: Choose_Trip()).pack()

label_option = tk.Label(my_frame, bg= 'pink')
label_option.pack()

roof.mainloop()