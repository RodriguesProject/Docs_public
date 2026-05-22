#Aula 12: POO: Orientação a Objetos com Python (Parte 1)
class Pessoa:
    def __init__(self, nome, idade, altura): #Construtor da classe, é chamado quando um objeto é criado (self é uma referência ao próprio objeto)
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} de altura.") #ou print("Olá, meu nome é {}, tenho {} anos e {} de altura.".format(self.nome, self.idade, self.altura)) #Outra forma de formatar a string. OU print("Olá, meu nome é %s, tenho %d anos e %.2f de altura." % (self.nome, self.idade, self.altura)) #Outra forma de formatar a string usando o operador %. ou print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura:.2f} de altura.") #Outra forma de formatar a string usando f-string e limitando a altura a 2 casas decimais. ou print('Olá, meu nome é:', self.nome, ', tenho', self.idade, 'anos e', self.altura, 'de altura.') 
#Criando um objeto da classe Pessoa
pessoa1 = Pessoa("João", 30, 1.75)
pessoa1.apresentar() #Chama o método apresentar do objeto pessoa1
#Criando outro objeto da classe Pessoa
pessoa2 = Pessoa("Maria", 25, 1.65)
pessoa2.apresentar() #Chama o método apresentar do objeto pessoa2
print()
print('________________________________________________________')
print('________________________________________________________')
print()
#exercício
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")   
#Criando um objeto da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)
carro1.exibir_informacoes() #Chama o método exibir_informacoes do objeto carro1
#Criando outro objeto da classe Carro
carro2 = Carro("Honda", "Civic", 2019)
carro2.exibir_informacoes() #Chama o método exibir_informacoes
print()
print('________________________________________________________')
print('________________________________________________________')
print()
#Aula 13: POO: Orientação a Objetos com Python (Parte 2)
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos e {self.altura} de altura.")

    def get_nome(self):
        return self.__nome

    def set_idade(self, nova_idade):
        if nova_idade < 40:
            self.__idade = nova_idade

pessoa1 = Pessoa("Pedro", 30, 1.75)
pessoa2 = Pessoa("Ana", 25, 1.65)
pessoa3 = Pessoa("Carlos", 40, 1.80)
print('________________________________________________________')
print()
pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()
print('________________________________________________________')
print()
print(pessoa1.get_nome()) #Acessa o nome usando o método get_nome
print(pessoa2.get_nome()) #Acessa o nome usando o método get_nome
print(pessoa3.get_nome()) #Acessa o nome usando o método get_nome
print('________________________________________________________')
print()
pessoa1.set_idade(35) #Altera a idade de pessoa1 usando o método set_idade
pessoa1.apresentar() #Apresenta novamente para mostrar a idade atualizada   
print('________________________________________________________')
print()

#Crianuma novaclasse herança
class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura) #Chama o construtor da classe pai (Pessoa)
        self.matricula = matricula

    def estudante(self):
        print('A matrícula do aluno é:', self.matricula) #Adiciona informação adicional sobre a matrícula do aluno  
        print(f"Minha matrícula é {self.matricula}.") #Adiciona informação adicional sobre a matrícula do aluno
    
    def apresentar(self): #polimorfismo: Sobrescreve o método apresentar da classe pai (Pessoa) para incluir a matrícula do aluno
        print(f"Olá, meu nome é {super().get_nome()} e tenho {self.altura} de altura, minha matrícula é {self.matricula}.")
aluno1 = Aluno("Pedro", 20, 1.80, "2023001") #Cria um objeto da classe Aluno
aluno1.estudante() #Chama o método estudante da classe Aluno
aluno1.apresentar() #Chama o método apresentar da classe pai (Pessoa)        
