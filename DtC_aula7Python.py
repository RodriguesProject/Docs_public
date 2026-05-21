#Aula 7: Tipos, Estruturas de Dados e Fluxos de Controle (Parte 2)
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas)  # Imprime a lista de frutas
print()
for fruta in frutas:
    print(fruta)  # Imprime cada fruta individualmente
print()
num = 1
while num <= 5:
    print(num)  # Imprime os números de 1 a 5
    num += 1 # Incrementa o número para evitar um loop infinito
print()
# Exemplo de uso de break e continue
for i in range(1, 6):
    if i == 3:
        continue  # Pula a iteração quando i é igual a 3
    if i == 5:
        break  # Sai do loop quando i é igual a 5
    print(i)  # Imprime os números de 1 a 4, pulando o 3 e parando antes do 5