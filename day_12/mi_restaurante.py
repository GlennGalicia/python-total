from tkinter import *
import datetime
import random
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


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


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    y = 0
    for c in cuadros_bebida:
        if variables_bebida[y].get() == 1:
            cuadros_bebida[y].config(state=NORMAL)
            if cuadros_bebida[y].get() == '0':
                cuadros_bebida[y].delete(0, END)
            cuadros_bebida[y].focus()
        else:
            cuadros_bebida[y].config(state=DISABLED)
            texto_bebida[y].set('0')
        y += 1

    z = 0
    for c in cuadros_postre:
        if variables_postre[z].get() == 1:
            cuadros_postre[z].config(state=NORMAL)
            if cuadros_postre[z].get() == '0':
                cuadros_postre[z].delete(0, END)
            cuadros_postre[z].focus()
        else:
            cuadros_postre[z].config(state=DISABLED)
            texto_postre[z].set('0')
        z += 1


def total():
    suma_total_comida = 0
    indice = 0
    for cantidad in texto_comida:
        suma_total_comida += (float(cantidad.get()) * precios_comida[indice])
        indice += 1

    suma_total_bebida = 0
    indice = 0
    for cantidad in texto_bebida:
        suma_total_bebida += (float(cantidad.get()) * precios_bebida[indice])
        indice += 1

    suma_total_postre = 0
    indice = 0
    for cantidad in texto_postre:
        suma_total_postre += (float(cantidad.get()) * precios_postres[indice])
        indice += 1

    suma_total = suma_total_comida + suma_total_bebida + suma_total_postre
    impuestos = suma_total * 0.07
    total = suma_total + impuestos

    var_costo_comida.set(f'$ {round(suma_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(suma_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(suma_total_postre, 2)}')

    var_subtotal.set(f'$ {round(suma_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 61 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 61 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'${int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${int(postre.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 61 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 61 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 61 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto.')


def guardar():
    info_recibio = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    archivo.write(info_recibio)
    archivo.close()
    messagebox.showinfo("Información", "Su recibo ha sido guardado.")

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
                         variable=variables_comida[contador_comida],
                         command=revisar_check)
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
                         variable=variables_bebida[contador_bebida],
                         command=revisar_check)
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
                         variable=variables_postre[contador_postre],
                         command=revisar_check)
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

# etiquetas de costo z campos de entrada "Comidas"
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
botones_creados = []
columnas = 0

for boton in lista_botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   fg='black',
                   bd=1,
                   width=8)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)

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
