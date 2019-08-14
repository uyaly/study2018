import folium
from folium import plugins
heatmap1 = folium.Map(location=[28.12, 112.59], zoom_start=11)
heatmap1.add_children(plugins.HeatMap([[row["lat"],row["lon"]] for name, row in df1.iterrows()]))
heatmap1.save("map.html")
heatmap1