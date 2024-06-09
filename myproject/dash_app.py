from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd
from dash import html, dcc

# Create Dash app
app = DjangoDash('SimpleExample', external_scripts=['https://cdn.plot.ly/plotly-basic-2.12.1.min.js'])

# Sample data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Set the layout
app.layout = html.Div(style={'height': '100vh', 'width': '100vw', 'display': 'flex', 'flexDirection': 'column'}, children=[
    html.H1(children='Hello Dash', style={'flex': '0 1 auto'}),

    html.Div(children='Dash: A web application framework for Python.', style={'flex': '0 1 auto'}),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'flex': '1 1 auto', 'height': '100%', 'width': '100%'}  # Ensures the graph takes full width and height
    )
])
