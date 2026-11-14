#Aula 10: Programação Funcional e Lidando com Erros de Programação (Parte 1)
def sum(a, b):
    return a + b
result = sum(2, 3)
print(result)  # Output: 5

print("________________________________________________")
print("________________________________________________")
print()
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:
    result = divide(10, 0)
    print(result)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero

print("________________________________________________")
print("________________________________________________")
print()
def pure_increments(elements, index):
    elements[index] += 1
    return elements
lista = [1, 2, 3,4,5,6,7,8,9]
pure_increments(lista, 0)
print(lista)  # Output: [2, 2, 3,4,5,6,7,8,9] o item 0 da lista foi modificado, ou seja, a função não é pura
print("________________________________________________")
print()
# Para tornar a função pura, sem modificar a lista original, precisamos criar uma nova lista. Aqui está uma versão pura da função:
def pure_increments(elements, index):
    new_elements = elements.copy()
    new_elements[index] += 1
    return new_elements
lista = [1, 2, 3,4,5,6,7,8,9]
pure_increments(lista, 0)
print(lista) 
