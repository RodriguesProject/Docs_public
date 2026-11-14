import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
plt.figure(figsize=(8, 6)) #define o tamanho da figura para o gráfico de histograma.
#sns.histplot(data=titanic, x="age", bins=30, kde=True) #cria um gráfico de histograma usando o Seaborn, onde o eixo x representa a idade dos passageiros. O parâmetro data=titanic indica que os dados para o gráficoestão no DataFrame titanic. O parâmetro bins=30 define o número de intervalos (bins) para o histograma, e kde=True adiciona uma curva de densidade ao gráfico, que ajuda a visualizar a distribuição dos dados.
sns.histplot(data=titanic, x="age")
plt.title("Distribuição de Idade dos Passageiros do Titanic") #adiciona um título ao gráfico, indicando que ele mostra a distribuição de idade dos passageiros do Titanic.
plt.xlabel("Idade") #adiciona um rótulo ao eixo x, indicando que ele representa a idade dos passageiros.
plt.ylabel("Contagem") #adiciona um rótulo ao eixo y, indicando que ele representa a contagem de passageiros em cada intervalo de idade.
plt.show() #exibe o gráfico de histograma na tela.
#titanic.to_csv("titanic.csv", index=False) para download dos dados do titanic em csv, index=False para não incluir o índice do DataFrame no arquivo CSV.
