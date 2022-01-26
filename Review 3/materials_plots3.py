import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output 
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd

new_data = pd.read_csv('../Datasets/materials.csv')
df1=new_data
mat_data = pd.read_csv('../Datasets/unique_m.csv')
mat_df=mat_data
alkali_list=[list(mat_df.columns)[2],list(mat_df.columns)[10],list(mat_df.columns)[18],list(mat_df.columns)[36],list(mat_df.columns)[54]]
alkaline_list=[list(mat_df.columns)[3],list(mat_df.columns)[11],list(mat_df.columns)[19],list(mat_df.columns)[37],list(mat_df.columns)[55]]
transition_list=(list(mat_df.columns)[20:29])+(list(mat_df.columns)[38:47])+(list(mat_df.columns)[71:79])
posttransition_list=list(mat_df.columns)[12:13]+list(mat_df.columns)[29:31]+list(mat_df.columns)[47:50]+list(mat_df.columns)[79:85]
lantha_list=list(mat_df.columns)[56:71]
metalloids_list=list(mat_df.columns)[4:5]+list(mat_df.columns)[13:14]+list(mat_df.columns)[31:33]+list(mat_df.columns)[50:52]
nonmetals_list=list(mat_df.columns)[0:1]+list(mat_df.columns)[5:9]+list(mat_df.columns)[14:17]+list(mat_df.columns)[33:35]+list(mat_df.columns)[52:53]
noble_list=[list(mat_df.columns)[1],list(mat_df.columns)[9],list(mat_df.columns)[17],list(mat_df.columns)[35],list(mat_df.columns)[53],list(mat_df.columns)[85]]
mat_df['alkali_metals_coeff']=mat_df[alkali_list].max(axis=1)
mat_df['alkaline_earth_metals_coeff']=mat_df[alkaline_list].max(axis=1)
mat_df['transition_metals_coeff']=mat_df[transition_list].max(axis=1)
mat_df['posttransition_metals_coeff']=mat_df[posttransition_list].max(axis=1)
mat_df['lanthanoid_metals_coeff']=mat_df[lantha_list].max(axis=1)
mat_df['metalloids_coeff']=mat_df[metalloids_list].max(axis=1)
mat_df['reactive_nonmetals_coeff']=mat_df[nonmetals_list].max(axis=1)
# mat_df['noble_gases']=mat_df[noble_list].max(axis=1)
df2=mat_df.iloc[:,88:95]
frames =[df1,df2]
df = pd.concat(frames, axis=1, join='inner')
dict ={'alkali_metals':'alkali_metals_coeff', 'alkaline_earth_metals':'alkaline_earth_metals_coeff',
       'transition_metals':'transition_metals_coeff', 'posttransition_metals':'posttransition_metals_coeff', 'lanthanoid_metals':'lanthanoid_metals_coeff',
       'metalloids':'metalloids_coeff', 'reactive_nonmetals':'reactive_nonmetals_coeff'}

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

materials3 = html.Div([
    html.H1("Composition of superconductors in different critical temperature ranges", style={'text-align': 'center'}),

    dcc.Dropdown(id="option_slctd",
                  options=[
                      {"label": "Alkali Metals", "value": "alkali_metals"},
                      {"label": "Alkaline Earth Metals", "value": "alkaline_earth_metals"},
                      {"label": "Transition Metals", "value": "transition_metals"},
                      {"label": "Post-transition Metals", "value": "posttransition_metals"},
                      {"label": "Lanthanoid Metals", "value": "lanthanoid_metals"},
                      {"label": "Metalloids", "value": "metalloids"},
                      {"label": "Nonmetals", "value": "reactive_nonmetals"},
                      ],
                  multi=False,
                  disabled=False,
                  clearable=False,
                  value="reactive_nonmetals",
                  style={'width': "40%"}
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
    materials3
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
      Output(component_id='explore', component_property='figure')],
    [Input(component_id='option_slctd', component_property='value')]
)

def update_graph(option_slctd):
    # print(option_slctd)
    # print(type(option_slctd))

    container = "The Periodic Class chosen was: {}".format(option_slctd)

    # Plotly Express
    fig = px.box(df, x = option_slctd, y = dict[option_slctd], color="tc_quantile", labels={"tc_quantile":"Critical Temperature Range"})
    fig.update_yaxes(title_text="Stoichiometric_coefficients")
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True,port=8055)

