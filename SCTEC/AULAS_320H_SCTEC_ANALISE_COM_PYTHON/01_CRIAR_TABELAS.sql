-- AULA LOJA | ETAPA 1: CRIAR AS TABELAS
-- Execute o arquivo completo no banco aula_loja.
-- Mantem os nomes, tipos e regras do material original.
-- Nao apaga tabelas nem registros existentes.
-- IF NOT EXISTS pressupoe que tabelas preexistentes tenham a estrutura original.
-- As chaves inteiras continuam manuais, sem geracao automatica de IDs.

BEGIN;
DO $verificar_banco$
BEGIN
    IF current_database() <> 'aula_loja' THEN
        RAISE EXCEPTION 'Abra o Query Tool conectado ao banco aula_loja antes de continuar.';
    END IF;
END;
$verificar_banco$;

CREATE TABLE IF NOT EXISTS public.clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL,
    email VARCHAR(150) UNIQUE
);

CREATE TABLE IF NOT EXISTS public.pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    data_pedido DATE NOT NULL,
    valor_total NUMERIC(10,2) NOT NULL CHECK (valor_total >= 0),
    status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_pedidos_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES public.clientes(cliente_id)
);

CREATE TABLE IF NOT EXISTS public.itens_pedido (
    pedido_id INTEGER NOT NULL,
    produto_id VARCHAR(10) NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario NUMERIC(10,2) NOT NULL CHECK (preco_unitario >= 0),
    PRIMARY KEY (pedido_id, produto_id),
    CONSTRAINT fk_itens_pedido
        FOREIGN KEY (pedido_id)
        REFERENCES public.pedidos(pedido_id)
);

COMMIT;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name IN ('clientes', 'pedidos', 'itens_pedido')
ORDER BY table_name;
