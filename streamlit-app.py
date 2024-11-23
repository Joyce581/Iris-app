import streamlit as st
import pandas as pd

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=';')

# Créer un titre
st.title("Mon premier tableau de bord Streamlit")

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
import streamlit as st
import matplotlib.pyplot as plt

# Les données pour le graphique
labels = ['setosa', 'versicolor', 'virginica']
sizes = [25, 30, 45]  # Pourcentages des parts
colors = ['gold', 'yellowgreen', 'lightcoral',]
explode = (0.1, 0, 0) 

# Création du graphique
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax.axis('equal')  # Assure que le diagramme est dessiné en cercle.

# Affichage du graphique dans Streamlit
st.pyplot(fig)
















