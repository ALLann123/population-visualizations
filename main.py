#!/usr/bin/python3 
import streamlit as st
import pandas as pd
from my_visuals import display
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Population Visuals", layout="wide", page_icon="🤖")
st.title("Population (1955-2020) 👨‍👩‍👧‍👧")
st.write("In our dataframe we selected five countries to visualize: United States, India, China,Indonesia, and Brazil")

# DataFrame section
st.subheader("DataFrame")
df = display()
st.dataframe(df)

# Data Editor section
st.subheader("Data Editor")
editable_df = st.data_editor(df)

# Metrics section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))

# Visualization columns
col1, col2 = st.columns(2)

st.subheader("2. Line Chart")
st.line_chart(df, y_label="Population", x_label="Year")

with col1:
    st.subheader("1. Bar Chart")
    st.bar_chart(df, x_label="Year", y_label="Population", stack=False)

with col2:
    st.subheader("Last 5 Years")
    df_last_five_years = df[df.index.isin([2020, 2019, 2018, 2017, 2016])]
    st.bar_chart(df_last_five_years, stack=False)


st.subheader("3. Pie Chart")
# Get 2020 data (row), transpose to make countries the rows
df_2020 = df.loc[2020].reset_index()
df_2020.columns = ['Country', 'Population']
fig = px.pie(
    df_2020,
    names='Country',
    values='Population',
    title='Population in 2020 (%)'
)
st.plotly_chart(fig, use_container_width=True)

