import streamlit as st
import pandas as pd



st.write("# Cyb2077 Tableau de chasse")   # du markdown
df = pd.DataFrame({
    "Gang": ["NCPD", "Tyger claws", "Kang tao", "Arasaka", "Valentinos", "Wraiths"],
    "Quantite": [100, 2000, 200, 700, 800, 500]
})

# Ici un effort est fait sur la présentation

col1,col2 = st.columns(2)
with col1:
    df
with col2:
    st.bar_chart(df,x="Gang",y="Quantite")


