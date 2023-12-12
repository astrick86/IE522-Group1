import folium
import pandas as pd
from selenium import webdriver

# Load your CSV file (replace 'your_file.csv' with your actual file name)
data = pd.read_csv('/data_loc.csv')


# Create a folium map centered at the mean latitude and longitude
map_center = [data['latitude'].mean(), data['longitude'].mean()]
map_zoom = 7
mymap = folium.Map(location=map_center, zoom_start=map_zoom)

# Define a color map for categories
category_colors = {
    'selected hubs': 'blue',
    'selected plants': 'green',
    'Not selected plants': 'white',
    'Not selected hubs': 'white',
    # Add more categories as needed
}

def add_marker(row):
    category = row['status']
    location = [row['latitude'], row['longitude']]
    icon_color = category_colors.get(category, 'blue')  # Default to blue if category not found
    label = f"{category}"
    
    # Create a marker with a label
    marker = folium.Marker(location, icon=folium.Icon(color=icon_color))
    
    # Create a marker with a label using DivIcon
    icon = folium.DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html=f'<div style="font-size: 10pt; color : {icon_color};">{label}</div>'
    )
    
    folium.Marker(location, icon=folium.Icon(color=icon_color)).add_to(mymap)

# Apply the function to each row in the DataFrame
data.apply(add_marker, axis=1)

# Save the map as an HTML file
html_file = 'map_visualization_sol.html'
mymap.save(html_file)