import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html, Input, Output 

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


# df = px.data.tips()
# fig = px.strip(df, y="total_bill", x="day",orientation='h')

df = pd.read_csv('../Datasets/train.csv')

properties2 = html.Div([
    html.H1("Analysis of the Most Dominant Properties", style={'text-align': 'center'}),

    dcc.Dropdown(id="property",
                 options=[
                     {"label": "Weighted Geometric Mean of Valence", "value": "wtd_gmean_Valence"},
                     {"label": "Range of Thermal Conductivity", "value": "range_ThermalConductivity"},
                     {"label": "Fusion Heat Entropy", "value": "entropy_FusionHeat"},
                     {"label": "Entropy of Electron Affinity", "value": "entropy_ElectronAffinity"},
                     {"label": "Geometric Mean of Density", "value": "gmean_Density"},
                     {"label": "Range of First Ionization Enthalpy", "value": "range_fie"},
                     {"label": "Weighted Entropy of Atomic Mass", "value": "wtd_entropy_atomic_mass"},
                     {"label": "Number of constituent elements", "value": "number_of_elements"},
                     ],
                 multi=False,
                 disabled=False,
                 clearable=False,
                 value="range_ThermalConductivity",
                 style={'width': "60%"}
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
    properties2
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='explore', component_property='figure')],
    [Input(component_id='property', component_property='value')]
)

def update_graph(option_slctd):
    dff = df[['critical_temp',option_slctd]]

    container = "The property chosen by user was: {}".format(option_slctd)

    
    if(option_slctd=='number_of_elements'):
        a = pd.qcut(dff[option_slctd], q=6, precision = 0,duplicates='drop').astype('str')
        temp = pd.DataFrame({'count':a.value_counts()})
        temp = temp.sort_values('count')
        fig=px.bar(data_frame=temp,
        y='count',
        color=temp.index,
        labels={'index':'Quantiles'},)
        fig.update_yaxes(title_text="Critical Temperature")
        fig.update_xaxes(title_text="Number of constituent elements")
        fig.update_layout(
        title={
            'text': "Almost linear increase of constituent elements with critical temperature, and most materials consist of 5 to 9 atoms.",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom'
        })    
    else:
        dff['a'] = pd.qcut(dff[option_slctd], q=10, precision = 0,duplicates='drop').astype('str')
        dff['b'] = dff['a'].value_counts()
        dff = dff.sort_values('a')
        # Plotly Express
        fig = px.strip(data_frame=dff,
            x= dff.a, y='critical_temp',
            color=dff.a, 
            labels={'a':'Quantiles'},
            # facet_col="a"
            # hover_data=['State', 'Pct of Colonies Impacted'],
            # color_continuous_scale=px.colors.sequential.YlOrRd,
            # labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
            # template='plotly_dark'
            )
        fig.update_yaxes(title_text="Critical Temperature")
        if(option_slctd=='wtd_gmean_Valence'):
            fig.update_xaxes(title_text="Weighted Geometric Mean of Valence")
            fig.update_layout(
            title={
                'text': "Weighted geometric mean of valence shows an almost linear decrease, consistent with the negative correlation coefficient obtained.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            }) 
        elif(option_slctd=='range_ThermalConductivity'):
            fig.update_xaxes(title_text="Range of Thermal Conductivity")
            fig.update_layout(
            title={
                'text': "Thermal conductivity shows an almost linear increase, consistent with the positive correlation coefficient obtained.<br>We also notice the high concentration of thermal conductivities in the (399.8 400.0] quantile.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            })
        elif(option_slctd=='entropy_FusionHeat'):
            fig.update_xaxes(title_text="Entropy of Fusion Heat")
            fig.update_layout(
            title={
                'text': "Almost linear increase for fusion heat entropy, consistent with the positive correlation coefficient obtained for it.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            })
        elif(option_slctd=='entropy_ElectronAffinity'):
            fig.update_xaxes(title_text="Entropy of Electron Affinity")
            fig.update_layout(
            title={
                'text': "Almost linear increase for entropy of electron affinity with critical temperature.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            })        
        elif(option_slctd=='gmean_Density'):
            fig.update_xaxes(title_text="Geometric Mean of Density")
            fig.update_layout(
            title={
                'text': "Almost linear decrease, consistent with the negative correlation coefficient obtained.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            })
        elif(option_slctd=='range_fie'):
            fig.update_xaxes(title_text="Range of First Ionization Enthalpy")
            fig.update_layout(
            title={
                'text': "Almost linear increase and most superconductors have first ionization enthalpies <br> in the 528 kJ to 811 kJ, evident from the stripplot distribution.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            })
        elif(option_slctd=='wtd_entropy_atomic_mass'):
            fig.update_xaxes(title_text="Weighted Entropy of Atomic Mass")
            fig.update_layout(
            title={
                'text': "Almost linear increase of atomic mass with increase in critical temperature, <br> consistent with the positive correlation coefficient obtained.",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'
            })                                               
        # fig.update_yaxes(title_text="Critical Temperature")
        # fig.update_xaxes(title_text="Weighted Geometric Mean of Variance")
        # fig.update_layout(
        #     title={
        #         'text': "Weighted geometric mean of valence shows an almost linear decrease, consistent with the negative correlation coefficient obtained.",
        #         'y':0.95,
        #         'x':0.5,
        #         'xanchor': 'center',
        #         'yanchor': 'top'
        #     })

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True,port=8052)