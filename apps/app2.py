import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app

dash_colors = {
    'background': '#dee9fa',
    'text': '#BEBEBE',
    'grid': '#333333',
    'red': '#BF0000',
    'blue': '#10274a',
    'green': '#5bc246'
}

layout = html.Div(style={'backgroundColor': dash_colors['background']}, children =
    [   
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
        
        html.H1(children='Update the Database',
        style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'marginTop': 40,
            }
        ),

        html.Div(children='Please enter your additional information here to be viewed in INSIGHTS.', style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            }),
        
        html.Div(children='We keep your infomation safe and protected.', style={
            'textAlign': 'center',
            'color': dash_colors['text'],
            'marginBottom': 50
            }),

        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(),

                    dbc.Col(
                        [
                            html.Hr(style={'color': 'white'}),

                            dbc.FormGroup(
                                [
                                    dbc.Label("First name", html_for="form-first-name", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text", id="form-first-name", placeholder="Enter first name"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Last name", html_for="form-last-name", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text", id="form-last-name", placeholder="Enter last name"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Date of Birth", html_for="form-birth-date", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="date",
                                            id="form-birth-date",
                                            style={
                                                'height': '4rem'
                                            }
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Ethnic origin", html_for="ethnicity", width=2),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id='ethnic-origin',
                                            options=[
                                                {'label': '{}'.format(i), 'value': i} for i in [
                                                    'Arabian', 'Asian', 'Black African', 'Caucasian', 'Hispanic', 'Native American',
                                                ]
                                            ]
                                        ),
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Occupation", html_for="occupation", width=2),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id='occupation',
                                            options=[
                                                {'label': '{}'.format(i), 'value': i} for i in [
                                                    'Professional', 'Manager', 'Technician', 'Clerical Worker', 'Service & Support Workers', 'Skilled Agriculture Worker', 'Forestry & Fishery Worker', 'Craft Worker', 'Machine Operator', 'Technician', 'Armed Force', 'Other'
                                                ]
                                            ]
                                        ),
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Address 1", html_for="address-line1", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text", id="address-line1", placeholder="Enter your address (Line 1)"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Address 2", html_for="address-line2", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text", id="address-line2", placeholder="Enter your address (Line 2)"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Town", html_for="town", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text", id="town", placeholder="Enter Town/City"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Country", html_for="country", width=2),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id='country',
                                            options=[
                                                {'label': '{}'.format(i), 'value': i} for i in [
                                                    "South Africa", "England - United Kingdom", "Northern Ireland - United Kingdom", "Scotland - United Kingdom", "Wales - United Kingdom", "United States of America"
                                                ]
                                            ]
                                        ),
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Zip Code", html_for="zip-code", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="text", id="zip-code", placeholder="Enter Zip Code"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),
                            
                            dbc.FormGroup(
                                [
                                    dbc.Label("Telephone", html_for="telephone", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="tel", id="telephone", placeholder="Enter telephone number"
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Symptoms?", html_for="symptoms", width=2),
                                    dbc.Col(
                                        dbc.RadioItems(
                                            id="symptoms",
                                            options=[
                                                {"label": "False", "value": 0},
                                                {"label": "True", "value": 1},
                                            ],
                                            inline=True,
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Vaccinated", html_for="vaccinated", width=2),
                                    dbc.Col(
                                        dbc.RadioItems(
                                            id="vaccinated",
                                            options=[
                                                {"label": "False", "value": 0},
                                                {"label": "True", "value": 1},
                                            ],
                                            inline=True,
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Test date", html_for="test-date", width=2),
                                    dbc.Col(
                                        dbc.Input(
                                            type="date",
                                            id="test-date",
                                            style={
                                                'height': '4rem'
                                            }
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Test result", html_for="test-result", width=2),
                                    dbc.Col(
                                        dbc.RadioItems(
                                            id="test-result",
                                            options=[
                                                {"label": "Negative", "value": 0},
                                                {"label": "Positive", "value": 1},
                                            ],
                                            inline=True,
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Hospitalized", html_for="hospitalized", width=2),
                                    dbc.Col(
                                        dbc.RadioItems(
                                            id="hospitalized",
                                            options=[
                                                {"label": "False", "value": 0},
                                                {"label": "True", "value": 1},
                                            ],
                                            inline=True,
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            dbc.FormGroup(
                                [
                                    dbc.Label("Recovered", html_for="recovered", width=2),
                                    dbc.Col(
                                        dbc.RadioItems(
                                            id="recovered",
                                            options=[
                                                {"label": "False", "value": 0},
                                                {"label": "True", "value": 1},
                                            ],
                                            inline=True,
                                        ),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),

                            html.Hr(style={'color': 'white'}),

                            dbc.FormGroup(
                                [
                                    dbc.Label("", html_for="submit", width=2),
                                    dbc.Col(
                                        dbc.Button("SUBMIT", outline=False, color='primary', block=True, className="mr-1 mt-3 mb-5"),
                                        width=10,
                                    ),
                                ],
                                row=True,
                            ),
                            
                        ],
                        style = { 
                            'textAlign': 'center',
                            'color': 'black',
                            'cursor': 'pointer'
                        },
                        width=6  
                    ),

                    dbc.Col(),
                ]
            ),
            fluid=True,
        ),
        
    ]
)
