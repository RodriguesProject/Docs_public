SELECT current_database();

-- TABELA DE CLIENTES

CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL,
    email VARCHAR(150) UNIQUE
);

--TABELA DE PEDIDOS

CREATE TABLE pedidos (
	pedido_id INTEGER PRIMARY KEY,
	cliente_id INTEGER NOT NULL,
	data_pedido DATE NOT NULL,
	valor_total NUMERIC(10,2) NOT NULL CHECK (valor_total >= 0),
	status VARCHAR (20) NOT NULL,
	CONSTRAINT fk_pedidos_cliente
		FOREIGN KEY (cliente_id)
		REFERENCES clientes(cliente_id)	
);

--TABELA DE ITENS

CREATE TABLE itens_pedido (
	pedido_id INTEGER NOT NULL,
	produto_id VARCHAR(10) NOT NULL,
	quantidade INTEGER NOT NULL,
	preco_unitario NUMERIC(10,2) NOT NULL CHECK (preco_unitario >= 0),
	PRIMARY KEY (pedido_id, produto_id),
	CONSTRAINT fk_itens_pedido
		FOREIGN KEY (pedido_id)
		REFERENCES pedidos(pedido_id)
);

--INSERIR DADOS NAS TABELAS

INSERT INTO clientes (cliente_id, nome, estado, email)
VALUES (1, 'Ana Souza', 'RJ', 'anasouza@hotmail.com');

