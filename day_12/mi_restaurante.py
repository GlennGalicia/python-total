from tkinter import *

# Crear instancia
aplicacion = Tk()

# Definir tamaño de la ventana
aplicacion.geometry("1200x600+0+0")

# Evitar maximizar pantalla
aplicacion.resizable(False, False)

# Titulo de la ventana
aplicacion.title("Mi restaurante - Sistema de Facturación")

# Color de fondo
aplicacion.config(bg="salmon")

# Evitar que la pantalla se cierre
aplicacion.mainloop()