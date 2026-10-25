import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="StockDetective | Dead Stock Analyzer",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #FF4B4B; margin-bottom: 0px; }
    .sub-title { font-size: 1.1rem; color: #A0A0A0; margin-bottom: 20px; }
    .metric-card { background-color: #1E1E1E; padding: 15px; border-radius: 8px; border-left: 4px solid #FF4B4B; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="main-title">💀 StockDetective: Dead Stock & Risk Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Screen, filter, and diagnose unviable, low-liquidity, and zombie stocks to protect your portfolio.</p>', unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🔍 Screening Parameters")

data_source = st.sidebar.radio("Select Data Source", ["Sample Dataset", "Custom CSV Upload"])

@st.cache_data
def load_sample_data():
    return pd.read_csv("sample_stocks.csv")

if data_source == "Sample Dataset":
    df = load_sample_data()
    st.sidebar.success("Loaded built-in sample stock dataset.")
else:
    uploaded_file = st.sidebar.file_uploader("Upload Stock CSV File", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        st.info("Please upload a CSV file or switch to the Sample Dataset.")
        df = load_sample_data()

st.sidebar.markdown("---")
st.sidebar.subheader("Dead Stock Thresholds")
min_volume = st.sidebar.slider("Min Daily Trading Volume", 5000, 100000, 20000, step=5000)
max_return = st.sidebar.slider("Max 1-Year Price Change (%)", -80.0, 10.0, -15.0, step=5.0)
max_de = st.sidebar.slider("Max Debt-to-Equity Ratio", 0.5, 10.0, 3.0, step=0.5)

# --- DATA PROCESSING & RISK SCORING ---
def evaluate_dead_stocks(data, vol_thresh, ret_thresh, de_thresh):
    # Calculate custom Dead Stock Risk Score (0-100)
    # Higher score = higher probability of being a dead/uninvestable stock
    conditions = []
    for _, row in data.iterrows():
        score = 0
        reasons = []
        
        if row['Daily_Volume'] < vol_thresh:
            score += 40
            reasons.append("Low Liquidity")
        if row['Price_Change_1Y_Pct'] < ret_thresh:
            score += 30
            reasons.append("Negative Momentum")
        if row['Debt_to_Equity'] > de_thresh:
            score += 20
            reasons.append("High Leverage")
        if row['ROE_Pct'] < 0:
            score += 10
            reasons.append("Negative ROE")
            
        if score >= 60:
            classification = "💀 Dead Stock (Avoid)"
        elif score >= 30:
            classification = "⚠️ Stagnant / Watch"
        else:
            classification = "✅ Healthy"
            
        conditions.append({
            'Risk_Score': score,
            'Classification': classification,
            'Flags': ", ".join(reasons) if reasons else "None"
        })
    
    res_df = pd.DataFrame(conditions)
    return pd.concat([data.reset_index(drop=True), res_df], axis=1)

processed_df = evaluate_dead_stocks(df, min_volume, max_return, max_de)

# --- MAIN DASHBOARD TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Overview & Screening", "💀 Dead Stock Deep Dive", "⚙️ Data Quality & Audit"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    total_stocks = len(processed_df)
    dead_count = len(processed_df[processed_df['Classification'].str.contains("Dead Stock")])
    stagnant_count = len(processed_df[processed_df['Classification'].str.contains("Stagnant")])
    healthy_count = len(processed_df[processed_df['Classification'].str.contains("Healthy")])
    
    col1.metric("Total Analyzed", total_stocks)
    col2.metric("💀 Dead Stocks", dead_count, delta_color="inverse")
    col3.metric("⚠️ Stagnant Stocks", stagnant_count)
    col4.metric("✅ Healthy Stocks", healthy_count)
    
    st.markdown("### 📋 Filtered Stock Universe")
    
    # Filter selection
    status_filter = st.multiselect(
        "Filter by Classification",
        options=["💀 Dead Stock (Avoid)", "⚠️ Stagnant / Watch", "✅ Healthy"],
        default=["💀 Dead Stock (Avoid)", "⚠️ Stagnant / Watch", "✅ Healthy"]
    )
    
    filtered_view = processed_df[processed_df['Classification'].isin(status_filter)]
    st.dataframe(filtered_view, use_container_width=True)
    
    # Download button
    csv_data = filtered_view.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Screening Report (CSV)",
        data=csv_data,
        file_name="dead_stock_screening_report.csv",
        mime="text/csv"
    )

with tab2:
    st.markdown("### 🔬 Dead Stock Risk Visualizer")
    
    if not processed_df.empty:
        fig = px.scatter(
            processed_df,
            x="Daily_Volume",
            y="Price_Change_1Y_Pct",
            size=processed_df["Risk_Score"] + 5,
            color="Classification",
            hover_name="Ticker",
            text="CompanyName",
            title="Trading Volume vs. 1-Year Price Return (Risk Heatmap)",
            labels={"Daily_Volume": "Daily Trading Volume", "Price_Change_1Y_Pct": "1-Year Price Change (%)"}
        )
        fig.update_traces(textposition='top center')
        fig.update_layout(height=550)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available to display visualizations.")

with tab3:
    st.markdown("### 🛠️ Dataset Data Quality Checks")
    st.markdown("Ensuring data integrity before running investment heuristics.")
    
    null_counts = processed_df.isnull().sum().sum()
    duplicate_rows = processed_df.duplicated().sum()
    
    col_a, col_b = st.columns(2)
    col_a.metric("Missing Values Detected", null_counts)
    col_b.metric("Duplicate Records", duplicate_rows)
    
    if null_counts == 0 and duplicate_rows == 0:
        st.success("Data Quality Status: **PASSED** ✅. No missing or duplicate fields found in the dataset.")
    else:
        st.warning("Data Quality Status: **WARNING** ⚠️. Anomalies detected in source data.")
        
    st.markdown("#### Raw Schema Inspection")
    st.write(processed_df.dtypes)
