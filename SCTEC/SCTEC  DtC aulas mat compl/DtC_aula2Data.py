#Aula 2: Numpy: Objetos, Vetorização e Fundamentos da Estatística
import sys
sys.stdout.reconfigure(encoding='utf-8')


import numpy as np
#Criando um array unidimensional
array1 = np.array([10, 20, 30, 40, 50])
print(array1, "\n")  # Imprime o array e uma nova linha para melhor formatação
print(array1[2], "\n")  # Acessando o terceiro elemento (índice 2)
print(array1[1:4], "\n")  # Acessando os elementos do índice 1 ao 3 
print(array1[::2], "\n")  # Acessando os elementos de índice par (0, 2, 4)
print(array1[1::2], "\n")  # Acessando os elementos de índice impar (1, 3)

min = np.min(array1)  # Calculando o valor mínimo do array
max = np.max(array1)  # Calculando o valor máximo do array

print('Mínimo: ', min, "\n")  # Imprime o valor mínimo
print('Máximo: ', max, "\n")  # Imprime o valor máximo
print('Media: ', np.mean(array1), "\n")  # Calculando a média dos elementos do array
print('Mediana: ', np.median(array1), "\n")  # Calculando a mediana dos elementos do array
print('Desvio Padrão: ', np.std(array1), "\n")  #Calculando o desvio padrão dos elementos do array
print('Variância: ', np.var(array1), "\n")  # Calculando a variância dos elementos do array 
print('________________________________\n')


print('MATRIZ__________________________\n') #Criando um array bidimensional
array2 = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
])
print(array2, "\n")  # Imprime o array bidimensional    
print(array2[1, 2], "\n")  # Acessando o elemento da primeira linha e segunda coluna (índice [0, 1]), Saída esperada: 6

#informações da matriz
print('informações da matriz___________\n');
print(f"Shape da matriz: {array2.shape}", "\n")  # Imprime a forma do array (número de linhas e colunas)
print(f"Size da matriz: {array2.size}", "\n")  # Imprime o número total de elementos no array
print(f"Data type dos elementos: {array2.dtype}", "\n")  # Imprime o tipo de dados dos elementos do array
print('________________________________\n');


print(array2[0:2, 1:3], "\n")  # Acessando um subarray (primeiras duas linhas e colunas 1 a 2)
print(array2[:, 0], "\n")  # Acessando todos os elementos da primeira coluna (todas as linhas)
print(array2[1, :], "\n")  # Acessando todos os elementos da segunda linha (todas as colunas)
print('________________________________\n');

print('________________________________\n');
print('EXERCÍCIOS______________________\n');

array3 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])  # Criando um array unidimensional com os números de 5 a 50  
print('Array3: ', array3, "\n")  # Imprime o array3 
print('Média: ', np.mean(array3), "\n")  # Calculando a média dos elementos do array3
print('Mediana: ', np.median(array3), "\n")  # Calculando a mediana dos elementos do array3
print('Desvio Padrão: ', np.std(array3), "\n")  # Calculando o desvio padrão dos elementos do array3
print('Variância: ', np.var(array3), "\n")  # Calculando a variância dos elementos do array3
