import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Adiciona a pasta raiz ao path para importar o módulo src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model_roi import RealEstateSimulator

st.set_page_config(page_title="Real Estate ROI Predictor", layout="wide")

st.title("🏢 Real Estate ROI Predictor")
st.markdown("Simulador de Retorno sobre Investimento para imóveis de curta temporada (ex: Porto Alegre e Canela).")

# Sidebar para inputs do usuário
st.sidebar.header("Parâmetros do Imóvel")
property_price = st.sidebar.number_input("Valor do Imóvel (R$)", value=500000.0, step=10000.0)
renovation_cost = st.sidebar.number_input("Custo de Reforma (R$)", value=20000.0, step=5000.0)

st.sidebar.header("Receitas e Despesas")
daily_rate = st.sidebar.number_input("Diária Média Estimada (R$)", value=350.0, step=10.0)
monthly_condo = st.sidebar.number_input("Condomínio Mensal (R$)", value=600.0, step=50.0)
annual_iptu = st.sidebar.number_input("IPTU Anual (R$)", value=1500.0, step=100.0)
monthly_maintenance = st.sidebar.number_input("Manutenção Mensal (R$)", value=200.0, step=50.0)

# Instanciando o simulador
simulator = RealEstateSimulator(property_price=property_price, renovation_cost=renovation_cost)

st.write("---")
st.subheader("📊 Análise de Cenários de Ocupação")

# Calculando cenários
scenarios_results = simulator.simulate_scenarios(
    base_daily_rate=daily_rate,
    condo=monthly_condo,
    iptu=annual_iptu,
    maintenance=monthly_maintenance
)

# Convertendo resultados para um DataFrame para facilitar a visualização
df_results = pd.DataFrame(scenarios_results).T
st.dataframe(df_results.style.format("{:.2f}"))

# Gráfico de ROI por Cenário
st.subheader("Comparativo de ROI Anual (%)")
fig = px.bar(
    df_results, 
    y="ROI (%)", 
    text="ROI (%)",
    color=df_results.index,
    labels={"index": "Cenário", "ROI (%)": "Retorno Sobre Investimento (%)"}
)
fig.update_traces(textposition='outside')
st.plotly_chart(fig, use_container_width=True)
