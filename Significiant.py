import streamlit as st
import pandas as pd
import folium

# Titre de l'application
st.title("Carte Interactive des Séismes en France")

# Charger les données directement depuis le fichier fourni
file_path = 'data_france (1).csv'
data = pd.read_csv(file_path)

# Aperçu des données
data_france = data[data['state'] == 'France']
st.write("Aperçu des données en France :", data_france.head())

# Vérifier que des données existent pour la France
if data_france.empty:
    st.warning("Aucune donnée trouvée pour la France.")
else:
    st.success(f"{len(data_france)} données trouvées pour la France.")

    # Créer une carte centrée sur la France
    france_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

    # Filtrer selon la colonne 'significance'
    low_significance = data_france[data_france['significance'] < 50]
    medium_significance = data_france[(data_france['significance'] >= 50) & (data_france['significance'] < 150)]
    high_significance = data_france[data_france['significance'] >= 150]

    # Ajouter les couches pour chaque catégorie
    low_layer = folium.FeatureGroup(name="Significance < 50").add_to(france_map)
    for _, row in low_significance.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=2,
            color='green',
            fill=True,
            fill_color='green',
            fill_opacity=0.6
        ).add_to(low_layer)

    medium_layer = folium.FeatureGroup(name="Significance 50-150").add_to(france_map)
    for _, row in medium_significance.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            color='orange',
            fill=True,
            fill_color='orange',
            fill_opacity=0.6
        ).add_to(medium_layer)

    high_layer = folium.FeatureGroup(name="Significance >= 150").add_to(france_map)
    for _, row in high_significance.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6
        ).add_to(high_layer)

    folium.LayerControl().add_to(france_map)

    # Afficher la carte avec Streamlit
    st.subheader("Carte des séismes :")
    folium_static(france_map)
