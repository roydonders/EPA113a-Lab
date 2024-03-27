import pandas as pd
import plotly.graph_objects as go

file_name = '../data/ass3_final_n1_network.csv'

# Sample DataFrame
data = {
    'road': ['A', 'A', 'B', 'B', 'B'],
    'lat': [51.1, 51.2, 52.0, 52.1, 52.2],
    'lon': [4.5, 4.6, 4.7, 4.8, 4.9]
}
df = pd.read_csv(file_name
                 )
# Create a figure with scatter plot
fig = go.Figure()

# Add scatter plot for each road
for road, group in df.groupby('road'):
    fig.add_trace(go.Scattermapbox(
        lon=group['lon'],
        lat=group['lat'],
        mode='lines+markers',
        name=road,
        hovertext=group['id'],
        marker=dict(size=10),
        line=dict(width=2),
    ))

# Update layout for mapbox
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox=dict(
        zoom=10,
        center=dict(lat=df['lat'].mean(), lon=df['lon'].mean()),
    ),
)

# Show figure
fig.show()
