# Importamos Pandas
import pandas as pd
import matplotlib.pyplot as plt

# Creamos una serie de números y hallamos su media
numeros = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
print(numeros.mean())

# Hallamos la suma de dichos números
print(numeros.sum())

# Creamos una SERIE de tres colores diferentes
colores = pd.Series(['azul', 'gris', 'verde'])

# Visualizamos la serie creada
print(colores)

# Creamos una serie con tipos de autos, y la visualizamos
tipo_autos = pd.Series(['Sedan', 'SUV', 'Pick Up'])
print(tipo_autos)

# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autos = pd.DataFrame({'Tipo Auto': tipo_autos, 'Color': colores})
print(tabla_autos)

# Importar "ventas-autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_auto = pd.read_csv('ventas-autos.csv')
print('\n')

# Exportar el Dataframe como un archivo CSV a mi carpeta "/content/drive/MyDrive/Colab Notebooks/pruebas/"
# ventas_auto.to_csv('ventas-autos-glenn.csv', index=False)

# Analicemos los tipos de datos disponibles en el dataset de ventas autos
print(ventas_auto.dtypes)
print('\n')

# Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset
print(ventas_auto.describe())
print('\n')

# Obtenemos información del dataset utilizando info()
print(ventas_auto.info())
print('\n')

# Listamos los nombres de las columnas de nuestro dataset
print(ventas_auto.columns)
print('\n')

# Averiguamos el "largo" de nuestro dataset
print(len(ventas_auto))
print('\n')

# Mostramos las primeras 5 filas del dataset
print(ventas_auto.head())
print('\n')

# Mostramos las primeras 7 filas del dataset
print(ventas_auto.head(7))
print('\n')

# Mostramos las últimas 7 filas del dataset
print(ventas_auto.tail(7))
print('\n')

# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
print(ventas_auto.loc[3])
print('\n')

# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
print(ventas_auto.iloc[[3, 7, 9]])
print('\n')

# Seleccionar la columna "Kilometraje"
print(ventas_auto['Kilometraje'])
print('\n')

# Encontrar el valor medio de la columnas "Kilometraje"
print(ventas_auto['Kilometraje'].mean())
print('\n')

# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
print(ventas_auto[ventas_auto['Kilometraje'] > 100000])
print('\n')

# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
print(pd.crosstab(ventas_auto['Fabricante'], ventas_auto['Puertas']))
print('\n')

# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
# ventas_auto.groupby(['Fabricante']).mean()
# print('\n')

# Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje
# plt.plot(ventas_auto['Kilometraje'])
# plt.show()

# Puede que un gráfico más apropiado en este caso sea un histograma?
# plt.hist(ventas_auto['Kilometraje'])
# plt.show()

# Elimina la puntuación de la columna de precios
ventas_auto['Precio (USD)'] = ventas_auto['Precio (USD)'].str.replace(r'[\$,\.]', '', regex=True)
ventas_auto['Precio (USD)'] = ventas_auto['Precio (USD)'].astype(int)/100
plt.plot(ventas_auto['Precio (USD)'])
plt.show()