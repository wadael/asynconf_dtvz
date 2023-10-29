import plotly.express as px
import streamlit as st
import pandas as pd

#
#   La conversion vers Streamlit de l'exemple de DASH'
#


st.write("# Ma première appli")   # du markdown
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Quantite": [4, 1, 2, 2, 4, 5],
    "Ville": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Fruit", y="Quantite", color="Ville", barmode="group")

st.write("## Afficher le graphique")
st.write(fig)
