import streamlit as st
import pandas as pd
from datetime import datetime
import os

# =========================
# CONFIGURAÇÕES DO SISTEMA
# =========================
ARQUIVO_DADOS = "base_vendas.csv"

VENDEDORES = ["Vendedor A", "Vendedor B", "Vendedor C", "Vendedor D"]

FORMAS_PAGAMENTO = ["PIX", "CRÉDITO", "DÉBITO", "DINHEIRO"]

# =========================
# CATÁLOGO DE PRODUTOS (FICTÍCIO PARA DEMONSTRAÇÃO)
# =========================
PRODUTOS_PRECOS = {
    "Produto Alpha": 349.90,
    "Produto Beta": 329.90,
    "Produto Gamma": 389.90,
    "Produto Delta": 419.90,
    "Produto Epsilon": 649.90,
    "Produto Zeta": 189.90,
    "Produto Eta": 49.90,
    "Produto Theta": 44.90,
    "Produto Iota": 59.90,
    "Produto Kappa": 79.90,
    "Produto Lambda": 39.90,
    "Produto Sigma": 19.90
}

# =========================
# INICIALIZAÇÃO DO CARRINHO
# =========================
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# =========================
# INTERFACE
# =========================
st.set_page_config(page_title="Sistema de Vendas", layout="wide")

st.title("Sistema de Registro de Vendas")

# =========================
# SIDEBAR - CONTROLE DA VENDA
# =========================
with st.sidebar:
    st.header("Dados da Venda")

    vendedor = st.selectbox("Vendedor", VENDEDORES)
    forma_pagamento = st.selectbox("Forma de Pagamento", FORMAS_PAGAMENTO)

    st.divider()

    if st.button("Limpar Carrinho"):
        st.session_state.carrinho = []
        st.rerun()

# =========================
# SELEÇÃO DE PRODUTOS
# =========================
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    produto = st.selectbox("Produto", list(PRODUTOS_PRECOS.keys()))

with col2:
    quantidade = st.number_input("Quantidade", min_value=1, value=1)

with col3:
    preco_unitario = round(PRODUTOS_PRECOS[produto], 2)
    st.write("Preço")
    st.write(f"R$ {preco_unitario:.2f}")

# =========================
# ADICIONAR AO CARRINHO
# =========================
if st.button("Adicionar ao Carrinho ➕", use_container_width=True):

    item = {
        "produto": produto,
        "quantidade": quantidade,
        "preco_unitario": round(preco_unitario, 2),
        "subtotal": round(preco_unitario * quantidade, 2)
    }

    st.session_state.carrinho.append(item)
    st.toast("Item adicionado com sucesso!")

# =========================
# CARRINHO
# =========================
st.divider()
st.subheader("Carrinho de Compras")

if st.session_state.carrinho:

    df = pd.DataFrame(st.session_state.carrinho)

    st.table(df)

    total_venda = round(df["subtotal"].sum(), 2)
    st.metric("Total da Venda", f"R$ {total_venda:.2f}")

    # =========================
    # FINALIZAR VENDA
    # =========================
    if st.button("Finalizar Venda", type="primary", use_container_width=True):

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id_venda = datetime.now().strftime("%Y%m%d%H%M%S")

        registros = []

        for item in st.session_state.carrinho:
            registros.append({
                "data_hora": data_hora,
                "id_venda": id_venda,
                "vendedor": vendedor,
                "forma_pagamento": forma_pagamento,
                "produto": item["produto"],
                "quantidade": item["quantidade"],
                "valor_total": round(item["subtotal"], 2)
            })

        df_final = pd.DataFrame(registros)

        if os.path.exists(ARQUIVO_DADOS):
            df_final.to_csv(ARQUIVO_DADOS, mode="a", index=False, header=False)
        else:
            df_final.to_csv(ARQUIVO_DADOS, index=False)

        st.success(f"Venda {id_venda} registrada com sucesso!")

        st.session_state.carrinho = []
        st.balloons()

else:
    st.info("Carrinho vazio. Adicione produtos para iniciar a venda.")