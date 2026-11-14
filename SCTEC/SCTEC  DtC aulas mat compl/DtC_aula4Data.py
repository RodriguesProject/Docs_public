"""Aula 4 — análise exploratória, limpeza e manipulação com Pandas.

Execute a partir de qualquer diretório: os CSVs são procurados ao lado deste script.
Os valores ausentes são mantidos inicialmente para que possam ser analisados.
"""
from pathlib import Path
import pandas as pd

PASTA_DADOS = Path(__file__).resolve().parent


def carregar_csv(nome_arquivo: str) -> pd.DataFrame:
    caminho = PASTA_DADOS / nome_arquivo
    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho}. "
            "Coloque o CSV na pasta do script ou ajuste PASTA_DADOS."
        )
    return pd.read_csv(caminho)


# Dataset Titanic
df = carregar_csv("titanic.csv")
print("Informações gerais:")
df.info()
print("\nEstatísticas descritivas:\n", df.describe(include="all"))
print("\nPrimeiras linhas:\n", df.head())
print("\nTipos de dados:\n", df.dtypes)
print("\nValores ausentes por coluna:\n", df.isna().sum())

# Filtragem: passageiros com idade de até 10 anos.
if "age" in df.columns:
    print("\nPassageiros com até 10 anos:\n", df.loc[df["age"].le(10)].head())

# Identificação e remoção de duplicatas, mantendo a última ocorrência.
duplicadas = df.duplicated()
print("\nQuantidade de linhas duplicadas:", int(duplicadas.sum()))
df_sem_duplicatas = df.drop_duplicates(keep="last").copy()
print("Linhas após remoção:", len(df_sem_duplicatas))

# Exemplo de tratamento seletivo: não substitua todos os NaN por texto "0".
# Para uma coluna numérica, a mediana pode ser uma estratégia adequada:
if "age" in df_sem_duplicatas.columns:
    idade_mediana = df_sem_duplicatas["age"].median()
    df_sem_duplicatas["age"] = df_sem_duplicatas["age"].fillna(idade_mediana)

# Renomeação e ordenação, se a coluna existir.
if "sex" in df_sem_duplicatas.columns:
    df_sem_duplicatas = df_sem_duplicatas.rename(columns={"sex": "genero"})
    print("\nRegistros ordenados por gênero:\n",
          df_sem_duplicatas.sort_values(by="genero").head())

# Dataset de vendas de sorvete
vendas = carregar_csv("Ice Cream Sales - temperatures.csv")
print("\nResumo do dataset de sorvetes:\n", vendas.describe(include="all"))
if "Temperature" in vendas.columns:
    print("\nMenores temperaturas:\n",
          vendas.sort_values(by="Temperature").head())
