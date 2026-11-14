SELECT current_database();

--	EXISTEM INFORMAÇÕES AUSENTES?

SELECT COUNT(*) AS linhas_com_ausencia
FROM vendas_kaggle
WHERE transacao_id IS NULL
	or data_venda is null
	or cliente_id is null
	or genero is null
	or idade is null
	or categoria is null
	or quantidade is null
	or preco_unitario is null
	or valor_total is null;

-- O TOTAL CORRESPONDE À QUANTIDADE MULTIPLICADA PELO PREÇO?

select count (*) as totais_divergentes
FROM vendas_kaggle
WHERE valor_total <> quantidade * preco_unitario;

-- Interpretação: as verificações de ausência e de cálculo total não encontraram problema.

-- PRODUZIR INDICADORES GERAIS

SELECT COUNT(*) AS transacoes,
		sum(quantidade) AS unidades,
		sum(valor_total) as valor_total,
		round(AVG(valor_total), 2) as valor_medio
FROM vendas_kaggle

-- ATENDENDO UMA SOLICITAÇÃO DE FILTROS

-- 1- MOSTRANDO DEZ TRANSAÇÕES DE "Electronics" COM VALOR DE PELO MENOS 1
select transacao_id, categoria, valor_total
from vendas_kaggle
WHERE categoria = 'Electronics'
	and valor_total >= 1000
order by valor_total desc, transacao_id
limit 10;

-- 2- COMPARAR CATEGORIAS
-- QUAL CATEGORIA LIDERA EM VALOR TOTAL? ELA TAMBÉM LIDERA EM QUANTIDADE DE TRANSAÇÕES?

select categoria,
		count(*) as transacoes,
		sum(quantidade) as  unidades,
		sum(valor_total) as valor_total,
		round(AVG(valor_total), 2)  as valor_medio
FROM vendas_kaggle
group by categoria
order by valor_total desc;

-- Analisar o periodo - por data
select date_trunc('month', data_venda) :: date as mes,
		count(*) as transacoes,
		sum(valor_total) as valor_total
FROM vendas_kaggle
GROUP BY DATE_TRUNC('month', data_venda):: date
order by mes;

-- RECORTE ANUAL
select transacao_id, data_venda, valor_total
from vendas_kaggle
where data_venda >= DATE '2023-01-01'
	and data_venda < DATE '2024-01-01'
order by data_venda, transacao_id
limit (10);

-- FILTRAGEM DE GRUPOS

-- QUAIS CATEGORIAS ULTRAPASSAM 150 MIL UNIDADES MONETÁRIAS?
select categoria,
		sum(valor_total) as valor_total
FROM vendas_kaggle
group by categoria
having sum(valor_total) > 150000
ORDER BY valor_total desc;
