import pandas as pd
import plotly.express as px
import plotly.express as px
df = pd.read_csv('Desempleabilidad_Posgrado_Ingenieria_Sistemas_Further_Updated.csv')
print(df)

# Suponiendo que tu DataFrame se llama df
fig = px.histogram(df, x='Tiempo hasta primer empleo (meses)',
                   title='Distribución del Tiempo hasta el Primer Empleo',
                   labels={'Tiempo hasta primer empleo (meses)': 'Meses hasta el primer empleo'},
                   nbins=12)
fig.show()
fig = px.histogram(df, x='Situación actual (empleo)', color='Cambio de empleo (sí/no)',
                   title='Situación de Empleo y Cambio de Empleo',
                   barmode='group',
                   labels={'Situación actual (empleo)': 'Situación de Empleo', 'Cambio de empleo (sí/no)': '¿Cambio de Empleo?'})
fig.show()


# Suponiendo que tu DataFrame se llama df
fig = px.box(df, x='Utilización de conocimientos (sí/no)', y='Salario inicial (miles de pesos)',
             color='Mejora de pensum (sí/no)',
             title='Relación entre la Utilización de Conocimientos y la Percepción de Mejora del Pensum',
             labels={
                 'Utilización de conocimientos (sí/no)': 'Utilización de Conocimientos',
                 'Salario inicial (miles de pesos)': 'Salario Inicial',
                 'Mejora de pensum (sí/no)': 'Necesidad de Mejorar el Pensum'
             },
             category_orders={"Utilización de conocimientos (sí/no)": ["Sí", "No"],
                              "Mejora de pensum (sí/no)": ["Sí", "No"]})
fig.update_traces(quartilemethod="inclusive")  # or 'exclusive' or 'linear' by your choice
fig.show()