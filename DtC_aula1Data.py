import sys
sys.stdout.reconfigure(encoding='utf-8')
#Aula 1: Mineração, Preparação e Estatística para Ciência de Dados

import pandas as pd

#criando uma série
serie = pd.Series([10, 20, 30, 40, 50]);
print(serie, end='\n\n') #imprimindo a série com espaço (,end='\n\n' para adicionar uma linha em branco após a impressão)
print('__________________________', end='\n\n')
#Carregando o dataset
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Idade': [25, 30, 35, 40, 45, 70],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador']
}
df = pd.DataFrame(data)
print(df, end='\n\n') #acessando a coluna 'Nome'
print('__________________________', end='\n\n')
print(df['Nome'], end='\n\n') #acessando a coluna 'Nome'
print(df['Idade'], end='\n\n') #acessando a coluna 'Idade'
print(df['Cidade'], end='\n\n') #acessando a coluna 'Cidade'
print('__________________________', end='\n\n')
print(df.iloc[0], end='\n\n') #acessando a primeira linha do DataFrame
print(df.iloc[1]) #acessando a segunda linha do DataFrame
print('__________________________', end='\n\n')
print(df.loc[0,'Nome'], end='\n\n') #acessando a primeira linha do DataFrame usando loc
print(df.loc[1,'Nome'], end='\n\n') #acessando a segunda linha do DataFrame usando loc
print('__________________________', end='\n\n')
print(df['Idade'].mean(), end='\n\n') #calculando a média da coluna 'Idade'
print(df['Idade'].median(), end='\n\n') #calculando a mediana da coluna 'Idade'
print('__________________________', end='\n\n')

#Exercício: Crie um dataframe que contenha algumas linhas e colunas de dados sobre funcionários de uma empresa, incluindo informações como nome, endereco, data de nascimento, data de admissao, cargo e salário. Em seguida, mostre na tela todas as linhas da coluna de data de admissao.
print('_______EXERCICIO__________', end='\n\n')

data_funcionarios = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elisa'],
    'Endereco': ['Rua A, 123', 'Rua B, 456', 'Rua C, 789', 'Rua D, 101', 'Rua E, 202'],
    'Data de Nascimento': ['1990-01-01', '1985-05-15', '1992-07-20', '1988-03-10', '1995-12-30'],
    'Data de Admissao': ['2015-06-01', '2010-09-15', '2018-01-20', '2012-11-10', '2020-02-28'],
    'Cargo': ['Analista', 'Gerente', 'Desenvolvedor', 'Designer', 'Coordenador'],
    'Salario': [5000, 8000, 6000, 5500, 7000]
}
df_funcionarios = pd.DataFrame(data_funcionarios)
print(df_funcionarios, end='\n\n') #imprimindo o DataFrame de funcionários
print(df_funcionarios['Data de Admissao'], end='\n\n') #imprimindo a coluna de data de admissao
print('__________________________', end='\n\n')
#Carregando um dataset de e-commerce
print('____CARREGANDO DATASET____', end='\n\n')
df = pd.read_csv('E_commerce_dataset - E_commerce_dataset.csv')
print(df.head(), end='\n\n') #imprimindo as primeiras linhas do DataFrame
print(df.info(), end='\n\n') #imprimindo informações sobre o DataFrame
print(df.describe(), end='\n\n') #imprimindo estatísticas descritivas do