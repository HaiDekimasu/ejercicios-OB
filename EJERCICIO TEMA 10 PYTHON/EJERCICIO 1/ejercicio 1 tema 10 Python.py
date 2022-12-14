##En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
##Al principio no tiene que haber una opción seleccionada.
from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
label = Label(text="QUIEN GANARA EL MUNDIAL")
label.pack()

Radiobutton(root, text="Argentina", variable=opcion, 
            value='Argentina', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Portugal", variable=opcion, 
            value='Portugal', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Brasil", variable=opcion,   
            value='Brasil', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Francia", variable=opcion,   
            value='Francia', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()