import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("EA.csv")
    return df

df = load_data()
st.title("📊 HR Attrition Dashboard")
st.markdown("Welcome Director! This dashboard provides insights into why employees are leaving the company.")

# --- Filters ---
with st.sidebar:
    st.header("🔍 Filter Data")
    department = st.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
    job_role = st.multiselect("Select Job Role", df["JobRole"].unique(), default=df["JobRole"].unique())

filtered_df = df[(df["Department"].isin(department)) & (df["JobRole"].isin(job_role))]

# --- 1. Attrition Distribution ---
st.subheader("1. Overall Attrition Count")
st.markdown("Shows how many employees have left vs stayed.")
fig1 = px.histogram(filtered_df, x="Attrition", color="Attrition", barmode="group")
st.plotly_chart(fig1)

# --- 2. Attrition by Department ---
st.subheader("2. Attrition by Department")
st.markdown("Understand which departments have the most attrition.")
fig2 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig2)

# --- 3. Age Distribution by Attrition ---
st.subheader("3. Age Distribution of Employees")
st.markdown("Younger or older staff? This chart helps you spot age-related attrition.")
fig3 = px.box(filtered_df, x="Attrition", y="Age", color="Attrition")
st.plotly_chart(fig3)

# (Add more charts below following this pattern...)
