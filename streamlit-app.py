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
# Plots
def make_choropleth(PetalLength, PetalWidth, SepalWidth, SepalLength):
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column,
                               color_continuous_scale=input_color_theme,
                               hover_name= input_id,
                               locationmode='ISO-3')
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
return choropleth














