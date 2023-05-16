# Imports
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dash_table
from data import df, dims
from dash.dash_table.Format import Format, Scheme

# Create parallel coordinates plot
fig = px.parallel_coordinates(df, dimensions=dims, color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)

# Define the layout for the app, which includes two range sliders, a parallel coordinates plot, and a data table
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H4('Market Value Range:'),
            dcc.RangeSlider(
                id='market-value-slider',
                min=int(df['Market Value'].min()),
                max=int(df['Market Value'].max()),
                value=[int(df['Market Value'].min()), int(df['Market Value'].max())],
                marks={i: {'label': f"{int(i):,}", 'style': {'color': '#'}} for i in
                       range(int(df['Market Value'].min()), int(df['Market Value'].max()) + 1, 20000000)},
            ),
            html.H4('Contract Expiration Year Range:'),
            dcc.RangeSlider(
                id='contract-expiration-slider',
                min=int(df['Contract Expiration Year'].min()),
                max=int(df['Contract Expiration Year'].max()),
                step=1,
                value=[int(df['Contract Expiration Year'].min()), int(df['Contract Expiration Year'].max())],
                marks={i: f"{i}" for i in
                       range(int(df['Contract Expiration Year'].min()), int(df['Contract Expiration Year'].max()) + 1,
                             1)},
            ),
        ], width=12, className='mb-4'),
# Define two range sliders for filtering by Market Value and Contract Expiration Year
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="parallel-coordinates-plot", figure=fig, selectedData={'points': []}),
        ], width=12),
# Define a parallel coordinates plot
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='players-table',
                columns=[
                    {"name": i, "id": i, "type": "datetime", "format": Format(scheme=Scheme.fixed)}
                    if i == "Contract Expiration Date"
                    else {"name": i, "id": i, "type": "numeric", "format": Format(scheme=Scheme.fixed, group=',')}
                    if i == "Market Value"
                    else {"name": i, "id": i}
                    for i in df.iloc[:, [0, 1, 2, 3, 4, 12, 14]].columns
                ],
                data=df.to_dict('records'),
                style_table={
                    'maxHeight': 'calc(100vh - 300px)',
                    'overflowY': 'auto',
                    'border': 'thin lightgrey solid'
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'left',
                    'minWidth': '180px',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'lineHeight': '15px'
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    },
                    {
                        'if': {'row_index': 'even'},
                        'backgroundColor': 'rgb(255, 255, 255)'
                    },
                    {
                        'if': {'state': 'selected'},
                        'backgroundColor': 'blue'},
                    {
                        'if': {'state': 'selected'},
                        'backgroundColor': 'blue',
                        'color': 'white'
                    }
                ]
            ),
        ], width=12),
# Define a data table to display player data
    ]),
    dcc.Store(id='activefilters', data={}),
    dcc.Store(id='original-figure', data=fig),
], fluid=True)
# Create two storage components to hold filter data and the original figure data
