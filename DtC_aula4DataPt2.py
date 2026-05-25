import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\thiag\\OneDrive\\Documentos\\GitHub\\Docs_public\\titanic.csv')
print(df.info(), end='\n\n')
print(df.describe(), end='\n\n')
print(df.head(), end='\n\n')
print('__________________________', end='\n\n')
suvivors_count = df['survived'].value_counts()
print(suvivors_count, end='\n\n')
print('__________________________', end='\n\n')
plt.figure(figsize=(8,6))
sns.barplot(x=suvivors_count.index, y=suvivors_count.values, color=['red', 'green'])
plt.title('Contagem de Sobreviventes')
plt.xlabel('Sobrevivente (0 = Não, 1 = Sim)')
plt.ylabel('Contagem')
plt.show()