import streamlit as st
import pandas as pd

st.write("# Cyb2077 Tableau de chasse")   # du markdown
df = pd.DataFrame({
    "Gang": ["NCPD", "Tyger claws", "Kang tao", "Arasaka", "Valentinos", "Wraiths"],
    "Quantite": [100, 2000, 200, 200, 800, 500]
})
df # pour afficher directement le dataframe
st.bar_chart(df,x="Gang",y="Quantite")


