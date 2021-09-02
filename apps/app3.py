import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


from app import app

dash_colors = {
    'background': '#111111',
    'text': '#BEBEBE',
    'grid': '#333333',
    'red': '#BF0000',
    'blue': '#466fc2',
    'green': '#5bc246'
}

# To read the dataset 

data = pd.read_csv('data/covid_worldwide_income_group.csv')

# Defining App layout



layout = html.Div([
    # html.H3('App 1'),
    # dcc.Dropdown(
    #     id='app-1-dropdown',
    #     options=[
    #         {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
    #             'NYC', 'MTL', 'LA'
    #         ]
    #     ]
    # ),
    # html.Div(id='app-1-display-value'),
    # dcc.Link('Go to App 2', href='/apps/app2')

    dbc.Jumbotron(
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
                                                'color': dash_colors['green'],
                                                'margin': 0,
                                                'padding': 50,
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
                                            'color': dash_colors['green'],
                                            'margin': 0,
                                            'padding': 50,
                                            'cursor': 'pointer'
                                            },      
                                        ),
                                    ),
                                    style={
                                        'textDecoration': 'none'
                                    }
                                )
                            ),

                            dbc.Col(
                                dcc.Link(
                                    href='/insights',
                                    refresh=False,
                                    children=(
                                        html.H1(children='INSIGHTS', id='insights-nav',
                                        style={
                                            'textAlign': 'center',
                                            'color': dash_colors['green'],
                                            'margin': 0,
                                            'padding': 50,
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
                )
            ],
            fluid=True,
            style={
                'textAlign': 'center',
                'color': dash_colors['green'],
                'backgroundColor': 'black',
                'marginTop': 0,
                'padding': 0
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
            'color': dash_colors['text']
            }),
        
        html.Div(children='Drag the slider to see the effects on the population.', style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'marginBottom': 50
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
              dcc.Graph(
                  id='covid-vs-edu',
              ),    
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
      ], style = {'width':'90%','margin':'auto'})
])

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

@app.callback(Output('covid-vs-edu', 'figure'),
              [Input('population-slider', 'value'),
               Input('interest-variable', 'value')])             
def update_scatter(selected_pop, interest_var):
  sorted = data[data.population <= selected_pop]
  fig = px.scatter(sorted,
                  x='expected_years_of_school',
                  y=sorted[interest_var]/sorted.population,
                  size='population',
                  color='income_group',
                  hover_name='country',
                  template='plotly_white',
                  labels={'expected_years_of_school':'Expected Years of School',
                          'y': scatter_y_label(interest_var)},
                  title='Total Cases VS Education Level')
  fig.update_layout(transition_duration=500)
  return fig

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

# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')]
#     )
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

