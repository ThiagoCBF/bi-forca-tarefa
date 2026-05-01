import pandas as pd

# =========================
# CARREGAR BASE TRATADA
# =========================
df = pd.read_csv("dados_tratados.csv")

print("========== ANÁLISE EXPLORATÓRIA ==========\n")

# =========================
# FATURAMENTO TOTAL
# =========================
faturamento_total = df["valor_total"].sum()
print(f"Faturamento Total: R$ {faturamento_total:,.2f}")

# =========================
# TOTAL DE VENDAS
# =========================
total_vendas = df["id_venda"].nunique()
print(f"Total de Vendas: {total_vendas}")

# =========================
# TICKET MÉDIO
# =========================
ticket_medio = faturamento_total / total_vendas if total_vendas > 0 else 0
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
    df.groupby("produto")["quantidade_produto"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_produtos)

# =========================
# FORMAS DE PAGAMENTO
# =========================
print("\nDistribuição por Forma de Pagamento:")
pagamentos = (
    df.groupby("forma_pagamento")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)
print(pagamentos)

# =========================
# VENDAS POR MÊS
# =========================
if "mes" in df.columns:
    print("\nFaturamento por Mês:")
    vendas_mes = (
        df.groupby("mes")["valor_total"]
        .sum()
        .sort_index()
    )
    print(vendas_mes)

# =========================
# PRODUTOS POR VENDA
# =========================
media_itens_venda = df.groupby("id_venda")["quantidade_produto"].sum().mean()
print(f"\nMédia de itens por venda: {media_itens_venda:.2f}")

print("\n========== FIM DA ANÁLISE ==========")