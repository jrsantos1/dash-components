import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Nome': ['A', 'B', 'C', 'D'],
    'Valor': [50, -30, 20, -10]
})

# Iniciando o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    dcc.Graph(
        id='tabela',
        figure=go.Figure(
            data=[
                go.Table(
                    header=dict(values=list(df.columns)),
                    cells=dict(values=[df[col] for col in df.columns])
                )
            ]
        )
    )
])

# Aplicando o estilo CSS
app.css.append_css({
    'external_url': (
        'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'
    )
})

# Adicionando o estilo customizado para a célula
app.css.append_css({
    'external_url': (
        '''
        .negative-cell {
            background-image: linear-gradient(to right, red 0%, red calc(50% - 1px), white 50%, white 100%);
        }
        '''
    )
})

# Callback para aplicar a classe CSS à célula negativa
@app.callback(
    dash.dependencies.Output('tabela', 'figure'),
    [dash.dependencies.Input('tabela', 'figure')]
)
def update_table(figure):
    for i, row in enumerate(df.itertuples()):
        for j, val in enumerate(row):
            if j == 1 and val < 0:  # Verifica se o valor é negativo na segunda coluna
                figure['data'][0]['cells']['fill']['color'][i * len(df.columns) + j] = 'negative-cell'
    return figure

# Rodando o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)