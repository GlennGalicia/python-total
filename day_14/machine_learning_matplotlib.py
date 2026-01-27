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
    y.append(num**2)

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
y_1 = x_1**2

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

# Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario,
# y el eje y contiene los valores.


# Añadimos los títulos correspondientes

# Probemos a continuación con un gráfico de barras horizontales

#######
# Un gráfico semejante es un histograma. Podemos generar números aleatorios que siguen una distribución normal (que se acumulan en torno a un valor central), con la función randn:
# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
# Creamos el histograma

#######
# Veamos ahora un caso más complejo, trabajando con subplots, o figuras que cotienen varios gráficos:
# Creamos una figura con 4 subgráficos (2 por fila)


#######
# Añadimos datos a cada uno de los gráficos (axes)
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5


# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas


# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión


# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda


# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal

#######
# Matplotlib tiene un conjunto de varios estilos disponibles, podemos verificarlos de la siguiente manera:
# Verificamos estilos disponibles
# Cambiamos el estilo predeterminado por "seaborn-whitegrid"

#######
# Habiendo cambiado el estilo (el cambio más evidente que veremos será una grilla en el fondo de cada gráfico), cambiaremos también los colores de las líneas, puntos y barras en cada uno de los gráficos por códigos hex a nuestra preferencia:
# Copiamos los valores de los gráficos anteriores
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5


# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas


# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión


# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda


# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
