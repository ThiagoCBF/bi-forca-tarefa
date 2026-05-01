-- =========================================
-- ANÁLISE DE VENDAS - SOLUÇÃO BI VAREJO
-- =========================================

-- =========================
-- 1. FATURAMENTO TOTAL
-- =========================
SELECT 
    SUM(valor_total) AS faturamento_total
FROM base_tratada;

-- =========================
-- 2. TOTAL DE TRANSAÇÕES
-- =========================
SELECT 
    COUNT(DISTINCT id_venda) AS total_transacoes
FROM base_tratada;

-- =========================
-- 3. TICKET MÉDIO
-- =========================
SELECT 
    SUM(valor_total) / COUNT(DISTINCT id_venda) AS ticket_medio
FROM base_tratada;

-- =========================
-- 4. TOP VENDEDORES
-- =========================
SELECT 
    vendedor,
    SUM(valor_total) AS faturamento
FROM base_tratada
GROUP BY vendedor
ORDER BY faturamento DESC
LIMIT 5;

-- =========================
-- 5. TOP PRODUTOS
-- =========================
SELECT 
    produto,
    SUM(quantidade_produto) AS total_vendido
FROM base_tratada
GROUP BY produto
ORDER BY total_vendido DESC
LIMIT 10;

-- =========================
-- 6. FATURAMENTO POR FORMA DE PAGAMENTO
-- =========================
SELECT 
    forma_pagamento,
    SUM(valor_total) AS total_pago
FROM base_tratada
GROUP BY forma_pagamento
ORDER BY total_pago DESC;

-- =========================
-- 7. ANÁLISE TEMPORAL (MENSAL)
-- =========================
SELECT 
    mes,
    SUM(valor_total) AS faturamento_mes
FROM base_tratada
GROUP BY mes
ORDER BY mes;

-- =========================
-- 8. MÉDIA DE ITENS POR VENDA
-- =========================
SELECT 
    AVG(total_itens) AS media_itens_por_venda
FROM (
    SELECT 
        id_venda,
        SUM(quantidade_produto) AS total_itens
    FROM base_tratada
    GROUP BY id_venda
) AS subquery;