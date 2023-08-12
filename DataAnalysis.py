import pandas as pd

dados = pd.read_excel("vendas.xlsx")
#print(dados)
'''
cima = dados.head()
print(cima)

baixo = dados.tail()
print(baixo)

total = dados.shape
print(total)

tipos = dados.dtypes
print(dados)

descricao = dados.describe()
print(descricao)
'''

#vendas por loja
vendas_loja = dados.loja.value_counts()
print(vendas_loja)

#vendas por tamanho
vendas_tamanho = dados.tamanho.value_counts()
print(vendas_tamanho)

#formas de pagamento
forma_pagamento = dados.forma_pagamento.value_counts()
print(forma_pagamento)

#faturamente por loja
faturamento = dados.groupby("loja").preco.sum()
print(faturamento)

# faturamento medio por loja
faturamento_medio = dados.groupby("loja").preco.mean()
print(faturamento_medio)

#agrupamento de mais de uma coluna
agrupamento = dados.groupby(["loja", "forma_pagamento"]).preco.sum()
print(agrupamento)

#criando arquivo excel
arquivo = dados.groupby(["loja", "forma_pagamento", "preco"] ).preco.sum().to_excel("analise_dados.xlsx")
print(arquivo)
