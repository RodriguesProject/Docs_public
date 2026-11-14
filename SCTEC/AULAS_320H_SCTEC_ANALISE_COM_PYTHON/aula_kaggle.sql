CREATE TABLE public.vendas_kaggle(
transacao_id INTEGER PRIMARY KEY,
data_venda DATE NOT NULL,
cliente_id VARCHAR(20) NOT NULL,
genero VARCHAR(20),
idade SMALLINT CHECK (idade >= 0),
categoria VARCHAR(50) NOT NULL,
quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
preco_unitario NUMERIC(12,2) NOT NULL CHECK(preco_unitario >= 0),
valor_total NUMERIC(12,2) NOT NULL CHECK(valor_total > 0)
);