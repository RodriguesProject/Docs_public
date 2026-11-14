"""Aula 3 — exemplos executáveis de gráficos de linha e de barras."""
import matplotlib.pyplot as plt
import numpy as np

# Gráfico de linha
x_linha = np.array([1, 2, 3, 4, 5])
y_linha = x_linha ** 2

plt.figure(figsize=(7, 4))
plt.plot(x_linha, y_linha, marker="o", label="y = x²")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de linha")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()

# Gráfico de barras
frutas = ["Maçã", "Laranja", "Uva"]
quantidades = [5, 3, 7]

plt.figure(figsize=(7, 4))
plt.bar(frutas, quantidades, color="steelblue")
plt.xlabel("Frutas")
plt.ylabel("Quantidade")
plt.title("Quantidade de frutas")
plt.tight_layout()
plt.show()

# Exercício: salários fictícios
nomes = ["Alice", "Bruno", "Carla", "Diego", "Eva"]
salarios = [5000, 6000, 7000, 8000, 9000]

plt.figure(figsize=(7, 4))
plt.bar(nomes, salarios)
plt.xlabel("Funcionários fictícios")
plt.ylabel("Salário (R$)")
plt.title("Exemplo de salários")
plt.tight_layout()
plt.show()
