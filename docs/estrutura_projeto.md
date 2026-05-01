# Estrutura do Projeto

## Visão Geral
Este projeto foi desenvolvido para transformar dados operacionais de vendas em inteligência de negócio por meio de uma pipeline estruturada de coleta, tratamento, modelagem, análise e visualização.

O objetivo principal foi construir uma solução de Business Intelligence aplicada a uma operação comercial varejista, permitindo acompanhamento estratégico de vendas, produtos, vendedores e operação.

---

# Pipeline de Dados

## 1. Coleta de Dados
### Ferramenta:
Google Forms

### Função:
Padronizar o registro operacional de vendas em tempo real.

### Dados coletados:
- Data e hora
- ID da venda
- Vendedor
- Forma de pagamento
- Produto
- Quantidade
- Valor total

---

# 2. Armazenamento Inicial
### Ferramenta:
Google Sheets

### Função:
Centralizar automaticamente os dados brutos coletados via formulário.

### Saída:
- dados_brutos

---

# 3. Tratamento e Padronização
### Ferramenta:
Python (Pandas)

### Arquivos:
- tratamento_dados.py
- validacao_dados.py
- analise_exploratoria.py

### Funções:
- Limpeza de inconsistências
- Padronização de colunas
- Tratamento de valores nulos
- Conversão de tipos
- Remoção de duplicidades
- Validação da base
- Análise exploratória inicial

### Saída:
- dados_tratados

---

# 4. Modelagem Relacional
### Ferramenta:
SQL

### Objetivo:
Estruturar os dados em formato analítico para escalabilidade e consumo em BI.

### Tabelas principais:
- tb_vendas
- tb_itens_venda
- tb_produtos
- tb_vendedores

### Funções:
- Consolidação de vendas
- Separação entre fatos e dimensões
- Queries gerenciais
- Ranking de performance
- Análise operacional

---

# 5. Visualização e Business Intelligence
### Ferramenta:
Power BI

### Dashboards:
- Página 1: Visão Executiva
- Página 2: Produtos & Categorias
- Página 3: Performance de Vendedores
- Página 4: Estoque & Operação

### Principais KPIs:
- Faturamento Total
- Lucro
- Ticket Médio
- Total de Vendas
- Produtos mais vendidos
- Produtos mais lucrativos
- Estoque crítico
- Performance comercial

---

# Estrutura de Pastas
```txt
projeto-bi-varejo/
│── README.md
│
├── images/
│   ├── dashboard_executiva.png
│   ├── dashboard_produtos.png
│   ├── dashboard_vendedores.png
│   ├── dashboard_operacao.png
│   └── modelagem_tabelas.png
│
├── python/
│   ├── tratamento_dados.py
│   ├── validacao_dados.py
│   └── analise_exploratoria.py
│
├── sql/
│   ├── criacao_tb_vendas.sql
│   ├── criacao_tb_itens_venda.sql
│   ├── ranking_produtos.sql
│   ├── ranking_vendedores.sql
│   ├── estoque_critico.sql
│   ├── lucro_produtos.sql
│   └── vendas_por_pagamento.sql
│
└── docs/
    ├── estrutura_projeto.md
    └── dicionario_dados.md