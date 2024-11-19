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
st.sidebar.title("Joyce's Sidebar Menu") 

# Add widgets to the sidebar
option = st.sidebar.selectbox("Choose an Option:", 
              ["Data Classification", "Iris Classification"]
)
  
import streamlit as st
import matplotlib as plt

# Sidebar for feature selection
x_feature = st.sidebar.selectbox("Select X-axis feature", df.columns[:-1]
y_feature = st.sidebar.selectbox("Select Y-axis feature", df.columns[:-1]

# Create matplotlib scatter plot
fig, ax = plt.subplots()
for Species in
df['Species'].unique(): Species_data = df[df['Species'] == Species]

ax.scatter(Species_data[x_feature], Species_data[x_feature], label=Species)
ax.set_xlabel(x_feature)
ax.set_ylabel(y_feature)
ax.legend()

# display the plot in Streamlit
st.pyplot(fig)













