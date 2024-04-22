from dash import Dash, html, dash_table
import components
import pandas as pd 
import random

app = Dash(__name__)
df_gapminder = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = df_gapminder[:500]
valores = [random.randint(-100, 100) for _ in range(len(df))]
df['lifeExpPerc'] = df_gapminder['lifeExp'] / df_gapminder['lifeExp'].sum() * 100
df['rand'] = valores
df['randPerc'] = df['rand'] / df['rand'].sum() * 100


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dash_table.DataTable(data=df.to_dict('records'),
                         style_data_conditional=components.table(df, 'randPerc')
                         )
                         ])

if __name__ == '__main__':
    app.run_server(debug=True)