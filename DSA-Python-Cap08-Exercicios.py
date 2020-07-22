
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 8</font>
# 
# ## Download: http://github.com/dsacademybr

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ### Exercícios Sobre Módulos Python Para Análise de Dados

# ### ****** ATENÇÃO ******
# ### Alguns dos exercícios podem requerer pesquisa adicional na documentação dos pacotes. Pesquise!

# ### Exercício 1

# In[ ]:


# Crie um array NumPy com 1000000 e uma lista com 1000000.
# Multiplique cada elemento do array e da lista por 2 e calcule o tempo de execução com cada um dos objetos (use %time).
# Qual objeto oferece melhor performance, array NumPy ou lista?


# In[22]:


import numpy as np
import pandas as pd
import matplotlib as mt
import random


# In[52]:


array = np.arange(1000000)
get_ipython().run_line_magic('time', 'for x in range(10): a2 = array * 2')


# In[53]:


lista = list(range(1000000))
get_ipython().run_line_magic('time', 'for x in range(10): lista2 = [x * 2 for x in lista]')


# ### Exercício 2

# In[63]:


# Exercício 2
# Crie um array de 10 elementos
# Altere o valores de todos os elementos dos índices 5 a 8 para 0
array = np.arange(10)
array[5:8] = 0
#for x in range(5,9):
#   array[x] = 0
array


# ### Exercício 3

# In[77]:


# Crie um array de 3 dimensões e imprima a dimensão 1 
array = np.array([[0,0,0], [0,1,0], [0,2,0]])
#array1 = np.eye(3)
array[0]


# ### Exercício 4

# In[114]:


# Crie um array de duas dimensões (matriz).
# Imprima os elementos da terceira linha da matriz
# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas

array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(array[2])
print(array[:2, 1:])
#array.transpose()[1:3]


# ### Exercício 5

# In[116]:


# Calcule a transposta da matriz abaixo
arr = np.arange(15).reshape((3, 5))

print(arr)

arr.transpose()


# ### Exercício 6

# In[123]:


# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

resultado = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
resultado


# ### Exercício 7

# In[128]:


# Crie um array A com 10 elementos e salve o array em disco com a extensão npy
# Depois carregue o array do disco no array B
array = np.arange(10)
np.save('arra_a', array)

a = np.load('arra_a.npy')
print(a)


# ### Exercício 8

# In[144]:


# Considerando a série abaixo, imprima os valores únicos na série
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])
obj.unique()

#obj = obj.drop_duplicates()
#df = pd.DataFrame(obj, columns=["Vogal"])
#df = df.sort_values(['Vogal'])
#df


# ### Exercício 9

# In[168]:


# Considerando o trecho de código que conecta em uma url na internet, imprima o dataframe conforme abaixo.
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
data = resp.json()
df = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
df


# In[20]:





# ### Exercício 10

# In[174]:


# Crie um banco de dados no SQLite, crie uma tabela, insira registros, 
# consulte a tabela e retorne os dados em dataframe do Pandas 
import sqlite3

conn = sqlite3.connect('meuBanco.sqlite')

query = """
    CREATE TABLE pessoa(
    id not null primary key,
    nome varchar(20),
    idade int(3)
    )
"""

conn.execute(query)


# In[176]:


data = [(1, 'Marccus', 19),
       (2, 'Pedro', 10),
        (3, 'Maria', 30),
        (4, 'Joana', 40)]

stmt = """ INSERT INTO pessoa VALUES(?, ?, ?)"""

conn.executemany(stmt, data)


# In[177]:


conn.commit()


# In[183]:


cursor = conn.execute('select * from pessoa')
rows = cursor.fetchall()
cursor.description

df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
df


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
