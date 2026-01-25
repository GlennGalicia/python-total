from tkinter import *

operador = ''


def click_boton(num):
    global operador
    operador += num
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

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
panel_costos = Frame(panel_izquierdo, bd=0, relief=FLAT, padx=50)
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
lista_postres = ['Helado', 'Fruta', 'Browni', 'Flan', 'Muse', 'Pastel 1', 'Pastel 2', 'Pastel 3']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador_comida = 0
for comida in lista_comidas:
    # crear checkbuttons
    variables_comida.append('')
    variables_comida[contador_comida] = IntVar()
    comida = Checkbutton(panel_comida,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador_comida])
    comida.grid(row=contador_comida,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador_comida] = StringVar()
    texto_comida[contador_comida].set('0')
    cuadros_comida[contador_comida] = Entry(panel_comida,
                                            font=('Dosis', 19, 'bold'),
                                            bd=1,
                                            width=6,
                                            state=DISABLED,
                                            textvariable=texto_comida[contador_comida])
    cuadros_comida[contador_comida].grid(row=contador_comida,
                                         column=1)
    contador_comida += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador_bebida = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador_bebida] = IntVar()
    bebida = Checkbutton(panel_bebida,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador_bebida])
    bebida.grid(row=contador_bebida,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador_bebida] = StringVar()
    texto_bebida[contador_bebida].set('0')
    cuadros_bebida[contador_bebida] = Entry(panel_bebida,
                                            font=('Dosis', 19, 'bold'),
                                            bd=1,
                                            width=6,
                                            state=DISABLED,
                                            textvariable=texto_bebida[contador_bebida])
    cuadros_bebida[contador_bebida].grid(row=contador_bebida,
                                         column=1)
    contador_bebida += 1

# generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador_postre = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador_postre] = IntVar()
    postre = Checkbutton(panel_postre,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador_postre])
    postre.grid(row=contador_postre,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador_postre] = StringVar()
    texto_postre[contador_postre].set('0')
    cuadros_postre[contador_postre] = Entry(panel_postre,
                                            font=('Dosis', 19, 'bold'),
                                            bd=1,
                                            width=6,
                                            state=DISABLED,
                                            textvariable=texto_postre[contador_postre])
    cuadros_postre[contador_postre].grid(row=contador_postre,
                                         column=1)

    contador_postre += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada "Comidas"
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# etiquetas de costo y campos de entrada "Bebidas"
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# etiquetas de costo y campos de entrada "Postres"
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# etiquetas de costo y campos de entrada "Subtotal"
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# etiquetas de costo y campos de entrada "Impuestos"
etiqueta_impuesto = Label(panel_costos,
                          text='Impuestos',
                          font=('Dosis', 12, 'bold'),
                          fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# etiquetas de costo y campos de entrada "Total"
etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
lista_botones = ['Total', 'Recibo', 'Guardar', 'Reiniciar']
columnas = 0

for boton in lista_botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   fg='black',
                   bd=1,
                   width=8)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 12, 'bold'),
                          width=32,
                          bd=1)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:

    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=8)

    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()
