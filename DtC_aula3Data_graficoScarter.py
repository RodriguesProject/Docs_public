#Definindo variáveis para o gráfico de pontos
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([ 23, 29, 11, 13, 17, 2, 3, 5, 7, 19])
plt.scatter(x, y, color='green', marker='*', s=100) #criando um gráfico de pontos e definindo a cor dos pontos usando o nome da cor
plt.legend(['Pontos'], loc='upper right') #adicionando uma legenda para os pontos e definindo a posição da legenda usando o parâmetro loc
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Pontos')
plt.show()