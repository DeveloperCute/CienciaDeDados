
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
# 
# ## Download: http://github.com/dsacademybr
# 
# ## Mini-Projeto 2 - Análise Exploratória em Conjunto de Dados do Kaggle
# 
# ## Análise 1

# In[1]:


# Imports
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import colorsys
from datetime import datetime
sns.set(style = "white")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Dataset
clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path,encoding = "latin-1")


# In[3]:


df.columns


# ## Distribuição de Veículos com base no Ano de Registro

# In[23]:


# Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
carYear = df.copy()
carYear = carYear.loc[:, ['name', 'yearOfRegistration']]


fig, ax = plt.subplots(figsize=(8,6))

sns.distplot(carYear["yearOfRegistration"], color="green", kde=True, ax=ax)
ax.set_title('Distribuição de Veículoos com base do Ano de Registro', fontsize=15)
plt.ylabel("DENSIDADE (KDE)", fontsize=15)
plt.xlabel("Ano de Registro", fontsize=15)
plt.show()




# In[13]:


# Salvando o plot
fig.savefig("plots/Analise1/vehicle-distribution.png")


# ## Variação da faixa de preço pelo tipo de veículo

# In[28]:


# Crie um Boxplot para avaliar os outliers
out = df.copy()
out = out.loc[:, ['vehicleType', 'price']]


# In[43]:



fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(out['vehicleType'], out['price'])
plt.xlabel('Tipo de Veículo', fontsize=15)
plt.ylabel('Range de preço', fontsize=15)
plt.grid(True)
plt.title('Análise de Outliers', color='r', fontsize=15)
plt.show()


# ## Contagem total de veículos à venda conforme o tipo de veículo

# In[26]:


# Crie um Count Plot que mostre o número de veículos pertencentes a cada categoria 
group = df.copy()
group = group.loc[:,['vehicleType', 'name']]
x = group['vehicleType'].value_counts()


colors = ('#6A5ACD', '#836FFF', '#6959CD', '#483D8B', '#191970', '#000080', '#00008B', '#0000CD')


width = 0.70
fig, ax = plt.subplots(figsize=(10,5))
fg = plt.bar(x.index, x.values, width, color = colors)
plt.xlabel('Tipo de Veículo')
plt.ylabel('Total de Veículos Para Venda')
plt.title('Contagem total de veículo à venda conforme o tipo de veículo', fontsize=15)
for x in fg:
    plt.annotate(x.get_height(), 
            xy=(x.get_x() + x.get_width() / 2, x.get_height()),
            xytext=(0, 3),
            textcoords='offset points',
            ha='center'
                ) 


plt.show()


# In[8]:


# Salvando o plot
g.savefig("plots/Analise1/count-vehicleType.png")


# Conheça a Formação Cientista de Dados, um programa completo, 100% online e 100% em português, com 340 horas, mais de 1.200 aulas em vídeos e 26 projetos, que vão ajudá-lo a se tornar um dos profissionais mais cobiçados do mercado de análise de dados. Clique no link abaixo, faça sua inscrição, comece hoje mesmo e aumente sua empregabilidade:
# 
# https://www.datascienceacademy.com.br/pages/formacao-cientista-de-dados

# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
