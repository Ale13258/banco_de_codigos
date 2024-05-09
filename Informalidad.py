
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv('Informalidad_Laboral_Colombia.csv')
print (df)

# Crear figura
fig = go.Figure()

# Agregar barras para el empleo informal
fig.add_trace(go.Bar(
    x=df['Sector'],
    y=df['Empleo_Informal'],
    name='Empleo Informal',
    marker_color='indianred'
))

# Agregar barras para el empleo formal
fig.add_trace(go.Bar(
    x=df['Sector'],
    y=df['Empleo_Formal'],
    name='Empleo Formal',
    marker_color='lightsalmon'
))

# Actualizar diseño de la figura
fig.update_layout(
    title='Comparación de Empleo Formal e Informal por Sector',
    xaxis_title='Sector',
    yaxis_title='Cantidad de Empleo',
    barmode='group',
    legend_title='Tipo de Empleo'
)

# Mostrar figura
fig.show()