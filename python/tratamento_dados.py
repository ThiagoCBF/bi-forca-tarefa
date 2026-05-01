import pandas as pd

# =========================
# CARREGAR BASE BRUTA
# =========================


df = pd.read_csv("dados_brutos.csv")

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
# RENOMEAR COLUNAS 
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
# REMOVER REGISTROS INVÁLIDOS
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
# REMOVER VALORES NULOS APÓS CONVERSÃO
# =========================
df = df.dropna(subset=["quantidade_produto", "valor_total"])

# =========================
# REMOVER DUPLICIDADES
# =========================
df = df.drop_duplicates()

# =========================
# AJUSTE DE DATA
# =========================
df["data_hora"] = pd.to_datetime(df["data_hora"], errors="coerce")

# =========================
# CRIAR COLUNAS AUXILIARES
# =========================
df["data"] = df["data_hora"].dt.date
df["mes"] = df["data_hora"].dt.month
df["ano"] = df["data_hora"].dt.year

# =========================
# EXPORTAR BASE TRATADA
# =========================
df.to_csv("dados_tratados.csv", index=False)

print("Tratamento concluído com sucesso.")
print(f"Total de registros finais: {len(df)}")