"""Aula — funções, tratamento de erros e imutabilidade (introdução)."""


def somar(a, b):
    """Retorna a soma de dois valores."""
    return a + b


print(somar(2, 3))


def dividir(a, b):
    """Divide a por b e sinaliza divisão por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


try:
    print(dividir(10, 0))
except ValueError as erro:
    print("Erro:", erro)


def incrementar_copia(elementos, indice):
    """Retorna uma nova lista, sem alterar a lista recebida."""
    if not 0 <= indice < len(elementos):
        raise IndexError("Índice fora dos limites da lista.")
    nova_lista = elementos.copy()
    nova_lista[indice] += 1
    return nova_lista


lista_original = [1, 2, 3, 4, 5]
lista_atualizada = incrementar_copia(lista_original, 0)
print("Lista original:", lista_original)
print("Nova lista:", lista_atualizada)
