"""Aula 1 — fundamentos de Pandas e preparação de dados."""
from pathlib import Path
import pandas as pd

# Série
serie = pd.Series([10, 20, 30, 40, 50])
print(serie, end="\n\n")

# DataFrame criado em memória
dados = {
    "Nome": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Idade": [25, 30, 35, 40, 45, 70],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Salvador"],
}
df = pd.DataFrame(dados)
print(df, end="\n\n")
print("Coluna Nome:\n", df["Nome"])
print("Primeira linha:\n", df.iloc[0])
print("Nome da segunda linha:", df.loc[1, "Nome"])
print("Média de idade:", df["Idade"].mean())
print("Mediana de idade:", df["Idade"].median())

# Exercício com dados inteiramente fictícios
dados_funcionarios = {
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa"],
    "Endereco": ["Rua A, 123", "Rua B, 456", "Rua C, 789", "Rua D, 101", "Rua E, 202"],
    "Data de Nascimento": ["1990-01-01", "1985-05-15", "1992-07-20", "1988-03-10", "1995-12-30"],
    "Data de Admissao": ["2015-06-01", "2010-09-15", "2018-01-20", "2012-11-10", "2020-02-28"],
    "Cargo": ["Analista", "Gerente", "Desenvolvedor", "Designer", "Coordenador"],
    "Salario": [5000, 8000, 6000, 5500, 7000],
}
df_funcionarios = pd.DataFrame(dados_funcionarios)
print("\nDatas de admissão fictícias:\n", df_funcionarios["Data de Admissao"])

# Dataset de e-commerce armazenado na mesma pasta deste script
arquivo_csv = Path(__file__).resolve().parent / "E_commerce_dataset - E_commerce_dataset.csv"
if arquivo_csv.exists():
    df_ecommerce = pd.read_csv(arquivo_csv)
    print("\nPrimeiras linhas do e-commerce:\n", df_ecommerce.head())
    print("\nInformações do dataset:")
    df_ecommerce.info()
    print("\nEstatísticas descritivas:\n", df_ecommerce.describe(include="all"))
else:
    print(f"Dataset não encontrado: {arquivo_csv}")
    print("Coloque o CSV na mesma pasta deste script para executar esta parte.")
