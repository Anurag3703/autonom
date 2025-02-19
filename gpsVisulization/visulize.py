import folium
import json


city_coordinates = [47.5289, 21.6254]
m = folium.Map(location=city_coordinates, zoom_start=12)


with open("roads.geojson", "r") as f:
    geojson_data = json.load(f)


def road_style(feature):

    condition = feature['properties']['condition']
    if condition == "Good":
        return {"color": "green", "weight": 20, "opacity": 0.7}
    elif condition == "Fair":
        return {"color": "orange", "weight": 4, "opacity": 0.7}
    else:
        return {"color": "red", "weight": 4, "opacity": 0.7}


folium.GeoJson(
    geojson_data,
    name="roads",
    style_function=road_style
).add_to(m)


m.save("colored_streets_map.html")
