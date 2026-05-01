

# docs/dicionario_dados.md

```markdown
# Dicionário de Dados

## Visão Geral
Este documento descreve as principais tabelas e campos utilizados na estrutura analítica do projeto de Business Intelligence para gestão comercial.

---

# Fonte Inicial

# dados_brutos
Base operacional originada do Google Forms e armazenada inicialmente no Google Sheets.

| Coluna | Descrição |
|--------|------------|
| data_hora | Data e hora do registro da venda |
| id_venda | Identificador da venda |
| vendedor | Nome do vendedor |
| forma_pagamento | Método de pagamento utilizado |
| produto | Nome do produto vendido |
| quantidade_produto | Quantidade vendida |
| valor_total | Valor total registrado |

---

# Tabelas Analíticas

# tb_vendas
Tabela fato consolidada por venda.

| Coluna | Descrição |
|--------|------------|
| id_venda | Identificador único da venda |
| data_venda | Data consolidada da venda |
| nome_vendedor | Vendedor responsável |
| forma_pagamento | Método de pagamento |
| valor_total_venda | Valor total da venda |

---

# tb_itens_venda
Tabela transacional detalhada por item.

| Coluna | Descrição |
|--------|------------|
| id_item | Identificador único do item |
| id_venda | Relacionamento com a venda |
| nome_produto | Produto vendido |
| quantidade | Quantidade vendida |
| valor_unitario | Valor unitário do item |

---

# tb_produtos
Tabela dimensão de produtos.

| Coluna | Descrição |
|--------|------------|
| id_produto | Identificador único do produto |
| nome_produto | Nome do produto |
| categoria | Categoria comercial |
| custo | Custo unitário |
| preco_venda | Preço de venda |
| estoque | Quantidade em estoque |

---

# tb_vendedores
Tabela dimensão de vendedores.

| Coluna | Descrição |
|--------|------------|
| id_vendedor | Identificador único |
| nome_vendedor | Nome do vendedor |

---

# Relacionamentos Principais

## tb_vendas
- id_venda → tb_itens_venda.id_venda
- nome_vendedor → tb_vendedores.nome_vendedor

## tb_itens_venda
- nome_produto → tb_produtos.nome_produto

---

# Principais Indicadores Derivados

## Comerciais:
- Faturamento Total
- Ticket Médio
- Total de Vendas
- Faturamento por Vendedor
- Faturamento por Forma de Pagamento

---

## Produtos:
- Quantidade Vendida
- Lucro por Produto
- Performance por Categoria

---

## Operacionais:
- Estoque Atual
- Estoque Crítico
- Potencial de Receita
- Capital em Estoque

---

# Observação
Todos os dados apresentados nesta estrutura podem ser anonimizados para fins de portfólio, mantendo foco na arquitetura, metodologia e capacidade analítica sem exposição de informações sensíveis.