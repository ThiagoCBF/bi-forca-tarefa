# Estrutura do Projeto

## Visão Geral

Este documento descreve a organização estrutural da solução de dados desenvolvida para análise comercial no varejo.

A estrutura foi definida com base em boas práticas de projetos de dados, separando claramente as camadas de ingestão, processamento, análise e visualização.

---

## Estrutura de Pastas
solucao-bi-varejo/

├── app_streamlit/
│ └── app.py
│
├── python/
│ ├── tratamento_dados.py
│ ├── analise_exploratoria.py
│ └── validacao_dados.py
│
├── sql/
│ └── queries.sql
│
├── images/
│ ├── dashboard_executiva.png
│ ├── dashboard_produtos.png
│ ├── dashboard_vendedores.png
│ ├── dashboard_operacao.png
│ ├── modelagem_tabelas.png
│ └── streamlit_interface.png
│
├── docs/
│ ├── arquitetura_solucao.md
│ ├── estrutura_projeto.md
│ └── dicionario_dados.md
│
│
├── README.md



---

## Descrição das Camadas

### app_streamlit
Aplicação responsável pelo registro das vendas de forma operacional.

### python
Scripts responsáveis pelo processamento, análise exploratória e validação dos dados.

### sql
Consultas analíticas utilizadas para suporte à camada de BI.

### images
Imagens dos dashboards e modelagem de dados.

### docs
Documentação técnica da solução.

### data
Bases de dados utilizadas no pipeline (não versionadas em produção real).

---

## Boas Práticas Aplicadas

- Separação por camadas de dados
- Organização modular do código
- Isolamento de dados sensíveis
- Estrutura compatível com pipelines de dados
