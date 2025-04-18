from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import os

enter_path = "formatted_data.csv"

if os.path.exists(enter_path):
    df = pd.read_csv(enter_path).sort_values(by=['Date'])

else:
    raise FileNotFoundError

app = Dash()

fig = px.line(df, x="Date", y="Sales", title="Pink morsel sales")

app.layout = html.Div(children=[
    dcc.Graph(
        id='Line chart',
        figure=fig
    )
])



if __name__ == '__main__':
    app.run(debug=True)
