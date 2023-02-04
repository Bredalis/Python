
import tkinter as tk

root = tk.Tk()
root.title("¡Saludo!")
root.resizable(0,0)

Second_Window = tk.Frame(root, width = 500, height = 500, bg = "pink")
Second_Window.pack()

Imagen = tk.PhotoImage()

tk.Label(Second_Window, text = "Hola Mundo, de la programacion", fg = "blue", font = (18), bg = "pink").pack()

root.mainloop()