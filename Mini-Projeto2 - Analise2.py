
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
# 
# ## Download: http://github.com/dsacademybr
# 
# ## Mini-Projeto 2 - Análise Exploratória em Conjunto de Dados do Kaggle
# 
# ## Análise 2

# In[2]:


# Imports
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style = "white")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Dataset
clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path,encoding = "latin-1")
df.columns


# In[70]:


# Crie um Plot que mostre o número de veículos pertencentes a cada marca
dataS = df.copy()
dataS.loc[:, ['brand','name']]

x = dataS.groupby(['brand']).count()['name']
x = x.sort_values()
width = 0.70
fig, ax = plt.subplots(figsize=(10,8))
plt.barh(x.index, x.values, width, color='r')
plt.xticks()
plt.xlabel("Marca", fontsize=20)
plt.ylabel("Número de veículos", fontsize=20)
plt.title('Número de veículos por marca')
plt.show()




# ## Número de veículos pertencentes a cada marca

# In[ ]:


# Salvando o plot
g.savefig(("plots/Analise2/brand-vehicleCount.png"))


# ## Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio

# In[69]:


# Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
df2 = df.copy()

df2 = df2.loc[:, ['vehicleType', 'price', 'gearbox']]


fig, ax = plt.subplots(figsize=(10,8))

sns.barplot(x="vehicleType", y='price', hue='gearbox', data=df2)
plt.grid(True)
plt.xlabel('Tipo de veículo', fontsize=15)
plt.ylabel('Preço médio', fontsize=15)
plt.title('Preço médio de veículos com base no tipo e no tipo de câmbio')
plt.show()





# In[6]:


# Salvando o plot
fig.savefig("plots/Analise2/vehicletype-gearbox-price.png")


# Conheça a Formação Cientista de Dados, um programa completo, 100% online e 100% em português, com 340 horas, mais de 1.200 aulas em vídeos e 26 projetos, que vão ajudá-lo a se tornar um dos profissionais mais cobiçados do mercado de análise de dados. Clique no link abaixo, faça sua inscrição, comece hoje mesmo e aumente sua empregabilidade:
# 
# https://www.datascienceacademy.com.br/pages/formacao-cientista-de-dados

# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
