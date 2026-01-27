# Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree

# Leer archivo csv
titanic = pd.read_csv('DataSet_Titanic.csv')

# Visualizar las primeras 5 líneas
# print(titanic.head())

# guardar en variable X los atributos predictores (todas las etiquetas excepto "Sobreviviente")
X = titanic.drop('Sobreviviente', axis=1)

# guardar en y la etiqueta a predecir ("Sobreviviente")
Y = titanic.Sobreviviente

# visualizar x
# print(X.head())

# visualizar y
# print(Y.head())

# creamos un objeto arbol
arbol = DecisionTreeClassifier(max_depth=2, random_state=42)

# entrenar a la máquina
arbol.fit(X, Y)

# predecimos sobre el set
pred_y = arbol.predict(X)

# comparar con etiquetas reales
print('Precision: ', accuracy_score(pred_y, Y))

# crear matriz de confusión
# cm = confusion_matrix(Y, pred_y)

# creamos un gráfico para la matriz de confusión
# disp = ConfusionMatrixDisplay(confusion_matrix=cm,)
# disp.plot(cmap='Blues', values_format='.0f')
# plt.show()

# creamos un gráfico para la matriz de confusión normalizada
cm = confusion_matrix(Y, pred_y, normalize='true')
disp = ConfusionMatrixDisplay(confusion_matrix=cm,)
disp.plot(cmap='Blues', values_format='.2f')
plt.show()

# mostramos un árbol gráficamente
plt.figure(figsize=(10, 8))
tree.plot_tree(arbol, filled=True, feature_names=X.columns)
plt.show()

# graficamos las importancias en un gráfico de barras
# creamos las variables x (importancias) e y (columnas)
importancias = arbol.feature_importances_
columnas = X.columns

# creamos el gráfico
sns.barplot(x=columnas, y=importancias)
plt.title('Feature Importance')
plt.show()