from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px
import os

enter_path = "formatted_data.csv"

if os.path.exists(enter_path):
    df = pd.read_csv(enter_path).sort_values(by=['Date'])

else:
    raise FileNotFoundError

app = Dash()

header = html.H1(
    "Pink morsel sales",
    id='header',
    style={"textAlign": "center"},
)
region_picker = dcc.RadioItems(
        id = "region_picker",
        options=[  {'label': 'North', 'value': 'north'},
                   {'label': 'East', 'value': 'east'},
                   {'label': 'South', 'value': 'south'},
                   {'label': 'West', 'value': 'west'},
                   {'label': 'All', 'value': 'all'}
                ],
        value='all',
        labelStyle = {'display': 'flex','margin-top': '10px'},
    )
region_picker_div = html.Div(
    [region_picker],
    style={'display': 'flex','margin-top': '10px', 'background-color': '#f0f0ff'},
)
@app.callback(
    Output('line_chart', 'figure'),
    Input('region_picker', 'value')
)

def update_chart(region):
    if region == 'all':
        filtered_data= df
    else:
        filtered_data = df[df['Region'] == region]

    fig = px.line(filtered_data, x="Date", y="Sales", title=f"{region.capitalize()} Sales", color_discrete_sequence=["#FF0000"])
    fig.update_layout(plot_bgcolor='#F3ECDB')

    return fig

app.layout = html.Div([
    header,
    dcc.Graph(id='line_chart', figure=update_chart(region='all')),
    region_picker_div,
]
)
if __name__ == '__main__':
    app.run(debug=True)
