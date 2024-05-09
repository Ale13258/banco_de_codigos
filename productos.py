import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('DATA_PRODUCTOS.csv')


meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
df['Mes_Venta'] = df['Mes_Venta'].map(meses)

ventas_enero = df[df['Mes_Venta'] == 1]


producto_mas_repetido = ventas_enero['Producto'].mode().iloc[0]


producto_menos_repetido = ventas_enero['Producto'].value_counts().idxmin()


ventas_producto_mas_repetido = ventas_enero[ventas_enero['Producto'] == producto_mas_repetido]


ventas_producto_menos_repetido = ventas_enero[ventas_enero['Producto'] == producto_menos_repetido]


plt.figure(figsize=(10, 6))
plt.hist(ventas_producto_mas_repetido['Precio'], bins=5, color='skyblue', edgecolor='black', rwidth=0.8)
plt.title(f'Histograma de ventas en enero para el producto más repetido: {producto_mas_repetido}')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.tight_layout() 
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(ventas_producto_menos_repetido['Precio'], bins=5, color='skyblue', edgecolor='black', rwidth=0.8)
plt.title(f'Histograma de ventas en enero para el producto menos repetido: {producto_menos_repetido}')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.tight_layout()  
plt.show()
producto_mas_repetido = df['Producto'].mode().iloc[0]


producto_menos_repetido = df['Producto'].value_counts().idxmin()

plt.figure(figsize=(10, 6))
plt.hist(df['Mes_Venta'], bins=range(1, 14), align='left', color='skyblue', edgecolor='black', rwidth=0.8)
plt.title('Histograma de ventas para todos los meses')
plt.xlabel('Mes')
plt.ylabel('Frecuencia')
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()  
plt.show()

print(f"El producto más repetido en todos los meses es: {producto_mas_repetido}")

print(f"El producto menos repetido en todos los meses es: {producto_menos_repetido}")
producto_mas_repetido = df['Producto'].mode().iloc[0]

#  producto menos repetido en todos los meses
producto_menos_repetido = df['Producto'].value_counts().idxmin()

#  Filtro de  para el producto más repetido en todos los meses
ventas_producto_mas_repetido = df[df['Producto'] == producto_mas_repetido]

# Filtro de datos para el producto menos repetido en todos los meses
ventas_producto_menos_repetido = df[df['Producto'] == producto_menos_repetido]


plt.figure(figsize=(10, 6))

# Histograma para el producto más repetido en rojo
plt.hist(ventas_producto_mas_repetido['Mes_Venta'], bins=range(1, 14), align='left', color='red', edgecolor='black', rwidth=0.5, alpha=0.5, label=producto_mas_repetido)

# Histograma para el producto menos repetido en azul
plt.hist(ventas_producto_menos_repetido['Mes_Venta'], bins=range(1, 14), align='left', color='blue', edgecolor='black', rwidth=0.5, alpha=0.5, label=producto_menos_repetido)

plt.title('Histograma de ventas para todos los meses')
plt.xlabel('Mes')
plt.ylabel('Frecuencia')
plt.xticks(range(1, 13))
plt.grid(True)

# Agregar una leyenda
plt.legend()

plt.tight_layout()  

print(f"El producto más repetido en todos los meses es: {producto_mas_repetido}")


print(f"El producto menos repetido en todos los meses es: {producto_menos_repetido}")