import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('ES_-Lista-de-Celulares-Samsung_MercadoLibre.csv')  # Asegúrate de proporcionar la ruta correcta al archivo CSV


df_septiembre = df[df['Mes '] == 'Septiembre']

# Encontrare el producto que más se repite en septiembre
producto_mas_repetido_septiembre = df_septiembre['Producto'].value_counts().idxmax()

# Encontrare el producto que menos se repite en septiembre
producto_menos_repetido_septiembre = df_septiembre['Producto'].value_counts().idxmin()

# Frecuencia de los productos seleccionados en septiembre
frecuencia_producto_mas_repetido_septiembre = df_septiembre[df_septiembre['Producto'] == producto_mas_repetido_septiembre].shape[0]
frecuencia_producto_menos_repetido_septiembre = df_septiembre[df_septiembre['Producto'] == producto_menos_repetido_septiembre].shape[0]

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))

# Grafica de barras para el producto más repetido en septiembre
plt.bar('Producto más vendido', frecuencia_producto_mas_repetido_septiembre, color='blue', label=producto_mas_repetido_septiembre)

# Grafica de barras para el producto menos repetido en septiembre
plt.bar('Producto menos vendido', frecuencia_producto_menos_repetido_septiembre, color='red', label=producto_menos_repetido_septiembre)

# Configuracion de  las etiquetas del eje y y el título
plt.ylabel('Cantidad de ventas en septiembre')
plt.title('Ventas de productos en septiembre')

# la leyenda
plt.legend()

#  gráfico
plt.show()
