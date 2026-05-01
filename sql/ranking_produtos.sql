-- ==========================================
-- RANKING DE PRODUTOS POR FATURAMENTO
-- Página Produtos & Categorias
-- ==========================================

SELECT 
    nome_produto,
    SUM(quantidade) AS total_vendido,
    SUM(quantidade * valor_unitario) AS faturamento_total
FROM tb_itens_venda
GROUP BY nome_produto
ORDER BY faturamento_total DESC;