import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html, Input, Output 

import numpy as np
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('../Datasets/train.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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

properties1 = html.Div([
    html.H1("Preliminary Investigation of Trends", style={'text-align': 'center'}),
    html.Br(),
    html.P("Choose the property for visualization:"),
    dcc.Dropdown(id="property",
                 options=[
                     {"label": "Favourable temperature", "value": "mean_atomic_mass"},
                     {"label": "Ionization Enthalpy", "value": "mean_fie"},
                     {"label": "Atomic Radius", "value": "mean_atomic_radius"},
                     {"label": "Mean Density", "value": "mean_Density"},
                     {"label": "Mean Fusion Heat", "value": "mean_FusionHeat"},
                     {"label": "Mean Thermal Conductivity", "value": "mean_ThermalConductivity"},
                     {"label": "Mean Valence", "value": "mean_Valence"},
                     ],
                 multi=False,
                 disabled=False,
                 clearable=False,
                 value="mean_atomic_mass",
                 style={'width': "50%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='explore', figure={})
],style=CONTENT_STYLE)

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

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
    properties1
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='explore', component_property='figure')],
    [Input(component_id='property', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The property chosen by user was: {}".format(option_slctd)

    dff = df[['critical_temp',option_slctd]]
    dff = dff.sort_values('critical_temp')

    # Plotly Express
    fig = px.line(dff,
        x = "critical_temp", y=option_slctd,
        # hover_data=['State', 'Pct of Colonies Impacted'],
        # color_continuous_scale=px.colors.sequential.YlOrRd,
        # labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
        )
    fig.update_xaxes(title_text="Critical Temperature")
    if(option_slctd=='mean_atomic_mass'):
        fig.update_yaxes(title_text="Mean Atomic Mass")
        fig.update_layout(
        title={
            'text': "Heavier atoms constitute superconductors that operate at lower temperatures only. <br>As the temperatures rise above 130K, the atomic size steadily drops.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        }) 
    elif(option_slctd=='mean_fie'):
        fig.update_yaxes(title_text="Mean of First Ionization Enthalpy")
        fig.update_layout(
        title={
            'text': "Lower ionization enthalpies at lower temperatures, rises steadily above 130 K.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })
    elif(option_slctd=='mean_atomic_radius'):
        fig.update_yaxes(title_text="Mean Atomic Radius")
        fig.update_layout(
        title={
            'text': "Larger atoms constitute superconductors that operate at lower temperatures only. <br> As the temperatures rise above 130K, the atomic size steadily drops.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })
    elif(option_slctd=='mean_Density'):
        fig.update_yaxes(title_text="Mean Density")
        fig.update_layout(
        title={
            'text': "Denser superconductors exist at lower critical temperatures.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })        
    elif(option_slctd=='mean_ElectronAffinity'):
        fig.update_yaxes(title_text="Mean of Electron Affinity")
        fig.update_layout(
        title={
            'text': "Non-metallic character, therefore, is visible in superconductors with high critical temperatures.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })
    elif(option_slctd=='mean_FusionHeat'):
        fig.update_yaxes(title_text="Mean Fusion Heat")
        fig.update_layout(
        title={
            'text': "At higher temperatures, superconductors readily change states on addition of heat.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })
    elif(option_slctd=='mean_ThermalConductivity'):
        fig.update_yaxes(title_text="Mean Thermal Conductivity")
        fig.update_layout(
        title={
            'text': "Thermal conductivity decreases with rise in critical temperature.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })
    elif(option_slctd=='mean_Valence'):
        fig.update_yaxes(title_text="Mean Valence")
        fig.update_layout(
        title={
            'text': "Valence decreases slightly, before increasing again.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })    
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True,port=8051)