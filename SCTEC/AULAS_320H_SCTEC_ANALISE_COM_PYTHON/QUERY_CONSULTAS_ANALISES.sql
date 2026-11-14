SELECT
    current_database() AS banco_atual,
    current_user AS usuario_atual;

-- Contagem de registros novos
SELECT COUNT(*) AS clientes_novos
FROM clientes
WHERE cliente_id BETWEEN 10001 AND 22000;

-- Contagem de registros de novos pedidos
SELECT COUNT(*) AS pedidos_novos
FROM pedidos
WHERE pedido_id BETWEEN 20001 AND 40000;

-- Linhas de itens novas
SELECT COUNT(*) AS linhas_de_itens_novas
FROM itens_pedido
WHERE pedido_id BETWEEN 20001 AND 40000;

-- Quantidade de clientes
SELECT COUNT(*) AS quantidade_clientes
FROM clientes; 

-- Consulta de amostra dos clientes cadastrados
SELECT 
    cliente_id,
	nome,
	estado
FROM clientes 
WHERE cliente_id BETWEEN 10001 AND 22000
ORDER BY cliente_id
LIMIT 20;

-- Pedidos entregues com valor a partir de R$ 500
SELECT
    pedido_id,
	data_pedido,
	valor_total,
	status
FROM pedidos
WHERE pedido_id BETWEEN 20001 AND 40000
  AND status = 'entregue'
  AND valor_total >= 500
ORDER BY valor_total DESC, pedido_id
LIMIT 10;

-- Trabalhando valores ausentes sem excluir registros automaticamente

-- Quantos clientes novos estão sem email?
SELECT COUNT(*) AS clientes_sem_email
FROM clientes
WHERE cliente_id BETWEEN 10001 AND 22000
  AND email IS NULL;

-- Qual o total de clientes com email cadastrado?
SELECT
    COUNT(*) AS total_clientes,
	COUNT(email) AS clientes_com_email
FROM clientes
WHERE cliente_id BETWEEN 10001 AND 22000;

-- Calculo de indicadores gerais - Contagem, Soma, Média, Máx, Min
SELECT
    COUNT(*) AS quantidade_pedidos,
	SUM(valor_total) AS valor_total,
	ROUND(AVG(valor_total), 2) AS valor_medio,
	MIN(valor_total) AS menor_pedido,
	MAX(valor_total) AS maior_pedido
FROM pedidos
WHERE pedido_id BETWEEN 20001 AND 40000;

-- Reunir os registros pelo status do pedido
SELECT
    status,
	COUNT(*) AS quantidade_pedidos,
	SUM(valor_total) AS valor_total,
	ROUND(AVG(valor_total), 2) AS valor_medio
FROM pedidos
WHERE pedido_id BETWEEN 20001 AND 40000
GROUP BY status
ORDER BY quantidade_pedidos DESC;

-- Relacionando pedidos e clientes - INNER JOIN
SELECT
    p.pedido_id,
	c.nome,
	c.estado,
	p.data_pedido,
	p.valor_total,
	p.status
FROM pedidos AS p
INNER JOIN clientes AS c
    ON p.cliente_id = c.cliente_id
WHERE p.pedido_id BETWEEN 20001 AND 40000
ORDER BY p.pedido_id
LIMIT 20;

-- Quais estados dos clientes concentram o maior valor de pedidos entregues?
SELECT
    c.estado,
	COUNT(p.pedido_id) AS quantidade_pedidos,
	SUM(p.valor_total) AS valor_total,
	ROUND(AVG(p.valor_total), 2) AS valor_medio
FROM pedidos AS p
INNER JOIN clientes AS c
    ON p.cliente_id = c.cliente_id
WHERE p.pedido_id BETWEEN 20001 AND 40000
  AND p.status = 'entregue'
GROUP BY c.estado
ORDER BY valor_total DESC;

-- Encontrando clientes cadastrados que ainda não fizeram pedidos
SELECT
    c.cliente_id,
	c.nome,
	c.estado
FROM clientes AS c
LEFT JOIN pedidos AS p
    ON c.cliente_id = p.cliente_id
WHERE c.cliente_id BETWEEN 10001 AND 22000
  AND p.pedido_id IS NULL
ORDER BY c.cliente_id;

-- Contagem de clientes sem pedidos registrados
SELECT COUNT(*) AS clientes_sem_pedidos
FROM clientes AS c
LEFT JOIN pedidos AS p
    	ON c.cliente_id = p.cliente_id
WHERE c.cliente_id BETWEEN 10001 AND 22000
  AND p.pedido_id IS NULL; 

 -- Valores de itens e pedidos
 -- Cálculo de cada Linha
 SELECT 
     pedido_id,
	 produto_id,
	 quantidade,
	 preco_unitario,
	 quantidade * preco_unitario AS valor_item
FROM itens_pedido
WHERE pedido_id BETWEEN 20001 AND 40000
ORDER BY pedido_id, produto_id
LIMIT 20;

-- Soma por pedido
SELECT 
    pedido_id,
	SUM(quantidade * preco_unitario) AS total_itens
FROM itens_pedido
WHERE pedido_id BETWEEN 20001 AND 40000
GROUP BY pedido_id
ORDER BY pedido_id;

-- Procurando divergências - consulta de pedidos sem itens ou com valores divergentes
SELECT 
    p.pedido_id,
	p.valor_total,
	SUM(i.quantidade * i.preco_unitario) AS total_itens
FROM pedidos AS p
LEFT JOIN itens_pedido AS i
    ON p.pedido_id = i.pedido_id
WHERE p.pedido_id BETWEEN 20001 AND 40000
GROUP BY p.pedido_id, p.valor_total
HAVING
    COUNT(i.produto_id) = 0
	OR p.valor_total <> SUM(i.quantidade * i.preco_unitario);