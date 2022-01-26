import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#483d8b",
}

# padding for the page content
CONTENT_STYLE = {
    # "background-color": "#d8bfd8",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# # padding for the page content
# LINK_STYLE = {
#     # "background-color": "#d8bfd8",
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "margin-top": "2rem",
#     "text-decoration": "none",
#     "color": "#000000",
#     "padding": "2rem 1rem"
# }

# A = {
#     "text-decoration": "none",
#     "color": "#000000",
# }

# # padding for the page content
# LINK_STYLE:HOVER = {
#     # "background-color": "#d8bfd8",
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "margin-top": "20rem",
#     "text-decoration": "none",
#     "color": "#000000",
#     "padding": "2rem 1rem",
# }

sidebar = html.Div(
    [
        html.B(html.H2("Menu", className="display-4",style={'color':"white"})),
        html.Hr(),
        html.P(
            "Superconductors - Interactive Dashboard", className="lead",style={'color':"white"}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="http://127.0.0.1:8050/", active="exact",style={'color':"white"}),
                dbc.NavLink("Property Visualization 1", href="http://127.0.0.1:8051/", active="exact",style={'color':"white"}),
                dbc.NavLink("Property Visualization 2", href="http://127.0.0.1:8052/", active="exact",style={'color':"white"}),
                dbc.NavLink("Material Visualization 1", href="http://127.0.0.1:8053/", active="exact",style={'color':"white"}),
                dbc.NavLink("Material Visualization 2", href="http://127.0.0.1:8054/", active="exact",style={'color':"white"}),
                dbc.NavLink("Material Visualization 3", href="http://127.0.0.1:8055/", active="exact",style={'color':"white"}),
                dbc.NavLink("Material Visualization 4", href="http://127.0.0.1:8056/", active="exact",style={'color':"white"}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# link = html.Div([
#     html.A("Link to external site", href='http://127.0.0.1:8051/', target="_blank")
# ],style=LINK_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Data Visualization Project: CSE-3020',
                        style={'textAlign':'center'}),
                html.Br(),
                html.Hr(),
                html.H3('Group 23'),
                html.H5('Mayukh Mondal: 20BCT0133'),
                html.H5('Rajarshi Saha: 20BCT0163'),
                html.H5('Parth Chaudhary: 15BCE2044'),
                html.Br(),
                html.Br(),
                html.P("We explore the different chemical properties of superconductors, and analyze these records to better understand any underlying trends. These trends, as presented in this dashboard, reveal certain interesting patterns about the composition and nature of superconductors."),
                html.Br(),
                html.P("We have made use of the Superconductors Dataset from the UCI Machine Learning Repository. It is sourced from:"),
                html.I("Hamidieh, Kam, A data-driven statistical model for predicting the critical temperature of a superconductor, Computational Materials Science, Volume 154, November 2018, Pages 346-354."),
                
                ]
    elif pathname == "/page-1":
        return [
                html.H1('Inspection of trends of properties with critical temperature',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df1, barmode='group', x='Years',
                         y=['Girls Grade School', 'Boys Grade School']))
                ]
    elif pathname == "/page-2":
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df1, barmode='group', x='Years',
                         y=['Girls High School', 'Boys High School']))
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__=='__main__':
    app.run_server(debug=True, port=8050)