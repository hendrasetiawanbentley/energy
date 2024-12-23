import dash
from dash import html

# Create the Dash app
app = dash.Dash(__name__)
server = app.server


# Define the layout
app.layout = html.Div([
    html.H1("Hello, World!", style={"textAlign": "center"}),
    html.P("This is a simple Dash app.", style={"textAlign": "center"})
])

if __name__ == '__main__':
    app.run_server(debug=False)
