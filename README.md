# Tech Challenge 1 - Estimativa de Custos Médicos (FIAP)
Curso de Pós-Graduação IA para DEV

Este repositório contém uma aplicação desenvolvida para estimar os **custos médicos individuais** com base em características pessoais, utilizando um modelo preditivo treinado com **XGBoost**.


**Grupo:**
- Bruno Lima da Cruz
- Fernando Fernandes Costa
- Matheus Braz Giudice dos Santos
- Mislene Dalila da Silva
- WELLINGTON CICERO DE CARVALHO 


## Sobre o Projeto

A aplicação foi criada como solução para um desafio da pós-graduação em Inteligência Artificial para Devs. O objetivo era prever o custo médico cobrado por um plano de saúde com base em dados como:

- Idade
- Gênero
- IMC (Índice de Massa Corporal)
- Número de filhos
- Se é fumante
- Região de residência

## Modelo Utilizado

O modelo escolhido foi o **XGBoost Regressor**, por apresentar o melhor desempenho preditivo durante os testes:

- **R² (Coeficiente de Determinação):** 0.88
- **RMSE:** Baixo erro quadrático médio em comparação com outros modelos testados (Regressão Linear, Árvore de Decisão, Random Forest)

O modelo foi treinado com a base de dados pública do Kaggle:  
[Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

## Acesso à Aplicação

A interface web permite que o usuário insira os parâmetros e visualize a **previsão do custo médico** estimado:

🔗 [Acesse aqui a aplicação online](https://techchalange1.onrender.com)

## Tecnologias

- Python
- Flask (API)
- XGBoost (modelo preditivo)
- HTML + CSS + JS (interface frontend)

## Estrutura do Repositório
techchalange1/
├── app/ # API Flask
├── frontend/ # Interface HTML/CSS/JS
├── modelo_xgboost.pkl
└── README.md
