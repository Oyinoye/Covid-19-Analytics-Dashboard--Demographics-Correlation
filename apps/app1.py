import dash
import dash_core_components as dcc
from dash_core_components.Link import Link
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dtb
from dash.dependencies import Input, Output

import pandas as pd
from datetime import datetime

import plotly
import plotly.graph_objects as go

from app import app

app.title = 'COVID-19'

dash_colors = {
    'background': '#dee9fa',
    'text': '#BEBEBE',
    'grid': '#333333',
    'red': '#BF0000',
    'blue': '#10274a',
    'green': '#5bc246'
}

# ------FRESH START---------

input_file_name_us = 'data/raw_data_csv/US Data_Case by county.csv'
input_file_name_us_demo = 'data/raw_data_csv/US_demographics_prepped.csv'
input_file_name_uk = 'data/raw_data_csv/UK Data_Case by region.csv'
input_file_name_uk_demo = 'data/raw_data_csv/UK Demographics 2020.csv'
input_file_name_sa = 'data/raw_data_csv/SA Data_Case by County.csv'

df_us = pd.read_csv(input_file_name_us)
df_uk = pd.read_csv(input_file_name_uk)
df_sa = pd.read_csv(input_file_name_sa)

table_head_sa = list(df_sa.columns.values)
table_head_uk = list(df_sa.columns.values)
table_head_us = list(df_sa.columns.values).pop()

df_us_demo = pd.read_csv(input_file_name_us_demo)
df_uk_demo = pd.read_csv(input_file_name_uk_demo)

df = df_us

# @app.callback(
#     Output('table-section', 'children'),
#     [Input('country-dropdown', 'value')])
# def updateTable(value):
#     table_df = df_us
#     table_head = table_head_us
#     if value == 'United States':
#         table_df = df_us
#         table_head = table_head_us
#     elif value == 'United Kingdom':
#         table_df = df_uk
#         table_head = table_head_uk
#     elif value == 'South Africa':
#         table_df = df_sa
#         table_head = table_head_sa
#     return [
#         dtb.DataTable(
#             data=table_df.to_dict('records'),
#             columns=[{'id': c, 'name': c} for c in table_df],
#             page_size=10
#         )
#     ]

layout = html.Div(style={'backgroundColor': dash_colors['background']}, children=[
    dbc.Navbar(
        [
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Link(
                                href='/',
                                refresh=False,
                                children=(
                                    html.H1(children='HOME', id='home-nav',
                                        style={
                                            'textAlign': 'center',
                                            'color': '#b5d3ff',
                                            'margin': 0,
                                            'padding': 10,
                                            'cursor': 'pointer',
                                            },      
                                    ),
                                ),
                                style={
                                    'textDecoration': 'none'
                                }
                            ),
                            
                        ),

                        dbc.Col(
                            dcc.Link(
                                href='/form',
                                refresh=False,
                                children=(
                                    html.H1(children='FORM', id='form-nav',
                                    style={
                                        'textAlign': 'center',
                                        'color': '#b5d3ff',
                                        'margin': 0,
                                        'padding': 10,
                                        'cursor': 'pointer'
                                        },      
                                    ),
                                ),
                                style={
                                    'textDecoration': 'none'
                                }
                            ),
                            style = {
                                'display': 'inline'
                            }
                        ),

                        dbc.Col(
                            dcc.Link(
                                href='/insights',
                                refresh=False,
                                children=(
                                    html.H1(children='INSIGHTS', id='insights-nav',
                                    style={
                                        'textAlign': 'center',
                                        'color': '#b5d3ff',
                                        'margin': 0,
                                        'padding': 10,
                                        'cursor': 'pointer'
                                        },      
                                    ),
                                ),
                                style={
                                    'textDecoration': 'none'
                                }
                            )
                        ),
                    ]
                ),
                fluid=True,
                style={
                    'color': '#e6f0ff',
                    'display':'inline',
                    'backgroundColor': dash_colors['blue'],
                }
            )
        ],
        sticky=True,
        style={
            'textAlign': 'center',
            'color': '#10274a',
            'backgroundColor': dash_colors['blue'],
            'marginTop': 0,
            'padding': 0,
        }
    ),
    html.H1(children='COVID-19 Comparison analysis across demographics for UK, US and SA',
        style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'marginTop': 40
            }
        ),

    
    html.Div(children='Select focus for the datatable, filter through for US, UK and SA:', style={
        'textAlign': 'center',
        'color': dash_colors['text']
        }),

    html.Div(
        dcc.Dropdown(
            id='country-dropdown',
            options=[
                {'label': '{}'.format(i), 'value': i} for i in [
                    'United States', 'United Kingdom', 'South Africa'
                ]
            ],
            value="United States",
        ),
    ),

    html.Div(id='datatable-section'),
    html.Div(id='datatable-interactivity-container'),

    html.Div(dcc.Markdown('''
        &nbsp;  
        &nbsp;  
        
        ### Visualization of Cases Across Regions
        '''),
        style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'width': '100%',
            'float': 'center',
            'display': 'inline-block'}
        ),

    html.Div(id='graph1', children=[
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': df_us["State"], 'y': df_us[" Cases "], 'type': 'bar', 'name': 'Cases'},
                    {'x': df_us["State"], 'y': list(df_us_demo["Total Minority Percentage"]), 'type': 'bar', 'name': u'Minority'},
                ],
                'layout': {
                    'title': 'Cases and Minority in US States (click the "cases" checkbox to toggle view))'
                }
            }
        )
    ]),

    html.Div(id='graph2', children=[
        dcc.Graph(
            id='example-graph2',
            figure={
                'data': [
                    {'x': df_uk_demo["Region"], 'y': df_uk_demo["Percentage minority ethnicities"], 'type': 'bar', 'name': 'Cases'},
                    # {'x': df_us["State"], 'y': list(df_us_demo["Total Minority Percentage"]), 'type': 'bar', 'name': u'Minority'},
                ],
                'layout': {
                    'title': 'Demographics and Cases in the UK (click the checkbox to toggle view))'
                }
            }
        )
    ]),

    html.Div(id='graph3', children=[
        dcc.Graph(
            id='example-graph3',
            figure={
                'data': [
                    {'x': df_sa["County"], 'y': df_sa["Total Cases "], 'type': 'bar', 'name': 'Cases'},
                    # {'x': df_us["State"], 'y': list(df_us_demo["Total Minority Percentage"]), 'type': 'bar', 'name': u'Minority'},
                ],
                'layout': {
                    'title': 'Cases in South Africa Regions (click the checkbox to toggle view))'
                }
            }
        )
    ]),

    # html.Div([
    #     dtb.DataTable(
    #         id='datatable-interactivity',
    #         columns=[
    #             {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
    #         ],
    #         data=df.to_dict('records'),
    #         editable=True,
    #         filter_action="native",
    #         sort_action="native",
    #         sort_mode="multi",
    #         column_selectable="single",
    #         row_selectable="multi",
    #         row_deletable=True,
    #         selected_columns=[],
    #         selected_rows=[],
    #         page_action="native",
    #         page_current= 0,
    #         page_size= 10,
    #     ),
    #     html.Div(id='datatable-interactivity-container')
    # ]),

])

# input_file_name_us = 'data/raw_data_csv/SA Data_Case by County.csv'
# df_sa = pd.read_csv(input_file_name_us)
# table_head = list(df_sa.columns.values)

@app.callback(
    Output('datatable-section', 'children'),
    [Input('country-dropdown', 'value')])
def updateTable(value):
    global df
    if value == 'United States':
        df = df_us
    elif value == 'United Kingdom':
        df = df_uk
    elif value == 'South Africa':
        df = df_sa
    return [
        dtb.DataTable(
            id='datatable-interactivity',
            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
            ],
            data=df.to_dict('records'),
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10,
        )
    ]

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    [Input('datatable-interactivity', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container', "children"),
    [Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff[" Cases "] or dff["areaName"] or dff["State"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in [" Cases ", "Deaths", "Population as at 2019"] if column in dff
    ]
