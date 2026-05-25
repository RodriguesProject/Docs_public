#Aula 4: Análise Exploratória de Dados com Pandas e Numpy: GroupBy, Filtragem, Manipulação de Dados
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('C:\\Users\\thiag\\OneDrive\\Documentos\\GitHub\\Docs_public\\titanic.csv')
print(df.info(), end='\n\n')
print(df.describe(), end='\n\n')
print(df.head(), end='\n\n')
#Data types of the columns
print(df.dtypes, end='\n\n')
#Filtragem
df_filtrado = (df[df['age'] <= 10].head())
print(df_filtrado, end='\n\n')
#linhas duplicadas
duplicateRows = df[df.duplicated()]
print("linhas duplicadas: ",len(duplicateRows), end='\n\n')
print('__________________________', end='\n\n')
print(len(df), end='\n\n')
df.drop_duplicates(keep='last', inplace=True)
print(len(df), end='\n\n')
#df.dropna(subset=['deck'], inplace=True)
#print(len(df), end='\n\n')
df.replace(np.nan,'0', inplace=True)
print(df)
#Renomeando colunas
df = df.rename(columns={'sex':'genero'})
print(df.head(), end='\n\n')

sorted_df = df.sort_values(by='genero', ascending=True)
print(sorted_df.head(5), end='\n\n')

print('__________________________', end='\n\n')
print('EXERCÍCIOS________________', end='\n\n')

df = pd.read_csv('C:\\Users\\thiag\\OneDrive\\Documentos\\GitHub\\Docs_public\\Ice Cream Sales - temperatures.csv')
print(df.info(), end='\n\n')
print(df.describe(), end='\n\n') 
sorted_df = df.sort_values(by='Temperature', ascending=True)
print(sorted_df.head(5), end='\n\n')
print('__________________________', end='\n\n')
print('__________________________', end='\n\n')