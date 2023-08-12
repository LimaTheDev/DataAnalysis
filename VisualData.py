import plotly_express as px 
from DataAnalysis import dados

colunas = ["loja", "cidade", "estado", "regiao", "tamanho", "local_consumo"]
for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y="preco", text_auto=True, color="forma_pagamento")
    grafico.show()

