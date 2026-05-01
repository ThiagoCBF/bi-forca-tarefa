import pandas as pd

# =========================
# CARREGAMENTO DA BASE BRUTA
# =========================
# Base transacional gerada pelo sistema de vendas
df = pd.read_csv("base_bruta.csv")

# =========================
# PADRONIZAÇÃO DE COLUNAS
# =========================
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# =========================
# NORMALIZAÇÃO DE NOMES DE COLUNAS
# =========================
df = df.rename(columns={
    "data_hora": "data_hora",
    "id_venda": "id_venda",
    "vendedor": "vendedor",
    "formapagamento": "forma_pagamento",
    "produto": "produto",
    "quantidadeproduto": "quantidade_produto",
    "valortotal": "valor_total"
})

# =========================
# REMOÇÃO DE REGISTROS INVÁLIDOS
# =========================
df = df.dropna(subset=["id_venda", "produto", "vendedor"])

# =========================
# PADRONIZAÇÃO DE TEXTO
# =========================
df["vendedor"] = df["vendedor"].astype(str).str.strip().str.title()
df["produto"] = df["produto"].astype(str).str.strip().str.title()
df["forma_pagamento"] = df["forma_pagamento"].astype(str).str.strip().str.upper()

# =========================
# CONVERSÃO DE TIPOS
# =========================
df["quantidade_produto"] = pd.to_numeric(df["quantidade_produto"], errors="coerce")
df["valor_total"] = pd.to_numeric(df["valor_total"], errors="coerce")

# =========================
# LIMPEZA APÓS CONVERSÃO
# =========================
df = df.dropna(subset=["quantidade_produto", "valor_total"])

# =========================
# REMOÇÃO DE DUPLICADOS
# =========================
df = df.drop_duplicates()

# =========================
# TRATAMENTO DE DATA
# =========================
df["data_hora"] = pd.to_datetime(df["data_hora"], errors="coerce")

# =========================
# CRIAÇÃO DE FEATURES TEMPORAIS
# =========================
df["data"] = df["data_hora"].dt.date
df["mes"] = df["data_hora"].dt.month
df["ano"] = df["data_hora"].dt.year

# =========================
# EXPORTAÇÃO DA BASE TRATADA
# =========================
df.to_csv("base_tratada.csv", index=False)

print("Pipeline de tratamento concluído com sucesso.")
print(f"Total de registros processados: {len(df)}")