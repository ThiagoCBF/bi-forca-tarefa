-- ==========================================
-- PERFORMANCE DE VENDEDORES
-- Página Performance Comercial
-- ==========================================

SELECT 
    nome_vendedor,
    COUNT(DISTINCT id_venda) AS total_vendas,
    SUM(valor_total_venda) AS faturamento_total,
    AVG(valor_total_venda) AS ticket_medio
FROM tb_vendas
GROUP BY nome_vendedor
ORDER BY faturamento_total DESC;