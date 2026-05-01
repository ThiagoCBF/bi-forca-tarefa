-- ==========================================
-- PRODUTOS COM ESTOQUE CRÍTICO
-- Página Operação
-- ==========================================

SELECT 
    id_produto,
    nome_produto,
    categoria,
    estoque
FROM tb_produtos
WHERE estoque < 10
ORDER BY estoque ASC;