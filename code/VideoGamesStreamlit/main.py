import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Le business mondial des jeux vidéo",
    page_icon="💰",
    layout='wide',
    initial_sidebar_state="expanded"
)


if 'df' not in st.session_state:
    df = pd.read_csv("vgsales.csv")
    df = df.sort_values(['Year','Platform'])
    df = df.fillna(0)
    st.session_state.df = df
else:
    df=st.session_state.df

st.write("# Jeux Vidéo ")
## filtered_df = dataframe_explorer(df)
## st.dataframe(filtered_df)

st.write("C'est un choix éditorial de garder en anglais les noms de colonnes.'")

fig = px.sunburst(df, path=['Year','Platform'], values='Global_Sales' )
st.write("## Ventes de jeux vidéo par year, par platform")
st.write("Sunburst")
fig

st.write("La treemap est une alternative au classique camembert.")
st.write("On voit ici que la même data peut être visualisée sous différents angles.")

treemap1 = px.treemap(df, path=[px.Constant("all"), 'Year','Platform'], values='Global_Sales',  labels='Year',hover_name="Year")
treemap1

st.write("## Ventes de jeux vidéo par Publisher,Genre and Platform")
treemap2 = px.treemap(df, path=[px.Constant("all"), 'Publisher','Genre'], values='Global_Sales', labels='Year',hover_name="Year")
treemap2

st.write("## Ventes de jeux vidéo par Genre and Year + platform")
treemap3 = px.treemap(df, path=[px.Constant("all"),'Genre','Year','Platform'], values='Global_Sales', labels='Year',hover_name="Year")
treemap3

st.write("## Ventes de jeux vidéo par platform, year")
treemap4 = px.treemap(df, path=[px.Constant("all"),'Platform','Year'], values='Global_Sales',labels='Year',hover_name="Year")
treemap4
