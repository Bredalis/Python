
import tkinter as tk

roof = tk.Tk()
roof.title("¡Saludo!")
roof.resizable(0,0)

my_frame = tk.Frame(roof, width= 500, height= 500, bg= 'pink')
my_frame.pack()

tk.Label(my_frame, text= "Hola Mundo de la programacion", fg= 'blue', font= (18), bg= 'pink').pack()

roof.mainloop()