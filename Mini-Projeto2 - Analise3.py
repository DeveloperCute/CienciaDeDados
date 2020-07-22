
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
# 
# ## Download: http://github.com/dsacademybr
# 
# ## Mini-Projeto 2 - Análise Exploratória em Conjunto de Dados do Kaggle
# 
# ## Análise 3

# In[1]:


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


# In[4]:


# Dataset
clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path,encoding = "latin-1")
df.columns


# ## Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio

# In[10]:


# Crie um Barplot com o Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio

df2 = df.copy()
df2 = df2.loc[:, ['fuelType', 'gearbox', 'price']]

fig, ax = plt.subplots(figsize=(10, 8))

sns.barplot(x='fuelType', y='price', hue='gearbox', data=df2)
plt.xlabel('Tipo de combustível', fontsize=15)
plt.ylabel('Preço médio', fontsize=15)
plt.title('Preço médio de veículo com base no tipo de combustível e no tipo de câmbio', fontsize=20)
plt.show()


# In[4]:


# Salvando o plot
fig.savefig("plots/Analise3/fueltype-vehicleType-price.png")


# ## Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio

# In[11]:


# Crie um Barplot com a Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio

df3 = df.copy()
df3 = df.loc[:, ['vehicleType', 'gearbox', 'powerPS']]


fig, ax = plt.subplots(figsize=(10,8))

sns.barplot(x='vehicleType', y='powerPS', hue='gearbox', data=df3)
plt.xlabel('Tipo de veículo')
plt.ylabel('Potência Média')
plt.title('Potência média de um veículo e tipo de caixa de câmbio')
plt.show()


# In[6]:


# Salvando o plot
fig.savefig("plots/Analise3/vehicletype-fueltype-power.png")


# Conheça a Formação Cientista de Dados, um programa completo, 100% online e 100% em português, com 340 horas, mais de 1.200 aulas em vídeos e 26 projetos, que vão ajudá-lo a se tornar um dos profissionais mais cobiçados do mercado de análise de dados. Clique no link abaixo, faça sua inscrição, comece hoje mesmo e aumente sua empregabilidade:
# 
# https://www.datascienceacademy.com.br/pages/formacao-cientista-de-dados

# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
