def saudação ():
    print("Bom dia monstrão")
saudação()

def saudação(nome):
    print(f"Bom dia {nome} monstrão")

saudação("Thiago")

def soma (a, b):
    return a + b

resultado = soma(8, 7,)
print(resultado)

quadrado = lambda x: x ** 2
print(quadrado(8))

def funcao():
    variavel_local = "Eu sou uma variável local 10"
    print(variavel_local)
variavel_global = "Eu sou uma variável global 20"
def funcao2():
    print(variavel_global)
funcao()
funcao2()

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura
area = area_retangulo(5, 3.5)
print(area)

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
print(soma_variavel(1, 2, 3))
print(soma_variavel(4, 5, 6, 7))

def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media
print(calcular_media(10, 15, 35))

def soma_3(x):
    return x + 3
somar = lambda x: x + 3
print("some 3 a um numero", somar(5))

x = 5
y = "3"
z = x + int(y)
print(z)
