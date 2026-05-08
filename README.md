# 🏢 Real Estate ROI Predictor & Market Analytics

## 🎯 O Problema de Negócio
Investidores imobiliários frequentemente tomam decisões baseadas em intuição ou em planilhas estáticas que não consideram a volatilidade do mercado. O desafio é avaliar com precisão o Retorno Sobre o Investimento (ROI) em diferentes cenários, especialmente em locações de curta temporada, equilibrando custos de manutenção, taxas de ocupação flutuantes e a valorização anual do ativo.

## 💡 A Solução
Este projeto é uma aplicação de inteligência imobiliária ponta a ponta. Ele fornece um motor de cálculo dinâmico e um dashboard interativo para simular e prever a rentabilidade de imóveis em mercados-chave (ex: Porto Alegre e Canela). 

A ferramenta permite:
* **Análise de Cenários:** Comparação em tempo real de lucratividade sob diferentes taxas de ocupação (ex: Airbnb vs. Locação Tradicional).
* **Modelagem Estatística:** Utilização de inferência bayesiana para estimar a probabilidade de retorno e testes A/B para comparar o desempenho histórico de diferentes perfis de imóveis.
* **Apoio à Decisão:** Visualização clara de fluxo de caixa, tempo de payback e projeção de valorização patrimonial.

## 🛠️ Stack Tecnológico e Arquitetura
* **Data Science & Analytics:** `Python`, `Pandas`, `SciPy` (Estatística Bayesiana e Testes de Hipótese).
* **Desenvolvimento Frontend / Visualização:** `Streamlit`, `Plotly`.
* **MLOps / Infraestrutura:** `Docker` para empacotamento da aplicação, garantindo reprodutibilidade em qualquer ambiente.

## 🚀 Como Executar o Projeto Localmente

**Pré-requisitos:** Docker instalado na máquina.

1. Clone o repositório:
`git clone https://github.com/SEU-USUARIO/real-estate-roi-predictor.git`

2. Construa a imagem Docker:
`docker build -t real-estate-app .`

3. Rode o contêiner:
`docker run -p 8501:8501 real-estate-app`

4. Acesse o dashboard no seu navegador através de `http://localhost:8501`.

## 👤 Sobre o Autor
Desenvolvido por **Adriano Belluco**, Especialista em Dados e Machine Learning Engineer, unindo profunda expertise analítica e modelagem matemática a uma sólida experiência em precificação de ativos e negócios imobiliários.
