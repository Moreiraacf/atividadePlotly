import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import numpy as np

df = pd.read_csv(r'C:\Users\Usuário\Documents\ProjetoPy\Atividade_plotly\ecommerce_estatistica.csv')

def geraGrafico(df):

    fig1 = px.histogram(df, x='Temporada', y='Qtd_Vendidos', nbins=35, title='Vendas Por Temporada')

    fig2 = px.line(df, x='N_Avaliações_MinMax', y='Material_Cod', color='Marca_Cod', )
    fig2.update_layout(
        title='Marca x Frequência',
        xaxis_title='Marca',
        yaxis_title='Frequência',
    )

    fig3 = px.scatter(df, x='Marca_Cod', y='Marca_Freq', color='Temporada')

    # fig4 = px.

    fig4 = px.bar(df, x='Temporada', y='Qtd_Vendidos_Cod', color='Marca_Cod', barmode='group', color_discrete_sequence=px.colors.qualitative.Bold)
    fig4.update_layout(
        title='Gráfico barra',
        xaxis_title='temp',
        yaxis_title = 'Qtd_vendas',
        legend_title = 'bla',
        plot_bgcolor = 'rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241,1)'
     )
    

    df_corr = df[['Marca_Cod','Marca_Freq', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Qtd_Vendidos_Cod', 
              'Temporada_Cod',]].corr()

    
    fig5 = px.imshow(df_corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Gráfico Regressão')


    marca_counts = df['Marca_Freq'].value_counts() # Contagem de marcas

    top5_marca = marca_counts.head(5) # Top 5 marcas

    outros = marca_counts.iloc[5:].sum() # Soma das demais marcas
    marcas_finais = pd.concat([top5_marca, pd.Series({'Outros': outros})]) # Agrupando as demais marcas em 'Outras'

    fig6 = px.pie(df, names='Qtd_Vendidos', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)

    return fig1, fig2, fig3, fig4, fig5, fig6

def cria_App(df):
    app = Dash(__name__)
    fig1, fig2, fig3, fig4, fig5, fig6 = geraGrafico(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
    ])
    return app


if __name__ == '__main__':
    app = cria_App(df)
    app.run(debug=True, port=8050) # Default 8050