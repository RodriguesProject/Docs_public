#Aula 6: Tipos, Estruturas de Dados e Fluxos de Controle (Parte 1)
pilha = [];  # Cria uma pilha vazia
pilha.append(4)  # Adiciona um elemento ao topo da pilha
print(pilha)  # Imprime a pilha
pilha.append(7)  # Adiciona outro elemento ao topo da pilha
pilha.append(9)  # Adiciona mais um elemento ao topo da pilha
pilha.append(1)  # Adiciona mais um elemento ao topo da pilha
print(pilha)  # Imprime a pilha após as adições
pilha.pop()  # Remove o elemento do topo da pilha portanto 1 LIFO (Last In, First Out)
print(pilha)  # Imprime a pilha após a remoção

print()
#Agora vamos trabalhar com filas, onde o primeiro elemento a entrar é o primeiro a sair (FIFO - First In, First Out)

from collections import deque  # Importa a classe deque para criar uma fila eficiente

fila = deque()  # Cria uma fila vazia
fila.append(4)  # Adiciona um elemento ao final da fila 
print(fila)  # Imprime a fila
fila.append(7)  # Adiciona outro elemento ao final da fila
fila.append(9)  # Adiciona mais um elemento ao final da fila
fila.append(1)  # Adiciona mais um elemento ao final da fila
print(fila)  # Imprime a fila após as adições
fila.popleft()  # Remove o elemento do início da fila portanto FIFO (First In, First Out)
print(fila)  # Imprime a fila após a remoção
fila.pop()  # Remove o elemento do final da fila
print(fila)  # Imprime a fila após a remoção do último elemento