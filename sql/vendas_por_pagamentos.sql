-- ==========================================
-- PERFORMANCE POR FORMA DE PAGAMENTO
-- Página Executiva
-- ==========================================

SELECT 
    forma_pagamento,
    COUNT(DISTINCT id_venda) AS total_vendas,
    SUM(valor_total_venda) AS faturamento_total,
    AVG(valor_total_venda) AS ticket_medio
FROM tb_vendas
GROUP BY forma_pagamento
ORDER BY faturamento_total DESC;