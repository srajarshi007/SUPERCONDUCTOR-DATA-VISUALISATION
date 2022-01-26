# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:23:08 2021

@author: RAJARSHI SAHA
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output 
from dash.dependencies import Input, Output


# data = pd.read_csv('C:/Users\RAJARSHI SAHA\OneDrive/Desktop/VIT FALL SEM 21-22/DATA VIZ/PROJECT/train.csv')
new_data = pd.read_csv('../Datasets/materials.csv')
mat_df=new_data
# alkali_list=[list(mat_df.columns)[2],list(mat_df.columns)[10],list(mat_df.columns)[18],list(mat_df.columns)[36],list(mat_df.columns)[54]]
# alkaline_list=[list(mat_df.columns)[3],list(mat_df.columns)[11],list(mat_df.columns)[19],list(mat_df.columns)[37],list(mat_df.columns)[55]]
# transition_list=(list(mat_df.columns)[20:29])+(list(mat_df.columns)[38:47])+(list(mat_df.columns)[71:79])
# posttransition_list=list(mat_df.columns)[12:13]+list(mat_df.columns)[29:31]+list(mat_df.columns)[47:50]+list(mat_df.columns)[79:85]
# lantha_list=list(mat_df.columns)[56:71]
# metalloids_list=list(mat_df.columns)[4:5]+list(mat_df.columns)[13:14]+list(mat_df.columns)[31:33]+list(mat_df.columns)[50:52]
# nonmetals_list=list(mat_df.columns)[0:1]+list(mat_df.columns)[5:9]+list(mat_df.columns)[14:17]+list(mat_df.columns)[33:35]+list(mat_df.columns)[52:53]
# noble_list=[list(mat_df.columns)[1],list(mat_df.columns)[9],list(mat_df.columns)[17],list(mat_df.columns)[35],list(mat_df.columns)[53],list(mat_df.columns)[85]]
# mat_df['alkali_metals']=mat_df[alkali_list].sum(axis=1)
# mat_df['alkaline_earth_metals']=mat_df[alkaline_list].max(axis=1)
# mat_df['transition_metals']=mat_df[transition_list].max(axis=1)
# mat_df['posttransition_metals']=mat_df[posttransition_list].max(axis=1)
# mat_df['lanthanoid_metals']=mat_df[lantha_list].max(axis=1)
# mat_df['metalloids']=mat_df[metalloids_list].max(axis=1)
# mat_df['reactive_nonmetals']=mat_df[nonmetals_list].max(axis=1)
# mat_df['noble_gases']=mat_df[noble_list].max(axis=1)
# # for i in range(0,21263):
# #     for j in alkali_list:
# #         if(mat_df.iloc[i,88]!=0):
# #             if(mat_df[j][i]==mat_df.iloc[i,88]):
# #                 mat_df.iloc[i,88]=j
# # # print(mat_df.iloc[:,88])
# # for i in range(0,21263):
# #     for j in alkaline_list:
# #         if(mat_df.iloc[i,89]!=0):
# #             if(mat_df[j][i]==mat_df.iloc[i,89]):
# #                 mat_df.iloc[i,89]=j
# # # print(mat_df.iloc[:,89])
# for i in range(0,21263):
#     for j in transition_list:
#         if(mat_df.iloc[i,90]!=0):
#             if(mat_df[j][i]==mat_df.iloc[i,90]):
#                 mat_df.iloc[i,90]=j
                
# for i in range(0,21263):
#     for j in posttransition_list:
#         if(mat_df.iloc[i,91]!=0):
#             if(mat_df[j][i]==mat_df.iloc[i,91]):                                                                        
#                 mat_df.iloc[i,91]=j
                
# # for i in range(0,21263):
# #     for j in lantha_list:
# #         if(mat_df.iloc[i,92]!=0):
# #             if(mat_df[j][i]==mat_df.iloc[i,92]):
# #                 mat_df.iloc[i,92]=j
                
# # for i in range(0,21263):
# #     for j in metalloids_list:
# #         if(mat_df.iloc[i,93]!=0):
# #             if(mat_df[j][i]==mat_df.iloc[i,93]):
# #                 mat_df.iloc[i,93]=j
                
# for i in range(0,21263):
#     for j in nonmetals_list:
#         if(mat_df.iloc[i,94]!=0):
#             if(mat_df[j][i]==mat_df.iloc[i,94]):
#                 mat_df.iloc[i,94]=j
# mat_df['tc_quantile']=pd.qcut(mat_df['critical_temp'],q=5,labels=["very low critical temp(< 4 K)","low critical temp(< 12 K)","moderate critical temp(< 32 K)","high critical temp(< 74 K)","very high critical temp(< 185 K)"],precision=0)
# print(mat_df.iloc[:,88:95])

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

materials2 = html.Div([
    html.H1("Distribution of critical temperatures of superconductors according to their constituent materials", style={'text-align': 'center'}),
    html.B(html.P("Select Element Group:")),

    dcc.Checklist(id='x-axis',
                  # options=[{'value': x, 'label': x} 
                  # for x in ['alkali_metals', 'alkaline_earth_metals', 'transition_metals', 'posttransition_metals','lanthanoid_metals','metalloids','reactive_nonmetals']],
                    options=[
                        {"label": "Alkali Metals", "value": "alkali_metals"},
                        {"label": "Alkaline Earth Metals", "value": "alkaline_earth_metals"},
                        {"label": "Transition Metals", "value": "transition_metals"},
                        {"label": "Post-transition Metals", "value": "posttransition_metals"},
                        {"label": "Lanthanoid Metals", "value": "lanthanoid_metals"},
                        {"label": "Metalloids", "value": "metalloids"},
                        {"label": "Nonmetals", "value": "reactive_nonmetals"}],
                  # multi=False,
                  # disabled=False,
                  # clearable=False,
                  # value="reactive_nonmetals",
                  # style={'width': "40%"}
                    value=["reactive_nonmetals"],
                    labelStyle={'display': 'inline-block'}
                  ),
    
    html.B(html.P("Y-Axis:")),
    
    dcc.RadioItems(
        id='y-axis', 
        options=[{'value': "critical_temp", 'label': "Critical Temperature"}],
                  # for x in ['total_bill', 'tip', 'size']],
        value="critical_temp", 
        labelStyle={'display': 'inline-block'}
    ),


    # html.Div(id='output_container', children=[]),
    # html.Br(),
    dcc.Graph(id='box-plot')
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
    materials2
])

@app.callback(
    Output("box-plot","figure"),
    [Input("x-axis", "value"), 
      Input("y-axis", "value"),])

def generate_chart(x,y):
    # print(option_slctd)
    # print(type(option_slctd))

    # container = "The Periodic Class chosen was: {}".format(option_slctd)


    # Plotly Express
    fig = px.box(mat_df, x = x, y = y)
    fig.update_xaxes(title_text='Elements')
    fig.update_yaxes(title_text='Critical Temperature')
    return fig

# if __name__ == '__main__':
app.run_server(debug=True,port=8054)