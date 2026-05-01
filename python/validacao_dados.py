import pandas as pd

# =========================
# CARREGAR BASE TRATADA
# =========================
df = pd.read_csv("dados_tratados.csv")

print("========== VALIDAÇÃO DE DADOS ==========\n")

# =========================
# VALORES NULOS
# =========================
print("Valores nulos por coluna:")
print(df.isnull().sum())

# =========================
# DUPLICIDADES
# =========================
duplicados = df.duplicated().sum()
print(f"\nTotal de linhas duplicadas: {duplicados}")

# =========================
# IDs DE VENDA AUSENTES
# =========================
ids_nulos = df["id_venda"].isnull().sum()
print(f"\nIDs de venda nulos: {ids_nulos}")

# =========================
# VALORES NEGATIVOS
# =========================
valores_negativos = (df["valor_total"] < 0).sum()
print(f"\nRegistros com valor_total negativo: {valores_negativos}")

# =========================
# QUANTIDADES INVÁLIDAS
# =========================
quantidade_invalida = (df["quantidade_produto"] <= 0).sum()
print(f"\nRegistros com quantidade inválida: {quantidade_invalida}")

# =========================
# FORMAS DE PAGAMENTO
# =========================
print("\nFormas de pagamento encontradas:")
print(df["forma_pagamento"].value_counts())

# =========================
# VENDEDORES
# =========================
print("\nVendedores encontrados:")
print(df["vendedor"].value_counts())

# =========================
# RESUMO
# =========================
print("\n========== RESUMO FINAL ==========")

if duplicados == 0 and valores_negativos == 0 and quantidade_invalida == 0:
    print("Base validada com sucesso. Nenhum problema crítico encontrado.")
else:
    print("Atenção: Foram encontrados pontos para revisão.")