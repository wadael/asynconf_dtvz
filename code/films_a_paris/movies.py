import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

import plotly.express as px

#
# Example d'utilisation de cartes avec Streamlit. 
# 
#

@st.cache_data
def getData():
    df = pd.read_csv("lieux-de-tournage-a-paris.csv", sep=';')  # ,nrows=50
    df['lon'] = df['Coordonnée en X']
    df['lat'] = df['Coordonnée en Y']
    return df

st.set_page_config(
    page_title="Tournages à Paris ", page_icon="🚅", layout='wide'
)

st.write("# Tournages à Paris")

df= getData()
df2 = df[["Identifiant du lieu", "Titre", "Réalisateur", "Producteur", "lat", "lon"]]
df2.dropna(axis=1)
df2=df2.head(1000)

conditions = [
        (df['Type de tournage'] == 'Long Métrage') ,
        (df['Type de tournage'] == 'Téléfilm') ,
        (df['Type de tournage'] == 'Ssérie TV')
]

values = ['blue', 'beige', 'pink']
df['colour'] = np.select(conditions, values)

col1, col2 = st.columns(2)

with col1:
    st.write("## Ici on utilise df")
    fig = px.density_mapbox(df, lat='lat', lon='lon', radius=5,
                            center=dict(lon= 2.349902, lat=48.852966 ), zoom=10,
                            mapbox_style="stamen-terrain", hover_data='Titre', color_continuous_scale=px.colors.sequential.Hot)
    fig


with col2:
    st.write("## Ici on utilise df2")
    st.write("Mille marqueurs semble être une limite ")

    st.write("there is " + str(len(df2)) + " locations")

    with st.expander("data", expanded=False):
        df2
    with st.expander("types", expanded=False):
        st.write(df2.dtypes)

    st.write("## Default st.map widget")
    st.map(df2, zoom=12, use_container_width=True)

    st.write("## Folium map (patience) ")

    map = folium.Map(
        location=[df2.iloc[[1]]['lat'], df2.iloc[[1]]['lon']],
        zoom_start=12, width='80%', height='80%', left='0%', top='0%'
    )

    for ind in range(len(df2)):
        txt = "" + str(df2.iloc[[ind]]['Titre'].to_string(index=False)) + "\n\n" + str( df2.iloc[[ind]]['Réalisateur'].to_string(index=False)) + "\n" + str(df.iloc[[ind]]['Producteur'].to_string(index=False))
        coul = 'red' # "" + str(df.iloc[[ind]]['colour'].to_string(index=False))
        ic = folium.Icon(color=coul, icon='camera', prefix='fa')

        folium.Marker(
             [df.iloc[[ind]]['lat'], df.iloc[[ind]]['lon']],
             popup=str(txt),
             tooltip=str(df.iloc[[ind]]['Titre'].to_string(index=False))
             , icon=ic
             , color=coul
        ).add_to(map)

    st_data = st_folium(map)



