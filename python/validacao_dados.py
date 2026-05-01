import pandas as pd

# =========================
# CARREGAMENTO DA BASE TRATADA
# =========================
df = pd.read_csv("base_tratada.csv")

print("========== VALIDAÇÃO DE QUALIDADE DE DADOS ==========\n")

# =========================
# VALORES AUSENTES (NULLS)
# =========================
print("Quantidade de valores nulos por coluna:")
print(df.isnull().sum())

# =========================
# DUPLICIDADE DE REGISTROS
# =========================
duplicados = df.duplicated().sum()
print(f"\nTotal de registros duplicados: {duplicados}")

# =========================
# VALIDAÇÃO DE ID DE TRANSAÇÃO
# =========================
ids_nulos = df["id_venda"].isnull().sum()
print(f"\nIDs de transação ausentes: {ids_nulos}")

# =========================
# VALIDAÇÃO DE VALORES FINANCEIROS
# =========================
valores_negativos = (df["valor_total"] < 0).sum()
print(f"\nRegistros com valor negativo: {valores_negativos}")

# =========================
# VALIDAÇÃO DE QUANTIDADE
# =========================
quantidade_invalida = (df["quantidade_produto"] <= 0).sum()
print(f"\nRegistros com quantidade inválida: {quantidade_invalida}")

# =========================
# DISTRIBUIÇÃO DE FORMAS DE PAGAMENTO
# =========================
print("\nDistribuição de formas de pagamento:")
print(df["forma_pagamento"].value_counts())

# =========================
# DISTRIBUIÇÃO DE VENDEDORES
# =========================
print("\nDistribuição de vendedores:")
print(df["vendedor"].value_counts())

# =========================
# RESUMO DE QUALIDADE
# =========================
print("\n========== RESUMO FINAL ==========")

if duplicados == 0 and valores_negativos == 0 and quantidade_invalida == 0:
    print("Base validada com sucesso. Nenhum problema crítico identificado.")
else:
    print("Atenção: inconsistências encontradas na base de dados.")