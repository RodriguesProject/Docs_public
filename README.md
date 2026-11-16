# Docs_public — arquivo público de estudos

Este repositório reúne exercícios, anotações e materiais de aprendizagem desenvolvidos durante a formação em tecnologia. Seu objetivo é demonstrar evolução técnica e registrar estudos; **não substitui o portfólio de projetos autorais**.

## Conteúdo

| Área | Conteúdo |
|---|---|
| Python e lógica | Fundamentos, condicionais, laços, funções, estruturas de dados e scripts introdutórios |
| Análise de dados | NumPy, Pandas, limpeza, preparação, análise exploratória e visualização |
| Bancos de dados | Estudos de SQL/NoSQL, consultas e materiais de apoio |
| Inteligência Artificial | Notebooks e materiais introdutórios |
| Desenvolvimento web | HTML, CSS, Grid, Flexbox, JavaScript e manipulação do DOM |
| Datasets | Bases didáticas utilizadas nos exercícios e estudos |

## Organização recomendada

- `SCTEC/`: materiais e exercícios relacionados às trilhas e aulas SCTEC/SENAI.
- `estudo python/`: exercícios de fundamentos e lógica com Python.
- `Python para Análise de Dados - 3 Ed. (Wes McKinney) pydata-book-3rd-edition/`: cópia principal de referência do código e dos notebooks do livro.
- `requirements.txt`: dependências Python usadas nos exercícios deste repositório.

**Regra para evitar duplicidade:** consulte a cópia principal do material de Wes McKinney indicada acima. Não crie outra cópia dentro de pastas de curso ou de exercícios. Os notebooks e datasets do livro são material de referência; os projetos autorais devem ficar em repositórios próprios.

## Ambiente Python

No terminal, a partir da pasta do repositório:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Se a política de execução do PowerShell impedir a ativação, use o interpretador diretamente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Não versione ambientes virtuais, credenciais, caches, arquivos temporários ou caminhos locais.

## Critérios de manutenção

1. Preserve os materiais didáticos úteis e mantenha os nomes originais dos arquivos sempre que isso ajudar a rastrear a aula de origem.
2. Separe exercícios de aula de projetos autorais com objetivo, análise e conclusões próprios.
3. Mantenha datasets pequenos e necessários aos exemplos; para bases grandes, avalie Git LFS ou disponibilização externa com fonte e licença documentadas.
4. Inclua um README em cada projeto autoral explicando objetivo, dados, ferramentas, etapas, resultados e como executar.
5. Verifique a licença e as condições de redistribuição de PDFs, livros, imagens e datasets antes de publicar.
6. Utilize dados fictícios ou anonimizados. Nunca publique documentos, endereços, telefones, credenciais, tokens ou informações pessoais.

## Portfólio

Projetos selecionados para apresentação profissional ficam no repositório [RodriguesProject](https://github.com/RodriguesProject/RodriguesProject). Este repositório permanece como arquivo público de aprendizagem.
