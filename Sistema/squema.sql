CREATE TABLE IF NOT EXISTS clientes (
    id    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome  VARCHAR(50) NOT NULL,
    cpf   VARCHAR(11) NOT NULL UNIQUE        
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome        VARCHAR(50)  NOT NULL,
    cpf         VARCHAR(11)  NOT NULL UNIQUE,
    senha_hash  VARCHAR(100) NOT NULL          
);

CREATE TABLE IF NOT EXISTS quartos (
    id             INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    numero_quarto  INTEGER NOT NULL UNIQUE,
    status         VARCHAR(10) NOT NULL DEFAULT 'LIVRE'
                   CHECK (status IN ('LIVRE', 'OCUPADO', 'LIMPEZA'))
);

CREATE TABLE IF NOT EXISTS hospedagens (
    id              INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cliente      INTEGER NOT NULL REFERENCES clientes(id),             
    numero_quarto   INTEGER NOT NULL REFERENCES quartos(numero_quarto),
    entrada         TIMESTAMP NOT NULL,
    saida_prevista  TIMESTAMP NOT NULL,
    saida           TIMESTAMP,                 
    valor_total     NUMERIC(10,2)             
);

CREATE TABLE IF NOT EXISTS gastos (
    id              INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_hospedagem   INTEGER NOT NULL REFERENCES hospedagens(id) ON DELETE CASCADE,
    nome            VARCHAR(30) NOT NULL,
    valor_unitario  NUMERIC(10,2) NOT NULL CHECK (valor_unitario > 0),
    quantidade      INTEGER NOT NULL CHECK (quantidade > 0)
);

CREATE INDEX IF NOT EXISTS idx_gastos_hospedagem ON gastos (id_hospedagem);