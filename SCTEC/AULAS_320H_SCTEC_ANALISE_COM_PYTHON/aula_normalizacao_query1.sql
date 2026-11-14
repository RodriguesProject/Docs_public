SELECT *
FROM vendas_brutas
ORDER BY pedido_id, produto_id;

SELECT COUNT (*)
FROM vendas_brutas;

-- Diagnosticar o que cada linha representa

SELECT
	COUNT(*) AS linhas,
	COUNT(DISTINCT pedido_id) AS pedidos,
	COUNT(DISTINCT cliente_id) AS clientes,
	COUNT(DISTINCT produto_id) AS produtos,
	SUM(quantidade) AS unidades,
	SUM(quantidade * preco_unitario) AS valor_total
FROM vendas_brutas;

-- CONSULTAS CLIENTES

SELECT
	cliente_id,
	cliente_nome,
	COUNT(*) AS linhas,
	COUNT(DISTINCT pedido_id) AS pedidos
FROM vendas_brutas
GROUP BY cliente_id, cliente_nome
ORDER BY cliente_id;

-- Informaçõees de pedido
SELECT DISTINCT
	pedido_id,
	cliente_id,
	cliente_nome,
	cliente_estado
FROM vendas_brutas
ORDER BY pedido_id;

-- Informações de produto
SELECT DISTINCT
	produto_id,
	produto_nome,
	categoria
FROM vendas_brutas
ORDER BY produto_id;

-- Informações dos itens
SELECT
	pedido_id,
	produto_id,
	quantidade,
	preco_unitario
FROM vendas_brutas
ORDER BY pedido_id, produto_id;

--VERIFICAÇÂO
SELECT cliente_id
FROM vendas_brutas
GROUP BY cliente_id
HAVING COUNT(DISTINCT (cliente_nome, cliente_estado)) > 1;

BEGIN;

CREATE TABLE clientes(
    cliente_id INTEGER PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	estado CHAR(2) NOT NULL
);

CREATE TABLE produtos (
    produto_id VARCHAR(10) PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	categoria VARCHAR(50) NOT NULL
);

CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
	cliente_id INTEGER NOT NULL,

	FOREIGN KEY (cliente_id)
	    REFERENCES clientes(cliente_id)
);

CREATE TABLE itens_pedido (
    pedido_id INTEGER NOT NULL,
	produto_id VARCHAR(10) NOT NULL,

	quantidade INTEGER NOT NULL
	    CHECK (quantidade > 0),

	preco_unitario NUMERIC(10,2) NOT NULL
	    CHECK (preco_unitario >= 0),

	PRIMARY KEY (pedido_id, produto_id),

	FOREIGN KEY(pedido_id)
	    REFERENCES pedidos(pedido_id),

	FOREIGN KEY (produto_id)
	    	REFERENCES produtos(produto_id)
	
);

INSERT INTO clientes (cliente_id, nome, estado)
SELECT DISTINCT
    cliente_id,
	cliente_nome,
	cliente_estado
FROM vendas_brutas;

INSERT INTO produtos (produto_id, nome, categoria)
SELECT DISTINCT
    produto_id,
	produto_nome,
	categoria
FROM vendas_brutas;

INSERT INTO pedidos (pedido_id, cliente_id)
SELECT DISTINCT
    pedido_id,
	cliente_id
FROM vendas_brutas;

INSERT INTO itens_pedido (
    pedido_id,
	produto_id,
	quantidade,
	preco_unitario
)
SELECT
    pedido_id,
	produto_id,
	quantidade,
	preco_unitario
FROM vendas_brutas;

COMMIT;

-- Conferindo o final
SELECT * FROM clientes;
SELECT * FROM produtos;
SELECT * FROM pedidos;
SELECT * FROM itens_pedido;

-- Reconstruir o relatório com JOIN
-- Visualizando cliente, produto e quantidade no mesmo relatório

SELECT
    p.pedido_id,
	c.cliente_id,
	c.nome AS cliente_nome,
	c.estado AS cliente_estado,
	pr.produto_id,
	pr.nome AS produto_nome,
	pr.categoria,
	i.quantidade,
	i.preco_unitario
FROM itens_pedido AS i

JOIN pedidos as p
   ON p.pedido_id = i.pedido_id

JOIN clientes AS c
    ON c.cliente_id = p.cliente_id

JOIN produtos AS pr
    ON pr.produto_id = i.produto_id

ORDER BY p.pedido_id, pr.produto_id;

-- Conferir se a migração preservou os dados
SELECT 
    'origem' AS etapa,
	COUNT(*) AS linhas,
	SUM(quantidade) AS unidades,
	SUM(quantidade * preco_unitario) AS valor_total
FROM vendas_brutas

UNION ALL

SELECT 
     'normalizado',
	 COUNT(*),
	 SUM(quantidade),
	 SUM(quantidade * preco_unitario)
FROM itens_pedido;