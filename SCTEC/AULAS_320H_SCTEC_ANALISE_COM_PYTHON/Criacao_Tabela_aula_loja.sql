SELECT current_database();

-- Tabela de clientes
CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL,
    email VARCHAR(150) UNIQUE
);

-- Tabela de pedidos
CREATE TABLE pedidos (
   pedido_id INTEGER PRIMARY KEY,
   cliente_id INTEGER NOT NULL,
   data_pedido DATE NOT NULL,
   valor_total NUMERIC(10,2) NOT NULL CHECK (valor_total >= 0),
   status VARCHAR(20) NOT NULL,
   CONSTRAINT fk_pedidos_cliente
        FOREIGN KEY (cliente_id)
		REFERENCES clientes(cliente_id)
);

-- Tabela de itens
CREATE TABLE itens_pedido (
    pedido_id INTEGER NOT NULL,
	produto_id VARCHAR(10) NOT NULL,
	quantidade INTEGER NOT NULL CHECK (quantidade > 0),
	preco_unitario NUMERIC(10,2) NOT NULL CHECK (preco_unitario >= 0),
	PRIMARY KEY (pedido_id, produto_id),
	CONSTRAINT fk_itens_pedido
	    FOREIGN KEY (pedido_id)
		REFERENCES pedidos(pedido_id)
);