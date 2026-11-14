nome = input("Digite seu nome: ")
ano_nascimento = input("Digite seu ano de nascimento: ")
print(f"Olá, {nome}! Você nasceu em {ano_nascimento}. Em 2030, você terá {2030 - int(ano_nascimento)} anos.")
print()

print("Agora vamos criar uma tupla de telefones:")

telefone3 = [("Yan", "1234-5678"), ("Maria", "9876-5432"), ("Pedro", "5555-5555")]
print(telefone3[0][1])  # Imprime o número de telefone de Yan
print(telefone3[1][1])  # Imprime o número de telefone de Maria
print(telefone3[2][1])  # Imprime o número de telefone de Pedro
print(telefone3[0])  # Imprime o nome de Yan e telefone
print(telefone3[1])  # Imprime o nome de Maria e telefone
print(telefone3[2])  # Imprime o nome de Pedro e telefone
print()

print("Agora vamos criar um dicionário de telefones:")

telefone3_dict = dict(telefone3)
print(telefone3_dict)  # Imprime a lista de telefones como um dicionário, onde Yan virou uma chave e seu número de telefone é o valor, e assim por diante para Maria e Pedro.
print(telefone3_dict["Yan"])  # Imprime o número de telefone de Yan usando a chave "Yan"
telefone3_dict["Ana2"] = "1111-2222"  # Adiciona um novo contato ao dicionário
print(telefone3_dict)  # Imprime o dicionário atualizado com o novo contato
telefone3_dict["Maria"] = "9999-8888"  # Atualiza o número de telefone de Maria
print(telefone3_dict)  # Imprime o dicionário atualizado com o número de telefone de Maria atualizado
telefone3_dict.pop("Pedro")  # Remove o contato de Pedro do dicionário
print(telefone3_dict)  # Imprime o dicionário atualizado sem o contato de Pedro
del telefone3_dict["Maria"]  # Remove o contato de Maria do dicionário usando a palavra-chave del
print(telefone3_dict)  # Imprime o dicionário atualizado sem o contato de Maria