"""Identificação exploratória de possíveis outliers usando o método IQR.

Um ponto fora dos limites estatísticos não é necessariamente um erro.
Investigue o contexto antes de corrigir, excluir ou manter qualquer registro.
"""
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arquivo = Path(__file__).resolve().parent / "titanic.csv"
if not arquivo.exists():
    raise FileNotFoundError(f"Não encontrei o arquivo: {arquivo}")

dados = pd.read_csv(arquivo)
if "age" not in dados.columns:
    raise KeyError("A coluna 'age' não existe no dataset.")

idades = dados["age"].dropna()
q1 = idades.quantile(0.25)
q3 = idades.quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

possiveis_outliers = idades[
    (idades < limite_inferior) | (idades > limite_superior)
]

print(f"Q1: {q1:.2f} | Q3: {q3:.2f} | IQR: {iqr:.2f}")
print(f"Limites: {limite_inferior:.2f} a {limite_superior:.2f}")
print("Quantidade de possíveis outliers:", len(possiveis_outliers))
print("Valores identificados:\n", possiveis_outliers.sort_values())

sns.boxplot(x=idades)
plt.title("Distribuição das idades — análise de possíveis outliers")
plt.xlabel("Idade")
plt.tight_layout()
plt.show()
