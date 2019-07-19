# historical transactions analysis 

# necessary imports
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
import pandas as pd 
import dash_table as dt
import numpy as np
import plotly.graph_objs as go
import dash_table.FormatTemplate as FormatTemplate


# import app
from app import app

# load data 
df = pd.read_csv('data_cleaned.csv')


# make a stacked Bar graph

tmp = pd.DataFrame(df.groupby(['Year', 'City'])['Place'].count()).unstack().fillna(value=0)
tmp.columns = tmp.columns.droplevel()
tmp = tmp.reset_index()
cols = list(tmp.columns)
cols.remove('Year')

bar1 = go.Bar(x=tmp.Year, y=tmp.BURNABY, name='Burnaby')
bar2 = go.Bar(x=tmp.Year, y=tmp.VANCOUVER, name='Vancouver')
bar3 = go.Bar(x=tmp.Year, y=tmp.COQUITLAM, name='Coquitlam')
bar4 = go.Bar(x=tmp.Year, y=tmp.RICHMOND, name='Richmond')
bar5 = go.Bar(x=tmp.Year, y=tmp['LAS VEGAS'], name='Las Vegas')
bar6 = go.Bar(x=tmp.Year, y=tmp['NEW WESTMINSTER'], name='New Westminster')
bar7 = go.Bar(x=tmp.Year, y=tmp['SAN FRANSCISCO'], name='San Franscisco')
bar8 = go.Bar(x=tmp.Year, y=tmp.TORONTO, name='Toronto')
bar9 = go.Bar(x=tmp.Year, y=tmp['NORTH VANCOUVER'], name='North Vancouver')
bar10 = go.Bar(x=tmp.Year, y=tmp.SURREY, name='Surrey')
bar11 = go.Bar(x=tmp.Year, y=tmp.Unknown, name='Unkown')

bar_graph_data = [bar1, bar2, bar3, bar4, bar5, bar6, bar7, bar8, bar9, bar10, bar11]
city_bar_layout = go.Layout(
    barmode='group',
    plot_bgcolor='#323846'
) 
 
# make a density plot for the yearly data
tmp = pd.DataFrame(df.groupby('Month')['amount'].sum())
amt = tmp.amount.values
months = df.Month.unique()
d = {'Month': months, 'Amount': amt}
tmp =  pd.DataFrame(d)

amt_bar_data = [go.Bar(x=months, y=amt)]
amt_bar_layout = go.Layout( 
    xaxis={
            'categoryorder': 'array',
            'categoryarray': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        },
    plot_bgcolor='#323846'
)



# page layout
layout = html.Div(
    [
        html.Div(
            [
                # html.H1('Historical Transactions'),
                html.Div(
                    dt.DataTable(
                        id='table',
                        columns=[
                            {
                                'id': 'amount',
                                'name': 'Price ($)',
                                'type': 'numeric',
                                'format': FormatTemplate.money(2)
                            },
                            {
                                'id': 'Date', 
                                'name': 'Date'
                            },
                            {
                                'id': 'Place',
                                'name': 'Place'
                            },
                            {
                                'id': 'City',
                                'name': 'City'
                            } 
                        ],
                        data=df.to_dict('records'),
                        sorting=True,
                        style_cell={
                            'minWidth': '0px',
                            'maxWidth': '100px',
                            'whitespace': 'normal',
                        },
                        style_table={
                            'height': '300px',
                            'overflowY': 'scroll',
                            'overflowX': 'scroll',
                            'border': 'thin lightgrey solid',
                            'backgroundColor': '#E8DDCD'
                        },
                        n_fixed_rows=1,
                        style_as_list_view=True,
                        style_cell_conditional = [
                            {
                                'if': {'column_id': i},
                                'textAlign': 'left',
                                'backgroundColor': '#E8DDCD'
                            } for i in ['Date', 'amount', 'Place']
                        ] + 
                        [
                            {
                                'if': {
                                        'column_id': 'amount',
                                    },
                                'backgroundColor': '#EF5939',
                                'width': '80px'
                            }
                        ] +
                        [
                            {
                                'if': {
                                    'column_id': 'Date',
                                },
                                'width': '90px',
                                'backgroundColor': '#E8DDCD'
                            }
                        ] +
                        [
                            {
                                'if': {
                                    'column_id': 'City',
                                },
                                'width': '90px',
                                'backgroundColor': '#E8DDCD'
                            }
                        ],
                        style_header={
                            'backgroundColor': '#F8F7F4'
                        },
                        filtering=True,

                    ),
                    className="one columns",
                    style={
                        'width': '100%',
                        'backgroundColor': '#E8DDCD'
                    },
                    
                    

                ),
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id='city-filter',
                    options=[{'label': i, 'value': i} for i in df.City.unique()],
                    multi=True,
                    value=df.City.unique()
                ),
                dcc.RadioItems(
                    id='measurement',
                    options=[{'label': 'Number of Purchase', 'value': 'count'}, 
                                {'label': 'Amount Spent', 'value': 'amt'}],
                    value='count',
                    labelStyle={'display': 'inline-block'}
                )
            ],
        className='row',
        style={
            'width': '50%',
        }
        ),
        html.Div(
            [
                html.Div(
                    dcc.Graph(
                        id='barGraph',
                        figure={
                            "data": bar_graph_data,
                            "layout": city_bar_layout
                        },
                    ),
                ),
                html.Div(
                    dcc.Graph(
                        id="amtBarGraph",
                        figure={
                            "data": amt_bar_data,
                            "layout": amt_bar_layout
                        },
                    )
                )
            ], 
            className="two columns",
            style={
                'width': '100%',
            }
        ), 
    ],
    className="row"
)
