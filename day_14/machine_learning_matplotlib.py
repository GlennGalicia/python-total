# Importamos el módulo de Matplotlib como plt
import matplotlib.pyplot as plt
import numpy as np

#######
# Creamos un gráfico utilizando plt.plot()
# plt.plot()
# plt.show()

#######
# Graficamos una lista de números
# a = [1,5,3,8,7,15]
# plt.plot(a)
# plt.show()

#######
# Creamos dos listas, x e y. Llenamos a la lista x de valores del 1 al 100.
# x = list(range(101))
# Los valores de y van a equivaler al cuadrado del respectivo valor en x con el mísmo índice
# y = []
# for num in x:
# #     y.append(num**2)
# # Graficamos ambas listas creadas
# plt.plot(x, y)
# plt.show()

#######
# Veamos cómo sería un flujo de trabajo en Matplotlib

# Preparar los datos
x = list(range(101))
y = []
for num in x:
    y.append(num ** 2)

# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x, y)

# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title='Grafico de casos COVID 19 LATAM', xlabel='Días', ylabel='Casos COVID')

# Guardamos nuestro gráfico empleando fig.savefig()
fig.savefig('casos_COVID.png')

#######
# Veamos ahora un gráfico de dispersión:
# creamos un nuveo set de datos utilizando la librería Numpy
x_1 = np.linspace(0, 10, 20)
y_1 = x_1 ** 2

# Creamos el gráfico de dispersión de x vs y
fig, ax = plt.subplots()
ax.scatter(x_1, y_1)
fig.show()

# Visualizamos ahora la función seno, utilizando np.sin(X)
fig, ax = plt.subplots()
x_2 = np.linspace(-10, 10, 100)
y_2 = np.sin(x_2)
ax.scatter(x_2, y_2)
fig.show()

#######
# Veamos ahora otro tipo de gráfico. Por ejemplo, un gráfico de barras, que por lo general asocia resultados numéricos a variables categóricas (categorías)
# Creemos un diccionario con tres platos y su respectivo precio
# Las claves del diccionario serán los nombres de las comidas, y los valores asociados, su precio
comidas = {'lasaña': 350, 'sopa': 150, 'roast beef': 650}

# Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario,
# y el eje y contiene los valores.
fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())

# Añadimos los títulos correspondientes
ax.set(title='Precio de comidas', xlabel='Comidas', ylabel='Precios')
fig.show()

# Probemos a continuación con un gráfico de barras horizontales
fig, ax = plt.subplots()
ax.barh(comidas.keys(), comidas.values())
fig.show()

#######
# Un gráfico semejante es un histograma. Podemos generar números aleatorios que siguen una distribución normal (que se acumulan en torno a un valor central), con la función randn:
# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
# Creamos el histograma
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x)
fig.show()


#######
# Habiendo cambiado el estilo (el cambio más evidente que veremos será una grilla en el fondo de cada gráfico), cambiaremos también los colores de las líneas, puntos y barras en cada uno de los gráficos por códigos hex a nuestra preferencia:
# Copiamos los valores de los gráficos anteriores
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax_1, ax_2), (ax_3, ax_4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax_1.plot(x_1, y_1, color='#fcba03')

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax_2.scatter(x_2, y_2, color='#fcba03')

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax_3.bar(comidas.keys(), comidas.values(), color='#03c6fc')

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax_4.hist(np.random.randn(1000), color='#fc036b')
fig.show()