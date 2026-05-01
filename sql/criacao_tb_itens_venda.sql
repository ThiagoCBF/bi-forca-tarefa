-- ==========================================
-- CRIAÇÃO DA TABELA DE ITENS DE VENDA
-- Cada linha representa um item/produto vendido
-- ==========================================

CREATE TABLE tb_itens_venda AS
SELECT 
    ROW_NUMBER() OVER () AS id_item,
    id_venda,
    produto AS nome_produto,
    quantidade_produto AS quantidade,
    (valor_total / NULLIF(quantidade_produto, 0)) AS valor_unitario
FROM dados_tratados;