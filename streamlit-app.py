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
import numpy as np

# Générer des données aléatoires pour le graphique en nuage de points
x = np.random.rand(50)
y = np.random.rand(50)

# Créer le graphique
fig, ax = plt.subplots()
ax.scatter(x, y)

# Ajouter des labels
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_title('Graphique en Nuage de Points')

# Afficher le graphique dans Streamlit
st.pyplot(fig)
import streamlit as st
import plotly.express as px
import numpy as np

# Générer des données aléatoires pour le graphique en nuage de points
x = np.random.rand(50)
y = np.random.rand(50)

# Créer le graphique
fig = px.scatter(x=x, y=y, labels={'x': 'Sepal Length', 'y': 'Petal Length'}, title='Graphique en Nuage de Points')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)















