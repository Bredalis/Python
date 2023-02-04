
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Open File")
root.geometry("100x30")
root.resizable(0,0)

def Open_File():

	Fichero = filedialog.askopenfilename(title = "Open", initialdir = "C:", filetypes = (("New folder", "*.py"), ("tkinter", "*.py")))
	
	print(Fichero)

tk.Button(root, text = "Open File", command = lambda: Open_File(), bg = "#EEFF41").pack()

root.mainloop()