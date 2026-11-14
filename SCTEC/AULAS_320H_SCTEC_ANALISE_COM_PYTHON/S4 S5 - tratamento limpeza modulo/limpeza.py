import re
import pandas as pd

def limpar_numero(texto):
  if pd.isna(texto):
    return ""

  texto = str(texto)

  return re.sub(r"\D", "", texto)

def email_valido(email):
  if pd.isna(email):
    return False

  email = str(email).strip()

  padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

  return bool(re.match(padrao, email))

def tratar_clientes(df):
    resultado = df.copy()

    resultado["telefone_limpo"] = resultado["telefone"].apply(
        limpar_numero
    )

    resultado["cpf_limpo"] = resultado["cpf"].apply(
        limpar_numero
    )

    resultado["email_limpo"] = resultado["email"].fillna("").apply(
        lambda texto: str(texto).strip()
    )

    resultado["email_formato_ok"] = resultado["email_limpo"].apply(
        email_valido
    )

    resultado["telefone_tamanho_ok"] = resultado["telefone_limpo"].apply(
        lambda texto: len(texto) in [10, 11]
    )

    resultado["cpf_11_digitos"] = resultado["cpf_limpo"].apply(
        lambda texto: len(texto) == 11
    )

    return resultado
