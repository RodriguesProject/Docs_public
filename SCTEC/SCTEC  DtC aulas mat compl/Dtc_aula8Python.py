#Aula 8: Ampliando Conhecimento de Estruturas de Dados e Fluxos de Controle (Parte 1)
hora = 9
humor = 'doido sonolento'

if humor == 'sonolento' and hora < 10:
    print('Estou com sono, preciso de um café!')
elif humor == 'sonolento' and hora >= 10:
    print('Ainda estou com sono, mas já é tarde para um café.')
elif humor == 'animado' and hora < 10:
    print('Estou animado, pronto para começar o dia!')
elif humor == 'animado' and hora >= 10:
    print('Estou animado, mas já é tarde para começar o dia.')
else:
    print('Estou em um estado de humor desconhecido Tome um café para melhorar!')
print('______________________________')
#Exemplo 2: Estrutura de Repetição com For
for i in range(1, 6):
    print(f'Número: {i}')
print('______________________________')
#Exemplo 3: Estrutura de Repetição com While
contador = 0
while contador < 5:
    print(f'Contador: {contador}')
    contador += 1
#Exemplo 4: Estrutura de Repetição com For e Condicional
for i in range(1, 11):
    if i % 2 == 0:
        print(f'{i} é um número par.')
    else:
        print(f'{i} é um número ímpar.')
print('______________________________')
print('______________________________')

#Aula 9: Ampliando Conhecimento de Estruturas de Dados e Fluxos de Controle (Parte 2)
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print('planeta: ', planeta)

print('______________________________')
i = 0
while i < 10:
    print(i,end=' ') #end=' ' para imprimir na mesma linha
    i += 1    
    