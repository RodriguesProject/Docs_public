#Aula 3: Visualização Eficaz de Dados com Matplotlib
import sys
sys.stdout.reconfigure(encoding='utf-8')
import matplotlib.pyplot as plt
import numpy as np
#criando um gráfico simples de linha
#plt.plot([1, 2, 3], [2, 6, 7])
#plt.show() #para exibir o gráfico retire o comentário (#) desta linha

#Dados de exemplo
x = ['Maça', 'Laranja', 'Uva']
y = [5, 3, 7]

#plt.bar(x, y, color=['red', 'orange', 'purple']) #criando um gráfico de barras e definindo as cores para cada barra usando uma lista de cores
#plt.bar(x, y, color= 'steelblue') #definindo uma única cor usando nome da cor
#adicionando rótulos e título
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')   
#plt.show()

# Gerar dados de exemplo
arr = np.array([1, 2, 3, 4, 5])
# Criar um gráfico de linha
#plt.plot(arr, arr**2, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Linha')
#plt.show()
print()
print('________________________________\n')
print('EXERCÍCIO_______________________\n')
#crie dois arrays com nome e salários de funcionários e em seguida mostre gráficos de barras para visualizar os salários dos funcionários.
nomes = np.array(['Alice', 'Bob', 'Charlie', 'Thiago', 'Maria'])
salarios = np.array([5000, 6000, 7000, 8000, 9000])
#plt.bar(nomes, salarios, color='skyblue')
plt.xlabel('Funcionários')
plt.ylabel('Salário')
plt.title('Salários dos Funcionários')
#plt.show()