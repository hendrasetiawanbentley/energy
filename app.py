import dash
from dash import html

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server  # Expose the Flask server for deployment

# Define the layout
app.layout = html.Div(
    children=[
        html.H1("Hello, World!", style={"textAlign": "center", "color": "blue"}),
        html.P("Welcome to your first Dash app!", style={"textAlign": "center"}),
    ]
)

# Run the app locally
if __name__ == "__main__":
    app.run_server(debug=True)
