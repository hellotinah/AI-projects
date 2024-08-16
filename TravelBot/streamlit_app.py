import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

# Load the updated itinerary events CSV file with coordinates
itinerary_df = pd.read_csv("itinerary_events_with_coordinates.csv")

# Streamlit app
st.title('Travel Itinerary Dashboard')

# Display the itinerary events
st.header('Itinerary Events 🐢')
st.dataframe(itinerary_df)

# Sidebar filters
st.sidebar.header('Filters')
selected_category = st.sidebar.multiselect(
    'Select Category',
    options=itinerary_df['category'].unique(),
    default=itinerary_df['category'].unique()
)

# Filter dataframe based on selected categories
filtered_df = itinerary_df[itinerary_df['category'].isin(selected_category)]

# Group events by category
grouped = filtered_df.groupby('category')

# Display grouped categories
st.header('Grouped Categories ⛰️')
for category, events in grouped:
    st.subheader(category)
    st.write(events)

# Display a bar chart of events by category
st.header('Events by Category')
category_counts = filtered_df['category'].value_counts()
st.bar_chart(category_counts)

# Display a pie chart of events by category
st.header('Events Distribution by Category')
fig, ax = plt.subplots()
ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Display a Google Map with markers
st.header('View on Map 📍')

# Prepare data for JavaScript
locations = filtered_df[['latitude', 'longitude', 'location']].dropna()

# Convert the DataFrame to a JSON string for use in JavaScript
locations_json = locations.to_json(orient='records')

# Create the Google Maps HTML
map_html = f"""
<html>
<head>
    <script src="https://maps.googleapis.com/maps/api/js?key=your_geocoding_api_key_here"></script>
    <script>
        var locations = {locations_json};
        function initMap() {{
            var map = new google.maps.Map(document.getElementById('map'), {{
                center: {{lat: 49.2827, lng: -123.1207}}, // Centered at Vancouver for initial load
                zoom: 4
            }});
            
            locations.forEach(function(location) {{
                new google.maps.Marker({{
                    position: {{lat: location.latitude, lng: location.longitude}},
                    map: map,
                    title: location.location
                }});
            }});
        }}
    </script>
</head>
<body onload="initMap()">
    <div id="map" style="height: 600px; width: 100%;"></div>
</body>
</html>
"""

# Embed the HTML in Streamlit
components.html(map_html, height=600)

# Optional: Provide a link to open Google Maps
st.write("You can also view the map directly on [Google Maps](https://www.google.com/maps).")
