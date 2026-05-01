-- ==========================================
-- CRIAÇÃO DA TABELA DE VENDAS CONSOLIDADAS
-- Uma venda pode ter múltiplos produtos,
-- então consolidamos por id_venda
-- ==========================================

CREATE TABLE tb_vendas AS
SELECT 
    id_venda,
    MIN(data_hora) AS data_venda,
    vendedor AS nome_vendedor,
    forma_pagamento,
    MAX(valor_total) AS valor_total_venda
FROM dados_tratados
GROUP BY 
    id_venda,
    vendedor,
    forma_pagamento;