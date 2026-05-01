# Arquitetura da Solução de Dados

## Visão Geral

Esta solução foi desenvolvida para simular um fluxo completo de dados aplicado à gestão comercial de varejo, integrando coleta operacional, processamento, modelagem e visualização de dados.

O objetivo da arquitetura é transformar dados brutos de vendas em informações estruturadas para análise de negócio e apoio à tomada de decisão.

---

## Arquitetura Geral

O fluxo da solução segue a seguinte estrutura:

Streamlit (Registro de Vendas)
↓
CSV (Camada Transacional)
↓
Python (ETL e Processamento de Dados)
↓
SQL (Modelagem Analítica)
↓
Power BI (Visualização e Dashboards)

---

## Camadas da Solução

### 1. Camada de Ingestão (Streamlit)
Responsável pelo registro operacional das vendas.

- Interface para entrada de dados
- Suporte a múltiplos itens por venda
- Geração de identificador único (id_venda)
- Cálculo automático de valores

---

### 2. Camada de Dados (CSV)
Armazenamento transacional das vendas.

- Base bruta gerada pelo sistema
- Estrutura orientada a eventos de venda
- Histórico completo das transações

---

### 3. Camada de Processamento (Python - ETL)

Responsável pela preparação e qualidade dos dados.

- Padronização de colunas
- Tratamento de tipos de dados
- Remoção de inconsistências
- Criação de variáveis temporais
- Validação da integridade da base

---

### 4. Camada de Modelagem (SQL)

Responsável pela estrutura analítica dos dados.

- Agregações de vendas
- Construção de KPIs
- Análises por produto, vendedor e período
- Suporte à camada de BI

---

### 5. Camada de Visualização (Power BI)

Responsável pela análise gerencial.

- Dashboards executivos
- Análise de produtos
- Performance de vendedores
- Indicadores operacionais

---

## Objetivo da Arquitetura

Garantir um fluxo de dados estruturado, confiável e escalável para suportar análises comerciais e indicadores de performance.

---

## Observação

Todos os dados utilizados nesta solução são fictícios, com finalidade exclusivamente demonstrativa e acadêmica.