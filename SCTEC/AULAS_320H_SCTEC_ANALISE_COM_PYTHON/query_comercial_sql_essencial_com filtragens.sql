SELECT current_database() AS banco,
       current_schema() AS esquema;

BEGIN;

CREATE TABLE produtos (
    produto_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nome VARCHAR (100) NOT NULL,
	categoria VARCHAR (50) NOT NULL,

	preco NUMERIC(10,2) NOT NULL
	    CHECK (preco >= 0 ),

	estoque INTEGER NOT NULL DEFAULT 0
	    CHECK (estoque >= 0),

	ativo BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO produtos (
    nome,
	categoria,
	preco,
	estoque,
	ativo
)
VALUES
('Mouse sem fio', 'Periféricos', 89.90, 14, TRUE),
('Teclado mecânico', 'Periféricos', 249.90, 7, TRUE),
('Webcam HD', 'Vídeo', 179.90, 3, TRUE),
('Headset', 'Áudio', 199.90, 9, TRUE),
('HUB USB-C', 'Acessórios', 159.90, 5, TRUE),
('Suporte notebook', 'Acessórios', 119.90, 2, FALSE),
('Cabo HDMI', 'Vídeo', 49.90, 30, TRUE);

COMMIT;

-- VISUALIZAR O CATÁLOGO COMPLETO
SELECT *
FROM produtos
ORDER BY produto_id;

-- SOLICITAÇÃO: PARA UMA LISTA DE PREÇOS, APENAS COM NOME E PREÇO
SELECT nome, preco
FROM produtos
ORDER BY produto_id;

-- ANALISAR PRODUTOS COM O PREÇO MAIOR DO QUE 150
SELECT produto_id, nome, preco
FROM produtos
WHERE preco > 150
ORDER BY produto_id;

-- ANALISAR UMA CATEGORIA - FILTRA UMA CATEGORIA
SELECT produto_id, nome, categoria
FROM produtos
WHERE categoria = 'Periféricos'
ORDER BY produto_id;

-- IDENTIFICAR PRODUTOS QUE ESTÃO COM ESTOQUE BAIXO - 10 unidades em estoque
-- COMBINAR CONDIÇÕES - (condicional AND)
SELECT produto_id, nome, estoque, ativo
FROM produtos
WHERE ativo = TRUE
    AND estoque < 10
ORDER BY produto_id;

-- APRESENTAR PRODUTOS DE VIDEO E DE AUDIO (condicional OR)
SELECT produto_id, nome, categoria
FROM produtos
WHERE categoria = 'Vídeo'
    OR categoria = 'Áudio'
ORDER BY produto_id;

-- PRODUTOS QUE ESTÂO INATIVOS (condicional NOT)
SELECT produto_id, nome, estoque, ativo
FROM produtos
WHERE NOT ativo
ORDER BY produto_id;

-- VISUALIZAR PRODUTOS ATIVOS DAS CATEGORIAS 'Vídeo' e 'Áudio'
SELECT nome, categoria, ativo
FROM produtos
WHERE ativo = TRUE
    AND (
        categoria = 'Vídeo'
		OR categoria = 'Áudio'
	);

-- PESQUISA DE PRODUTOS NA FAIXA DE PREÇO DE 80.00 a 200.00 (intervalos e pesquisa de texto)
SELECT produto_id, nome, preco
FROM produtos
WHERE preco BETWEEN 80 AND 200
ORDER BY produto_id;

-- Procurar produtos que tenha USB no nome - filtro (I LIKE)
SELECT produto_id, nome
FROM produtos
WHERE nome ILIKE '%USB%'
ORDER BY produto_id;
-- Procurar produtos que tenha HD no nome - filtro (I LIKE)
SELECT produto_id, nome
FROM produtos
WHERE nome ILIKE '%HD%'
ORDER BY produto_id;

-- MOSTRAR PRODUTOS DO MAIOR AO MENOR PREÇO
SELECT produto_id, nome, preco
FROM produtos
ORDER BY preco DESC, produto_id;

-- MOSTRAR PRODUTOS DO MENOR AO MAIOR PREÇO
SELECT produto_id, nome, preco
FROM produtos
ORDER BY preco ASC, produto_id;

-- ORDENAR POR CATEGORIA, E DENTRO DA CATEGORIA COLOCAR OS MENORES PREÇOS PRIMEIRO
SELECT produto_id, nome, categoria, preco
FROM produtos
ORDER BY categoria ASC, preco ASC, produto_id;

-- INSERIR REGISTRO DE MARCA NOS PRODUTOS
ALTER TABLE produtos
ADD COLUMN marca VARCHAR(50);

-- VERIFICAR A NOVA COLUNA MARCA DE PRODUTO
SELECT produto_id, nome, marca
FROM produtos
ORDER BY produto_id;

-- LOCALIZANDO INFORMAÇÕES AUSENTES
SELECT produto_id, nome
FROM produtos
WHERE marca IS NULL;

-- CRIAR E REMOVER TABELA DE TREINO
CREATE TABLE categorias_teste(
    categoria_id INTEGER PRIMARY KEY,
	nome VARCHAR(50) NOT NULL
);
-- Verificando tabela teste
SELECT *
FROM categorias_teste;
-- Excluindo tabela teste
DROP TABLE categorias_teste;

-- INSERIR PRODUTO NOVO - Cadastrar um adaptador USB
INSERT INTO produtos(
    nome,
	categoria,
	preco,
	estoque,
	ativo
)
VALUES (
    'Adaptador USB',
	'Acessórios',
	'39.90',
	'2',
	TRUE
)
RETURNING produto_id, nome, preco, estoque, ativo;
-- Visualizar produto novo
SELECT produto_id, nome
FROM produtos;

-- ATUALIZAÇÃO DE ESTOQUE 
-- CORREÇÃO - A LOGÍSTICA CONSTATOU QUE O SALDO CORRETO DO MOUSE É DE 20 UNIDADES
SELECT produto_id, nome, estoque
FROM produtos
WHERE produto_id =1;

UPDATE produtos
SET estoque = 20
WHERE produto_id = 1
RETURNING produto_id, nome, estoque;
-- COMPRA DE ESTOQUE - CASO A LOGISTICA TENHA COMPRADO MAIS 20 unidades
SET estoque = estoque + 20;

-- DESATIVAR PRODUTOS COM MENOS DE 3 UNIDADES EM ESTOQUE
-- Visualizar produtos
SELECT produto_id, nome, estoque, ativo
FROM produtos
WHERE estoque < 3;
-- Removendo
UPDATE produtos
SET ativo = FALSE
WHERE estoque < 3
RETURNING produto_id, nome, estoque, ativo;
-- 
UPDATE produtos
SET ativo = FALSE
WHERE estoque < 3
    AND ativo = TRUE
RETURNING produto_id, nome, estoque, ativo;

BEGIN;

UPDATE produtos
SET estoque = 2
WHERE produto_id = 3

UPDATE produtos
SET estoque = 2
WHERE produto_id = 3;

UPDATE produtos 
SET ativo = FALSE
WHERE estoque < 3
    AND ativo = TRUE
RETURNING produto_id, nome, estoque, ativo;

SELECT produto_id, nome, estoque, ativo
FROM produtos;

-- EXCLUINDO UM ITEM DE CADASTRO
-- PRECISAMOS EXCLUIR ADAPTADOR USB
SELECT produto_id, nome
FROM produtos
WHERE nome = 'Adapatador USB';

-- REMOVER (tem que ter WHERE e AND >>>>>>> para não deletar todos os produtos)
DELETE FROM produtos
WHERE produto_id = 8
    AND nome = 'Adaptador USB'
RETURNING produto_id, nome;

-- RESOLVENDO UMA SOLICITAÇÃO COMERCIAL COMPLETA
-- A equipe de marketind precisa de produtos ativos, com preços entre 50 e 250 e que não pertençam a categoria Vídeo
-- Lista deve começar pelo maior preço
SELECT produto_id, nome, categoria, preco, estoque
FROM produtos
WHERE ativo = TRUE
    AND preco BETWEEN 50 AND 250
	AND categoria <> 'Vídeo'
ORDER BY preco DESC, produto_id;