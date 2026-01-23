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

# Panel superior
panel_superior = Frame(aplicacion, bd=0, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="white",
                        font=('Dosis', 52), bg="salmon", width=27)

etiqueta_titulo.grid(row=0, column=0)

# Panel Izquiero
panel_izquierdo = Frame(aplicacion, bd=0, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=0, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comida = LabelFrame(panel_izquierdo, text="Comida", font=('Dosis', 19, 'bold'), bd=0, relief=FLAT)
panel_comida.pack(side=LEFT)

# Panel bebidas
panel_bebida = LabelFrame(panel_izquierdo, text="Bebidas", font=('Dosis', 19, 'bold'), bd=0, relief=FLAT)
panel_bebida.pack(side=LEFT)

# Panel Postres
panel_postre = LabelFrame(panel_izquierdo, text="Postres", font=('Dosis', 19, 'bold'), bd=0, relief=FLAT)
panel_postre.pack(side=LEFT)

# Panel Derecho
panel_derecho = Frame(aplicacion, bd=0, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=0, relief=FLAT)
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecho, bd=0, relief=FLAT)
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecho, bd=0, relief=FLAT)
panel_botones.pack()


# Evitar que la pantalla se cierre
aplicacion.mainloop()
