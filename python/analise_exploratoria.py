import pandas as pd

# =========================
# CARREGAMENTO DA BASE
# =========================
# Base de dados tratada utilizada para análise
df = pd.read_csv("base_tratada.csv")

print("========== ANÁLISE EXPLORATÓRIA ==========\n")

# =========================
# FATURAMENTO TOTAL
# =========================
faturamento_total = df["valor_total"].sum()
print(f"Faturamento Total: R$ {faturamento_total:,.2f}")

# =========================
# TOTAL DE TRANSAÇÕES
# =========================
total_transacoes = df["id_venda"].nunique()
print(f"Total de Transações: {total_transacoes}")

# =========================
# TICKET MÉDIO
# =========================
ticket_medio = (
    faturamento_total / total_transacoes
    if total_transacoes > 0 else 0
)

print(f"Ticket Médio: R$ {ticket_medio:,.2f}")

# =========================
# TOP VENDEDORES
# =========================
print("\nTop 5 Vendedores por Faturamento:")

top_vendedores = (
    df.groupby("vendedor")["valor_total"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_vendedores)

# =========================
# TOP PRODUTOS
# =========================
print("\nTop 10 Produtos por Quantidade Vendida:")

top_produtos = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_produtos)

# =========================
# MEIOS DE PAGAMENTO
# =========================
print("\nDistribuição por Forma de Pagamento:")

pagamentos = (
    df.groupby("forma_pagamento")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print(pagamentos)

# =========================
# ANÁLISE TEMPORAL (SE EXISTIR)
# =========================
if "mes" in df.columns:
    print("\nFaturamento por Período:")

    vendas_mes = (
        df.groupby("mes")["valor_total"]
        .sum()
        .sort_index()
    )

    print(vendas_mes)

# =========================
# MÉDIA DE ITENS POR TRANSAÇÃO
# =========================
media_itens = (
    df.groupby("id_venda")["quantidade"]
    .sum()
    .mean()
)

print(f"\nMédia de itens por transação: {media_itens:.2f}")

print("\n========== FIM DA ANÁLISE ==========")