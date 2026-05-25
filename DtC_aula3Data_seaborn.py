import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic") #carregar o conjunto de dados "titanic", que é um dataset de exemplo disponível no Seaborn. Ele contém informações sobre os passageiros do navio Titanic, como idade, sexo, classe, tarifa paga e se sobreviveram ou não.
df_titanic = titanic.head() #selecionar as primeiras linhas do DataFrame titanic e armazená-las em df_titanic. Isso é útil para obter uma visão geral dos dados e verificar a estrutura do DataFrame.
print(df_titanic, '\n') #imprimir o DataFrame df_titanic, mostrando as primeiras linhas do conjunto de dados do Titanic. Isso ajuda a entender quais colunas estão presentes e os tipos de dados que elas contêm.
df_por_sexo = titanic.groupby("sex")["survived"].sum().reset_index() #agrupa os dados por sexo e calcula a soma de sobreviventes para cada grupo. O resultado é um DataFrame onde cada linha represen   ta um sexo (masculino ou feminino) e a coluna "survived" contém a soma de sobreviventes para cada sexo. O método reset_index() é usado para transformar o índice do agrupamento em uma coluna normal, facilitando a visualização dos resultados.
print(df_por_sexo, '\n') #imprime o DataFrame resultante, mostrando a soma de sobreviventes para cada sexo. Isso pode ser útil para analisar a distribuição de sobreviventes entre homens e mulheres no Titanic.

plt.figure(figsize=(8, 6)) #define o tamanho da figura para o gráfico de barras.
sns.barplot(data=df_por_sexo, x="sex", y="survived") #cria um gráfico de barras usando o Seaborn, onde o eixo x representa o sexo dos passageiros e o eixo y representa a soma de sobreviventes para cada sexo. O parâmetro data=df_por_sexo indica que os dados para o gráfico estão no DataFrame df_por_sexo. O gráfico de barras é uma maneira visual de comparar a quantidade de sobreviventes entre homens e mulheres no Titanic.
plt.title("Número de Sobreviventes por Sexo") #adiciona um título ao gráfico, indicando que ele mostra o número de sobreviventes por sexo.
plt.xlabel("Sexo") #adiciona um rótulo ao eixo x, indicando que ele representa o sexo dos passageiros.
plt.ylabel("Número de Sobreviventes") #adiciona um rótulo ao eixo y, indicando que ele representa o número de sobreviventes.
plt.show() #exibe o gráfico de barras na tela.


df_por_sexo = titanic.groupby("sex")["survived"].mean() #agrupa os dados por sexo e calcula a média de sobrevivência para cada grupo. O resultado é uma série onde o índice é o sexo (masculino ou feminino) e os valores são as médias de sobrevivência correspondentes.
print(df_por_sexo, '\n') #imprime a série resultante, mostrando a média de sobrevivência para cada sexo. Isso pode ser útil para analisar se há diferenças significativas na taxa de sobrevivência entre homens e mulheres no Titanic.