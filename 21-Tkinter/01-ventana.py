""" 
¿Que es Tkinter?
Modulo para crear interfaces graficas de usuario
"""

from tkinter import *

# ? Crear la ventana raiz
ventana = Tk()

# * Cambio en el tamañop de la ventana
ventana.geometry("750x450")

# * Bloquear el tamaño de la ventana
ventana.resizable(1,1) # 1,1; 1,0; 0,0; 0,1

# * Poner imagen de icono
ventana.iconbitmap("21-Tkinter/img/descarga.png")

# ? Arrancar y mostrar la ventana hasta que se cierre

# * Debe ser el ultimo, para poder hacer cualquier cambio en la ventana
ventana.mainloop()