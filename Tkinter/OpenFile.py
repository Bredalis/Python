
from tkinter import filedialog
import tkinter as tk

Window = tk.Tk()
Window.title("Open File")
Window.geometry('100x30')
Window.resizable(0,0)

def Open_File():

	Folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", filetypes = (("Keras", "*.py"), ("Tkinter", "*.py")))
	
	File = open(Folder, 'r')

	print(File.read())

tk.Button(Window, text = "Open File", command = lambda: Open_File(), bg = '#EEFF41').pack()

Window.mainloop()