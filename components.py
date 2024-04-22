import pandas as pd 
import numpy as np

def table(df:pd.DataFrame, column: str):
    
    positivos = np.linspace(0, df[df[column] > 0][column].max(), 100)
    negativos = np.linspace(df[df[column] < 0][column].min(), 0, 100)

    styles = []

    for i, x in enumerate(zip(positivos, negativos)):
    #for p, n in zip(positivos.reshape(50,2), negativos.reshape(50,2)):
        
        #positivos 
        p_atual = x[0]
        p_anterior = 0 if i == 0 else positivos[i-1]
        n_atual = x[1]
        n_anterior = 0 if i == 0 else negativos[i-1]

        styles.append(
             {
                'if': {
                    'filter_query': ('{{{column}}} >= {min}' +
                                     (' && {{{column}}} <= {max}')).format(column=column, min=p_anterior, max=p_atual),
                    'column_id': f'{column}'},
                'background': (
                f"""
                    linear-gradient(to right,
                    white 0%,
                    white 50%,
                    green 50%,
                    green {50 if p_atual == 0 else 50 + round((p_atual * 0.5))}%,
                    white {50 + round((p_atual * 0.5)) + 1}%,
                    white 100%)
                """
            ),
            }
        )

        #negativos
        styles.append({
                'if': {
                    'filter_query': ('{{{column}}} >= {min} ' + 
                    ('&& {{{column}}} <= {max}')).format(column=column, min=round(n_anterior), max=round(n_atual)),
                    'column_id': f'{column}'},
                'background': (
                f"""
                    linear-gradient(to right,
                    white 0%,
                    white {(50 - (round(abs(n_atual))))-1}%,
                    red {50 - (round(abs(n_atual)))}%,
                    red 50%,
                    white 50%,
                    white 100%)
                """
            ),
            }
        )



    return styles
