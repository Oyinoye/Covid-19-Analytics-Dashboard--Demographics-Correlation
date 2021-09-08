import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_table as dtb


from app import app

dash_colors = {
    'background': '#dee9fa',
    'text': '#BEBEBE',
    'grid': '#333333',
    'red': '#BF0000',
    'blue': '#10274a',
    'green': '#5bc246'
}

# To read the dataset 

data = pd.read_csv('data/covid_worldwide_income_group.csv')

# Defining App layout

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


layout = html.Div( style={'backgroundColor': dash_colors['background']}, children =[

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
        
        html.H1(children='Insights into the Effects of Demographics on the Covid-19 Pandemic.',
        style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'marginTop': 40
            }
        ),

        html.Div(children='Effects of income and education on the rate of spread of the pandemic.', style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            }),
        
        

    # Test addition 

    html.Div(id='graph1', children = [
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]),

    html.Div(children='Drag the slider to see economic implications in other countries.', style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'marginBottom': 20,
            'paddingTop': 30,
            'textSize': '20rem'
            }),
    
    html.Div([
          html.Div([ 
              html.Label('Population'),
              dcc.Slider(
                  id='population-slider',
                  min=data.population.min(),
                  max=data.population.max(),
                  marks={
                    72037 : '72K',
                    80000000 : '80M',
                    150000000 : '150M',
                    300000000 : '300M',
                    700000000 : '700M',
                    1000000000 : '1B',
                    1439323776 : '1.4B' 
                  },
                  value=data.population.min(),
                  step=100000000,
                  updatemode='drag'
              )
          ]),
          html.Div([
              html.Label('Interest Variable'),
              dcc.Dropdown(
                  id='interest-variable',
                  options=[{'label':'Total Cases', 'value':'total_cases'},
                           {'label': 'Total Tests', 'value':'total_tests'},
                           {'label': 'Total Deaths', 'value':'total_deaths'},
                           {'label': 'Total Recovered', 'value':'total_recovered'}],
                  value='total_cases' 
              )
          ])
      ], style = {'width':'90%','margin':'auto'}), 
      html.Div([    
          html.Div(
              dcc.Graph(
                  id='covid-vs-income',
              )
      , style = {'width': '50%', 'display': 'inline-block'}),
          html.Div( 
              dcc.Graph(
                  id='covid-vs-income2',
              )
      , style = {'width': '50%', 'display': 'inline-block'})
    ], style = {'width':'90%','margin':'auto'}),

    html.Div([
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
        ),
        html.Div(id='datatable-interactivity-container2'),

    ]),



])

# ------------- Added Stuff ------------ 
@app.callback(
    Output('datatable-interactivity2', 'style_data_conditional'),
    Input('datatable-interactivity2', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container2', "children"),
    Input('datatable-interactivity2', "derived_virtual_data"),
    Input('datatable-interactivity2', "derived_virtual_selected_rows"))
def update_graphs(rows, derived_virtual_selected_rows):
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
                        "x": dff["country"],
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
        for column in ["pop", "lifeExp", "gdpPercap"] if column in dff
    ]

# -------------- Ended stuff ------------

def scatter_y_label (var):
  if var == 'total_cases':
    return 'Percentage Infected'
  elif var == 'total_tests':
    return 'Percentage Tested'
  elif var == 'total_deaths':
    return 'Percentage Dead'
  elif var == 'total_recovered':
    return 'Percentage Recovered'

# Variable VS Education Level Scatter Plot



# Variable Per Income Group Bar Chart

@app.callback(Output('covid-vs-income', 'figure'),
              [Input('population-slider', 'value'),
               Input('interest-variable', 'value')])             
def update_income_bar(selected_pop, interest_var):
  sorted = data[data.population <= selected_pop].groupby(by='income_group').sum().reset_index()
  fig = px.bar(sorted,
                  x='income_group',
                  y=interest_var,
                  color='income_group',
                  template='plotly_white',
                  labels={'income_group':'Income Group',
                          'total_cases':'Total Cases',
                          'total_tests':'Total Tests',
                          'total_deaths':'Total Deaths',
                          'total_recovered':'Total Recovered'},
                  title='Total Cases By Income Group')
  fig.update_layout()
  return fig

# Variable Per Country Bar Chart

@app.callback(Output('covid-vs-income2', 'figure'),
              [Input('population-slider', 'value'),
               Input('interest-variable', 'value')])             
def update_country_bar(selected_pop, interest_var):
  sorted = data[data.population <= selected_pop]
  fig = px.bar(sorted, 
                x='country', 
                y=interest_var, 
                color='income_group',
                template='plotly_white',
                labels={'country':'Country',
                        'total_cases':'Total Cases',
                        'total_tests':'Total Tests',
                        'total_deaths':'Total Deaths',
                        'total_recovered':'Total Recovered'},
                title='Total Cases per Country')
  fig.update_layout()
  return fig


