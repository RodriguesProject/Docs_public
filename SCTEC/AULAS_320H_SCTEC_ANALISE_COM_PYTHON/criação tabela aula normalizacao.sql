DROP TABLE IF EXISTS vendas_brutas;

CREATE TABLE vendas_brutas (
    pedido_id INTEGER,
    cliente_id INTEGER,
    cliente_nome VARCHAR(100),
    cliente_estado CHAR(2),
    produto_id VARCHAR(10),
    produto_nome VARCHAR(100),
    categoria VARCHAR(50),
    quantidade INTEGER,
    preco_unitario NUMERIC(10,2),
	
    PRIMARY KEY (pedido_id, produto_id)
);

INSERT INTO vendas_brutas (
    pedido_id,
	cliente_id,
	cliente_nome,
	cliente_estado,
	produto_id,
	produto_nome,
	categoria,
	quantidade,
	preco_unitario
)
VALUES 

(1001, 1, 'Ana Souza', 'RJ', 'P001', 'Mouse sem fio', 'Periféricos', 2, 89.90),

(1001, 1, 'Ana Souza', 'RJ', 'P005', 'HUB USB-C', 'Acessórios', 1, 159.90),

(1002, 2, 'Bruno Lima', 'SP', 'P002', 'Teclado mecânico', 'Periféricos', 1, 249.90),

(1003, 1, 'Ana Souza', 'RJ', 'P003', 'Webcam HD', 'Vídeo', 1, 179.90),

(1004, 3, 'Carla Dias', 'RJ', 'P001', 'Mouse sem fio', 'Periféricos', 1, 89.90);

COMMIT;

--SELECT * FROM vendas_brutas;