import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Ethiopia Financial Inclusion Forecast Dashboard")

df = pd.read_csv("data/processed/enriched_ethiopia_fi_unified_data.csv")

# 1. Key metrics
st.header("Current Status (2024)")
col1, col2 = st.columns(2)
col1.metric("Account Ownership", "49%", "+3pp since 2021")
col2.metric("Digital Payments", "~35%", "")

# 2. Trends
st.header("Historical Trends")
fig_trend = px.line(
    df[(df['record_type']=='observation') & (df['indicator_code'].isin(['ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT']))],
    x='observation_date', y='value_numeric', color='indicator_code'
)
st.plotly_chart(fig_trend)

# 3. Event timeline (simple)
st.header("Major Events")
events = df[df['record_type']=='event']
st.dataframe(events[['event_date','category','description']])

# 4. Forecast (from Task 4 – load or hardcode)
st.header("Forecast 2025–2027")
forecast_df = pd.DataFrame({   # example
    'Year': [2025,2026,2027],
    'Baseline': [51, 52.5, 54],
    'Optimistic': [53, 56, 59],
    'Pessimistic': [50, 51, 52]
})
fig_forecast = px.line(forecast_df, x='Year', y=['Baseline','Optimistic','Pessimistic'])
st.plotly_chart(fig_forecast)

# scenario selector
scenario = st.selectbox("Scenario", ["Baseline", "Optimistic", "Pessimistic"])