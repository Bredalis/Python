
import tkinter as tk
from tkinter import filedialog

roof = tk.Tk()
roof.title("Open File")
roof.geometry('100x30')
roof.resizable(0,0)

def Open_File():

	File = filedialog.askopenfilename(title = "Open", initialdir = "C:", filetypes = (("New folder", "*.py"), ("tkinter", "*.py")))
	
	print(File)

tk.Button(roof, text = "Open File", command = lambda: Open_File(), bg = '#EEFF41').pack()

roof.mainloop()