
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 7</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Missão: Analisar o Comportamento de Compra de Consumidores.

# ## Nível de Dificuldade: Alto

# Você recebeu a tarefa de analisar os dados de compras de um web site! Os dados estão no formato JSON e disponíveis junto com este notebook.
# 
# No site, cada usuário efetua login usando sua conta pessoal e pode adquirir produtos à medida que navega pela lista de produtos oferecidos. Cada produto possui um valor de venda. Dados de idade e sexo de cada usuário foram coletados e estão fornecidos no arquivo JSON.
# 
# Seu trabalho é entregar uma análise de comportamento de compra dos consumidores. Esse é um tipo de atividade comum realizado por Cientistas de Dados e o resultado deste trabalho pode ser usado, por exemplo, para alimentar um modelo de Machine Learning e fazer previsões sobre comportamentos futuros.
# 
# Mas nesta missão você vai analisar o comportamento de compra dos consumidores usando o pacote Pandas da linguagem Python e seu relatório final deve incluir cada um dos seguintes itens:
# 
# ** Contagem de Consumidores **
# 
# * Número total de consumidores
# 
# 
# ** Análise Geral de Compras **
# 
# * Número de itens exclusivos
# * Preço médio de compra
# * Número total de compras
# * Rendimento total
# 
# 
# ** Informações Demográficas Por Gênero **
# 
# * Porcentagem e contagem de compradores masculinos
# * Porcentagem e contagem de compradores do sexo feminino
# * Porcentagem e contagem de outros / não divulgados
# 
# 
# ** Análise de Compras Por Gênero **
# 
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Compras for faixa etária
# 
# 
# ** Identifique os 5 principais compradores pelo valor total de compra e, em seguida, liste (em uma tabela): **
# 
# * Login
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Itens mais populares
# 
# 
# ** Identifique os 5 itens mais populares por contagem de compras e, em seguida, liste (em uma tabela): **
# 
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# * Itens mais lucrativos
# 
# 
# ** Identifique os 5 itens mais lucrativos pelo valor total de compra e, em seguida, liste (em uma tabela): **
# 
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# 
# 
# ** Como considerações finais: **
# 
# * Seu script deve funcionar para o conjunto de dados fornecido.
# * Você deve usar a Biblioteca Pandas e o Jupyter Notebook.
# 

# In[3]:


# Imports
import pandas as pd
import numpy as np


# In[4]:


# Carrega o arquivo
load_file = "dados_compras.json"
file_recourses = pd.read_json(load_file, orient = "records")
df = pd.DataFrame(file_recourses)
file = df.loc[:, ['Login', 'Sexo', 'Idade']]
file.head()


# ## Informações Sobre os Consumidores

# In[5]:


# Implemente aqui sua solução
file = file.drop_duplicates()
number_count = file.count()[0]
pd.DataFrame({'Total de consumidores:' : [number_count]})


# ## Análise Geral de Compras

# In[99]:


# Implemente aqui sua solução
df.head()


# In[6]:


File = df.loc[:, ['Nome do Item', 'Valor']]
unicos = File.drop_duplicates()
ItensExclusivos = unicos.count()[0]
MediaCompra = df['Valor'].mean()
NumeroTotal = df.count()[0]
Rendimento = df['Valor'].sum()
#pd.DataFrame({'Itens exclusivos: ' : [File]})

compras = pd.DataFrame({'Itens exclusivos' : [ItensExclusivos], 
                       'Média de compra': [MediaCompra], 
                       'Número Total' : [NumeroTotal], 
                       'Rendimento' : [Rendimento]})
compras = compras.round(2)
compras['Rendimento'] = compras['Rendimento'].map('${:,.2f}'.format)
compras


# ## Análise Demográfica

# In[44]:


# Implemente aqui sua solução
contagem_den = df.loc[:, ["Login","Sexo"]]
contagem_den = contagem_den.drop_duplicates()
def contagem(lista):
    masc = fem = outro = 0
    for gen in lista['Sexo']:
        if gen == "Masculino":
            masc += 1
        elif gen == "Feminino":
            fem += 1
        else: 
            outro += 1
    return masc, fem, outro

def porcentagem(m,f,o):
    total = m+f+o
    m = (m/total) * 100
    f = (f/total) * 100
    o = (o/total) * 100
    return m, f, o

conta = contagem(contagem_den)
percen = porcentagem(conta[0], conta[1], conta[2])
print(f"Contagem masculina: {conta[0]} ||| Percentual masculino: {percen[0]:.2f}%")
print(f"Contagem Feminino: {conta[1]} ||| Percentual Feminino: {percen[1]:.2f}%") 
print(f"Contagem de outros: {conta[2]} ||| Percentual outros: {percen[2]:.2f}%")


# ## Informações Demográficas Por Gênero

# In[63]:


# Implemente aqui sua solução
genero_count = contagem_den["Sexo"].value_counts()
genero_percen = (genero_count / number_count) * 100

dataF = pd.DataFrame({"Sexo" : genero_count,
                     "Percent" : genero_percen})

dataF = dataF.round(2)
dataF["Percent"] = dataF["Percent"].map("{:,.1f}%".format)
dataF


# ## Análise de Compras Por Gênero

# In[86]:


# Implemente aqui sua solução
analise = df.loc[:, ['Idade', 'Sexo', 'Valor']]
tCompra = analise.groupby(['Sexo']).sum()['Valor'].rename("Total de vendas")
contCompra = analise.groupby(['Sexo']).count()['Valor'].rename("Contagem Compras")
meanCompra = analise.groupby(['Sexo']).mean()['Valor'].rename("Valor médio")

amostragem = pd.DataFrame({"Total de vendas" : tCompra,
                          "Contagem Compras" : contCompra,
                           "Valor médio" : meanCompra
                          })
amostragem["Total de vendas"] = amostragem["Total de vendas"].map("${:,.2f}".format)
amostragem["Valor médio"] = amostragem["Valor médio"].map("${:,.2f}".format)
amostragem


# ## Consumidores Mais Populares (Top 5)

# In[104]:


# Implemente aqui sua solução
valorT = file.groupby(["Login"]).sum()["Valor"].rename("Valor total de compra")
numeroC = file.groupby(["Login"]).count()["Valor"].rename("Numero de compras")
meanC = file.groupby(["Login"]).mean()["Valor"].rename("Preco medio")

dataCo = pd.DataFrame({"Valor total de compra" : valorT,
                       "Numero de Compras" : numeroC,
                       "Preço médio" : meanC 
                      })

dataCo["Valor total de compra"] = dataCo["Valor total de compra"].map("${:,.2f}".format)
dataCo["Preço médio"] = dataCo["Preço médio"].map("${:,.2f}".format)

dataCo.sort_values('Valor total de compra', ascending=False).head()


# ## Itens Mais Populares

# In[130]:


# Implemente aqui sua solução
df.head()


# In[137]:


quantCompraItem = df.groupby(["Nome do Item"]).count()["Valor"].rename("Item mais popular")
valorTotal = df.groupby(["Nome do Item"]).sum()["Valor"].rename("Valor total")

amostragem = pd.DataFrame({"quantidadeCompras" : quantCompraItem,
                           "Valor Total de vendas" : valorTotal
                          })
amostragem["Valor Total de vendas"] = amostragem["Valor Total de vendas"].map("${:,.2f}".format)
amostragem = amostragem.sort_values(["quantidadeCompras"], ascending=False)
amostragem.head()


# ## Itens Mais Lucrativos

# In[149]:


# Implemente aqui sua solução
quantCompraItem = df.groupby(["Nome do Item"]).count()["Valor"].rename("Item mais popular")
valorTotal = df.groupby(["Nome do Item"]).sum()["Valor"].rename("Valor total")

amostragem = pd.DataFrame({"Valor Total de vendas" : valorTotal,
                           "quantidadeCompras" : quantCompraItem
                           })
amostragem = amostragem.sort_values(["Valor Total de vendas"], ascending=False)
amostragem["Valor Total de vendas"] = amostragem["Valor Total de vendas"].map("${:,.2f}".format)


amostragem.head()


# ## Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
