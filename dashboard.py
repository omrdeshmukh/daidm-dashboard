import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

# Sidebar Filters
st.sidebar.title("Filter Data")
selected_dept = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
selected_job = st.sidebar.multiselect("Job Role", df["JobRole"].unique(), default=df["JobRole"].unique())
filtered_df = df[(df["Department"].isin(selected_dept)) & (df["JobRole"].isin(selected_job))]

# Main Title
st.title("📊 HR Attrition Dashboard")
st.markdown("This interactive dashboard provides macro and micro-level insights into employee attrition.")

# Tabs
tab1, tab2, tab3 = st.tabs(["📌 Overview", "📉 Attrition Drivers", "🧑‍🤝‍🧑 Demographics"])

# ---------------- OVERVIEW ---------------- #
with tab1:
    st.subheader("1. Overall Attrition Count")
    st.markdown("Compare the number of employees who have left vs. those who stayed.")
    fig = px.histogram(filtered_df, x="Attrition", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. Attrition by Department")
    st.markdown("Shows attrition across departments.")
    fig = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("3. Attrition by Job Role")
    st.markdown("See which roles experience the highest turnover.")
    fig = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("4. Monthly Income Distribution")
    st.markdown("Does pay affect attrition? Let’s find out.")
    fig = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- ATTRITION DRIVERS ---------------- #
with tab2:
    st.subheader("5. Age vs Attrition")
    st.markdown("Do younger or older employees leave more?")
    fig = px.box(filtered_df, x="Attrition", y="Age", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("6. Distance from Home")
    st.markdown("Employees with longer commutes tend to leave more often.")
    fig = px.violin(filtered_df, y="DistanceFromHome", x="Attrition", box=True, color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("7. Overtime vs Attrition")
    st.markdown("Does working overtime relate to higher attrition?")
    fig = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("8. Environment Satisfaction")
    st.markdown("Environment satisfaction score vs attrition.")
    fig = px.histogram(filtered_df, x="EnvironmentSatisfaction", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("9. Performance Rating")
    st.markdown("How performance rating affects attrition.")
    fig = px.histogram(filtered_df, x="PerformanceRating", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("10. Training vs Attrition")
    st.markdown("Is training frequency influencing attrition?")
    fig = px.box(filtered_df, x="Attrition", y="TrainingTimesLastYear", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("11. Years at Company")
    fig = px.histogram(filtered_df, x="YearsAtCompany", color="Attrition", nbins=30)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("12. Stock Option Level")
    fig = px.histogram(filtered_df, x="StockOptionLevel", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- DEMOGRAPHICS ---------------- #
with tab3:
    st.subheader("13. Gender Distribution")
    fig = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("14. Marital Status vs Attrition")
    fig = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("15. Education Field vs Attrition")
    fig = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("16. Business Travel")
    fig = px.histogram(filtered_df, x="BusinessTravel", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("17. Work-Life Balance")
    fig = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("18. Years Since Last Promotion")
    fig = px.box(filtered_df, x="Attrition", y="YearsSinceLastPromotion", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("19. Job Satisfaction vs Attrition")
    fig = px.histogram(filtered_df, x="JobSatisfaction", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("20. Relationship Satisfaction")
    fig = px.histogram(filtered_df, x="RelationshipSatisfaction", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)
