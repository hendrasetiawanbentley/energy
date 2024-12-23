import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Dummy data for the dashboard
data_bar = {
    "Date": ["Jan 1", "Jan 2", "Jan 3", "Jan 4", "Jan 5", "Jan 6"],
    "Website Blog": [400, 300, 200, 500, 700, 600],
    "Social Media": [200, 250, 300, 400, 350, 300],
}
data_pie = {
    "Category": ["Income", "Expenses", "Savings"],
    "Value": [75, 15, 10],
}
data_df_bar = pd.DataFrame(data_bar)
data_df_pie = pd.DataFrame(data_pie)

# Example charts
fig_bar = px.bar(data_df_bar, x="Date", y=["Website Blog", "Social Media"], title="Traffic Sources")
fig_pie = px.pie(data_df_pie, names="Category", values="Value", title="Income Distribution")

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    # Top Navigation Bar
    html.Div([
        html.Div("Gentelella-style Dashboard", className="navbar-brand"),
        html.Ul([
            html.Li(html.A("Home", href="#")),
            html.Li(html.A("Support", href="#")),
            html.Li(html.A("Reports", href="#")),
        ], className="navbar-menu")
    ], className="navbar"),

    # Dashboard Content
    html.Div([
        # Metrics Row
        html.Div([
            html.Div([
                html.H3("234"),
                html.P("New Accounts"),
            ], className="metric-card"),
            html.Div([
                html.H3("71%"),
                html.P("Total Expenses"),
            ], className="metric-card"),
            html.Div([
                html.H3("$1.45M"),
                html.P("Company Value"),
            ], className="metric-card"),
            html.Div([
                html.H3("+34"),
                html.P("New Employees"),
            ], className="metric-card"),
        ], className="metrics-row"),

        # Chart Section
        html.Div([
            html.Div([
                dcc.Graph(figure=fig_bar),
            ], className="chart-box"),
            html.Div([
                dcc.Graph(figure=fig_pie),
            ], className="chart-box"),
        ], className="chart-row"),

    ], className="dashboard-container"),
])

# Add Gentelella-style CSS
app.index_string = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #F7F7F7;
        }
        .navbar {
            width: 100%;
            background-color: #2A3F54;
            color: white;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .navbar-menu {
            list-style-type: none;
            display: flex;
            margin: 0;
            padding: 0;
        }
        .navbar-menu li {
            margin-left: 20px;
        }
        .navbar-menu li a {
            color: white;
            text-decoration: none;
        }
        .dashboard-container {
            padding: 20px;
        }
        .metrics-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .metric-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            width: 22%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .chart-row {
            display: flex;
            justify-content: space-between;
            gap: 20px;
        }
        .chart-box {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            width: 48%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div id="react-entry-point"></div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run_server(debug=True)
