import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# Títulos
st.title('Visualización de Datos de Vehículos')

# Crear botones para generar gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Si se hace clic en el botón de histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de vehículos')
    fig_hist = px.histogram(car_data, x="odometer",
                            title='Histograma de Odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Si se hace clic en el botón de gráfico de dispersión
if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de vehículos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title='Gráfico de Dispersión: Odometer vs Precio')
    st.plotly_chart(fig_scatter, use_container_width=True)

#  Usar casillas de verificación
st.write('Selecciona qué gráfico deseas ver:')
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de vehículos')
    fig_hist = px.histogram(car_data, x="odometer",
                            title='Histograma de Odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de vehículos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title='Gráfico de Dispersión: Odometer vs Precio')
    st.plotly_chart(fig_scatter, use_container_width=True)
