-- ==========================================
-- LUCRO TOTAL POR PRODUTO
-- Considera custo x venda
-- Página Produtos / Margem
-- ==========================================

SELECT 
    p.nome_produto,
    SUM((iv.valor_unitario - p.custo) * iv.quantidade) AS lucro_total
FROM tb_itens_venda iv
JOIN tb_produtos p 
    ON iv.nome_produto = p.nome_produto
GROUP BY p.nome_produto
ORDER BY lucro_total DESC;