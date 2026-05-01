# Dicionário de Dados

## Visão Geral

Este documento descreve os principais campos utilizados na base de dados da solução de análise comercial.

O objetivo é garantir clareza sobre o significado, formato e utilização de cada variável no pipeline de dados.

---

## Tabela: Base de Vendas

### id_venda
- Descrição: Identificador único da transação de venda
- Tipo: String / Inteiro
- Uso: Agrupamento de itens pertencentes à mesma venda

---

### data_hora
- Descrição: Data e hora em que a venda foi registrada
- Tipo: Datetime
- Uso: Análise temporal e construção de indicadores

---

### vendedor
- Descrição: Nome do vendedor responsável pela venda
- Tipo: String
- Uso: Análise de performance comercial

---

### forma_pagamento
- Descrição: Método utilizado no pagamento da venda
- Tipo: String
- Uso: Análise de comportamento de pagamento

---

### produto
- Descrição: Nome do produto vendido
- Tipo: String
- Uso: Análise de mix de produtos

---

### quantidade_produto
- Descrição: Quantidade de unidades vendidas por item
- Tipo: Inteiro
- Uso: Cálculo de volume de vendas

---

### valor_total
- Descrição: Valor total da linha de venda (quantidade × preço)
- Tipo: Float
- Uso: Cálculo de faturamento e KPIs financeiros

---

### data
- Descrição: Data derivada da coluna data_hora
- Tipo: Date
- Uso: Análise diária

---

### mes
- Descrição: Mês extraído da data da venda
- Tipo: Inteiro
- Uso: Análise temporal mensal

---

### ano
- Descrição: Ano da venda
- Tipo: Inteiro
- Uso: Análise histórica

---

## Observação

Todos os dados utilizados nesta estrutura são fictícios e utilizados exclusivamente para fins de estudo e demonstração de pipeline de dados.