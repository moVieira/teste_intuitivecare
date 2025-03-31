CREATE TABLE demonstracoes_contabeis (
    data DATE,
    reg_ans INT, 
    cd_conta_contabil INT, 
    descricao VARCHAR(150), 
    vl_saldo_inicial DECIMAL(15,2), 
    vl_saldo_final DECIMAL(15,2), 
    PRIMARY KEY (data, reg_ans, cd_conta_contabil) 
);
CREATE TABLE dados_cadastrais (
    registro_ans INT PRIMARY KEY,
    cnpj TEXT,
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf TEXT,
    cep TEXT
);







