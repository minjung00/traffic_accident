import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/minjung00/traffic_accident/main/%EB%8F%84%EB%A1%9C%EA%B5%90%ED%86%B5%EA%B3%B5%EB%8B%A8_%EC%82%AC%EA%B3%A0%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B5%90%ED%86%B5%EC%82%AC%EA%B3%A0%20%ED%86%B5%EA%B3%84_20211231.csv", encoding='cp949')

col1, col2 = st.columns(2)
# seaborn
col1.title("Seaborn")
plot = sns.lineplot(df, x='사고유형대분류', y='사고건수')
col1.pyplot(plot.figure)

col2.title("Plotly")
col2.plotly_chart(fig, use_container_width=True)
fig = px.line(df, x='사고유형대분류', y='사고건수')

fig.show()
