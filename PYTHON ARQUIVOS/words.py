"""Conta a frequência de palavras em um arquivo de texto.

Uso: python words.py caminho/para/arquivo.txt
Se nenhum caminho for informado, o programa solicita um nome.
"""
from collections import Counter
from pathlib import Path
import re
import sys


def contar_palavras(caminho: Path) -> Counter:
    contagem = Counter()
    with caminho.open("r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras = re.findall(r"\b[\wÀ-ÿ]+\b", linha.casefold())
            contagem.update(palavras)
    return contagem


def main() -> None:
    nome_arquivo = sys.argv[1] if len(sys.argv) > 1 else input("Informe o arquivo: ").strip()
    caminho = Path(nome_arquivo).expanduser()

    try:
        contagem = contar_palavras(caminho)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return
    except UnicodeDecodeError:
        print("Não foi possível ler o arquivo como UTF-8. Verifique a codificação.")
        return
    except OSError as erro:
        print(f"Erro ao abrir o arquivo: {erro}")
        return

    if not contagem:
        print("O arquivo não contém palavras.")
        return

    palavra, frequencia = contagem.most_common(1)[0]
    print(f"Palavra mais frequente: {palavra} ({frequencia} ocorrência(s))")


if __name__ == "__main__":
    main()
