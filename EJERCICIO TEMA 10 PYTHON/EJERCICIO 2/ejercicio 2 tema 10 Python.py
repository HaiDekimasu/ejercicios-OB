##En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Luis", "Carlos", "Juan", "Caro", "Vivi", "Pamela"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de Alumnos")
label.pack()
master.mainloop()