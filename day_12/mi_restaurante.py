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

# Lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Pescado', 'Salmon', 'Kebab', 'Pizza 1', 'Pizza 2', 'Pizza 3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino 1', 'Vino 2', 'Cerveza 1', 'Cerveza 3']
lista_postres = ['Helado', 'Fruta', 'Browni','Flan', 'Muse', 'Pastel 1', 'Pastel 2', 'Pastel 3']

# generar items comida
variables_comida = []

# generar items bebida
variables_bebida = []

# generar items postre
variables_postre = []


contador_comida = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador_comida] = IntVar()
    comida = Checkbutton(panel_comida, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador_comida])
    comida.grid(row=contador_comida, column=0, sticky=W)
    contador_comida += 1

contador_bebida = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador_bebida] = IntVar()
    bebida = Checkbutton(panel_bebida, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1,offvalue=0, variable=variables_bebida[contador_bebida])
    bebida.grid(row=contador_bebida, column=0, sticky=W)
    contador_bebida += 1

contador_postre = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador_postre] = IntVar()
    postre = Checkbutton(panel_postre, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1,offvalue=0, variable=variables_postre[contador_postre])
    postre.grid(row=contador_postre, column=0, sticky=W)
    contador_postre += 1



# Evitar que la pantalla se cierre
aplicacion.mainloop()
