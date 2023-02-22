
from tkinter import filedialog
import tkinter as tk

roof = tk.Tk()
roof.title("Open File")
roof.geometry('100x30')
roof.resizable(0,0)

def Open_File():

	file = filedialog.askopenfilename(title= "Open", initialdir= "C:", filetypes= (("New folder", "*.py"), ("tkinter", "*.py")))
	
	print(file)

tk.Button(roof, text= "Open file", command= lambda: Open_File(), bg= '#EEFF41').pack()

roof.mainloop()