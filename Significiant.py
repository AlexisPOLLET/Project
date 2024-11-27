import pandas as pd
import matplotlib.pyplot as plt
import folium

print(max(data_france['significance']))
print(min(data_france['significance']))
# Vérifier que des données existent pour la France
if data_france.empty:
    print("Aucune donnée trouvée pour la France.")
else:
    # Créer une carte centrée sur la France
    france_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

low_significance = data_france[data_france['significance'] < 50]
medium_significance = data_france[(data_france['significance'] >= 50) & (data_france['significance'] < 150)]
high_significance = data_france[data_france['significance'] >= 150]

# Ajouter une couche pour les séismes de faible significance
low_layer = folium.FeatureGroup(name="significance < 50").add_to(france_map)
for _, row in low_significance.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=2,
        color='green',
        fill=True,
        fill_color='green',
        fill_opacity=0.6
    ).add_to(low_layer)

# Ajouter une couche pour les séismes de moyenne significance
medium_layer = folium.FeatureGroup(name="significance 50-150 ").add_to(france_map)
for _, row in medium_significance.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color='orange',
        fill=True,
        fill_color='orange',
        fill_opacity=0.6
    ).add_to(medium_layer)

# Ajouter une couche pour les séismes de forte magnitude
high_layer = folium.FeatureGroup(name="significance >= 150").add_to(france_map)
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
    # Afficher la carte
france_map
