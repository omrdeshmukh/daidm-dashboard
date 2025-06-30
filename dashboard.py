import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter Options")
dept_filter = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
jobrole_filter = st.sidebar.multiselect("Job Role", df["JobRole"].unique(), default=df["JobRole"].unique())
gender_filter = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
marital_filter = st.sidebar.multiselect("Marital Status", df["MaritalStatus"].unique(), default=df["MaritalStatus"].unique())
overtime_filter = st.sidebar.multiselect("OverTime", df["OverTime"].unique(), default=df["OverTime"].unique())

filtered_df = df[
    (df["Department"].isin(dept_filter)) &
    (df["JobRole"].isin(jobrole_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["MaritalStatus"].isin(marital_filter)) &
    (df["OverTime"].isin(overtime_filter))
]

# --- Main Title ---
st.title("📊 HR Attrition Dashboard")
st.markdown("This dashboard helps HR leaders understand patterns of employee attrition through interactive, multidimensional analysis.")

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["📌 Overview", "📉 Attrition Drivers", "🧑‍🤝‍🧑 Demographics", "🌐 3D Analysis"])

# ---------------- OVERVIEW ---------------- #
with tab1:
    st.header("📌 Overview")
    
    st.subheader("1. Attrition Count")
    st.markdown("**Quick snapshot**: How many employees are leaving vs. staying.")
    fig = px.histogram(filtered_df, x="Attrition", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. Attrition by Department")
    st.markdown("Helps identify which departments are most affected by attrition.")
    fig = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("3. Attrition by Job Role")
    st.markdown("Shows which specific job roles have the highest exit rates.")
    fig = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- ATTRITION DRIVERS ---------------- #
with tab2:
    st.header("📉 Drivers of Attrition")

    st.subheader("4. Age vs Attrition")
    st.markdown("Are younger or older employees more likely to leave?")
    fig = px.box(filtered_df, x="Attrition", y="Age", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("5. Monthly Income vs Attrition")
    st.markdown("Examines whether compensation has an effect on attrition.")
    fig = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("6. Years at Company vs Attrition")
    st.markdown("Shows how tenure relates to attrition risk.")
    fig = px.histogram(filtered_df, x="YearsAtCompany", color="Attrition", nbins=30)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("7. Environment Satisfaction")
    st.markdown("Low satisfaction scores may indicate poor working conditions.")
    fig = px.histogram(filtered_df, x="EnvironmentSatisfaction", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("8. Work-Life Balance")
    st.markdown("Helps understand if employees are able to maintain personal balance.")
    fig = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("9. Overtime Status")
    st.markdown("Overworked employees may be more likely to quit.")
    fig = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("10. Job Satisfaction")
    st.markdown("Low job satisfaction is often a precursor to attrition.")
    fig = px.histogram(filtered_df, x="JobSatisfaction", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- DEMOGRAPHICS ---------------- #
with tab3:
    st.header("🧑‍🤝‍🧑 Demographics")

    st.subheader("11. Gender Distribution")
    st.markdown("Understanding if one gender is more prone to leave.")
    fig = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("12. Marital Status")
    st.markdown("Marital status can sometimes correlate with job switching behavior.")
    fig = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("13. Education Field")
    st.markdown("Some academic backgrounds may experience higher turnover.")
    fig = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("14. Business Travel Frequency")
    st.markdown("Excessive travel demands may increase attrition risk.")
    fig = px.histogram(filtered_df, x="BusinessTravel", color="Attrition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("15. Performance Rating")
    st.markdown("Do low or high performers tend to leave?")
    fig = px.histogram(filtered_df, x="PerformanceRating", color="Attrition")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- 3D ANALYSIS ---------------- #
with tab4:
    st.header("🌐 3D Exploratory Visualizations")

    st.subheader("16. Age vs Income vs Working Years")
    st.markdown("A 3D view to understand how age, pay, and experience affect attrition.")
    fig = px.scatter_3d(filtered_df, x="Age", y="MonthlyIncome", z="TotalWorkingYears",
                        color="Attrition", symbol="Attrition")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("17. Years at Company vs Job Satisfaction vs Commute Distance")
    st.markdown("Visualizes the relationship between loyalty, job contentment, and distance.")
    fig = px.scatter_3d(filtered_df, x="YearsAtCompany", y="JobSatisfaction", z="DistanceFromHome",
                        color="Attrition", symbol="Attrition")
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Plotly | Dataset: HR Employee Attrition")
