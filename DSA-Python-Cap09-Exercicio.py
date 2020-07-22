
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 9</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercício: Análise Exploratória de Dados com Python
# 
# Neste exercício, você vai realizar uma análise exploratória em um dos mais famosos datasets para Machine Learning, o dataset iris com informações sobre 3 tipos de plantas. Esse dataset é comumente usado em problemas de Machine Learning de classificação, quando nosso objetivo é prever a classe dos dados. No caso deste dataset, prever a categoria de uma planta a partir de medidas da planta (sepal e petal).
# 
# Em cada célula, você encontra a tarefa a ser realizada. Faça todo o exercício e depois compare com a solução proposta.
# 
# Dataset (já disponível com o Scikit-Learn): https://archive.ics.uci.edu/ml/datasets/iris

# In[2]:


# Imports
import time
import numpy as np
import pandas as pd
import matplotlib as mat
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
get_ipython().run_line_magic('matplotlib', 'inline')

fontsize = 14
ticklabelsize = 14


# In[3]:


np.__version__


# In[4]:


pd.__version__


# In[5]:


mat.__version__


# In[7]:


# Carregando o dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(len(df))
df


# ## Extração e Transformação de Dados

# In[9]:


# Imprima os valores numéricos da Variável target (o que queremos prever), 
# uma de 3 possíveis categorias de plantas: setosa, versicolor ou virginica
iris.target_names


# In[10]:


# Imprima os valores numéricos da Variável target (o que queremos prever), 
# uma de 3 possíveis categorias de plantas: 0, 1 ou 2
iris.target


# In[22]:


# Adicione ao dataset uma nova coluna com os nomes das espécies, pois é isso que vamos tentar prever (variável target)
df['name'] = pd.Categorical.from_codes(iris.target, iris.target_names)


# In[23]:


# Inclua no dataset uma coluna com os valores numéricos da variável target
df['target'] = iris.target


# In[26]:


# Extraia as features (atributos) do dataset e imprima 
features = df.columns[:4]
features


# In[33]:


# Calcule a média de cada feature para as 3 classes
df.groupby('target').mean().T


# ## Exploração de Dados

# In[36]:


# Imprima uma Transposta do dataset (transforme linhas e colunas e colunas em linhas)
df.transpose()


# In[37]:


# Utilize a função Info do dataset para obter um resumo sobre o dataset 
df.info()


# In[38]:


# Faça um resumo estatístico do dataset
df.describe()


# In[50]:


# Verifique se existem valores nulos no dataset
df.isnull().sum()


# In[52]:


# Faça uma contagem de valores de sepal length
df['sepal length (cm)'].value_counts()


# ## Plot

# In[63]:


# Crie um Histograma de sepal length
ex = ['sepal width (cm)', 'petal length (cm)','petal width (cm)', 'target', 'name']
df.loc[:,df.columns.difference(ex)].hist()
plt.show()


# In[87]:


# Crie um Gráficos de Dispersão (scatter Plot) da variável sepal length versus número da linha, 
# colorido por marcadores da variável target

plt.scatter(range(len(df2)), df['petal width (cm)'], c=df['target'])
plt.xlabel('Número da Linha', fontsize=fontsize)
plt.ylabel('Sepal length (cm)', fontsize=fontsize)
plt.title('Gráfico de Dispersão dos Atributos, colorido por marcadores da classe alvo', fontsize=fontsize)


# In[94]:


# Crie um Scatter Plot de 2 Features (atributos)
plt.scatter(df['petal width (cm)'], df['petal length (cm)'], c=df['target'])
plt.xlabel('Petal wid')
plt.ylabel('Petal Len')


# In[95]:


# Crie um Scatter Matrix das Features (atributos)
attributes = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
pd.plotting.scatter_matrix(df[attributes], figsize=(16, 12))


# In[98]:


# Crie um Histograma de todas as features
df.hist(figsize=(12,12))


# Conheça a Formação Cientista de Dados, um programa completo, 100% online e 100% em português, com 400 horas, mais de 1.200 aulas em vídeos e 26 projetos, que vão ajudá-lo a se tornar um dos profissionais mais cobiçados do mercado de análise de dados. Clique no link abaixo, faça sua inscrição, comece hoje mesmo e aumente sua empregabilidade:
# 
# https://www.datascienceacademy.com.br/pages/formacao-cientista-de-dados

# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
