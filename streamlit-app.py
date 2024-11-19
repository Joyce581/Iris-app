import streamlit as st
import pandas as pd

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=';')

# Créer un titre
st.title("Mon premier tableau de bord Streamlit")

# Afficher les données dans un tableau
st.table(data)

import altair as alt
import pandas as pd

# Create a chart
chart = alt.Chart(data).mark_line(point=True).encode(
      x = 'Sepal Length'
      y = 'Petal Width'
)
