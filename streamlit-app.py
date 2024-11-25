import streamlit as st
import pandas as pd

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=';')

# Créer un titre
st.title("Mes tableaux de bord d'Iris sur Streamlit")

# Afficher les données dans un tableau
#st.table(data)
import altair as alt
import pandas as pd

# Create a chart
chart = alt.Chart(data).mark_bar().encode( x='SepalLength', y='PetalWidth') 

# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)

import streamlit as st

# Add a title to the sidebar
st.sidebar.title("Iris Visualisation Menu") 

# Add widgets to the sidebar
option = st.sidebar.selectbox("Choose an Option:", 
              ["vertosa", "virginica", "versicolor"]
)
import altair as alt
import pandas as pd

# Create a chart
chart = alt.Chart(data).mark_line().encode( x='SepalWidth', y='PetalLength') 

# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)
import altair as alt
import pandas as pd

# Create a chart
chart = alt.Chart(data).mark_arc().encode( x='SepalWidth', y='SepalLength') 

# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)
















