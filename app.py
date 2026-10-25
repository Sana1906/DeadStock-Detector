import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="StockDetective | Live Dead Stock Analyzer",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #FF4B4B; margin-bottom: 0px; }
    .sub-title { font-size: 1.1rem; color: #A0A0A0; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="main-title">💀 StockDetective: Live Dead Stock & Risk Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Screen real-time market data to diagnose unviable, low-liquidity, and zombie stocks.</p>', unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🔍 Live Ticker Configuration")

# Default stock universe (Mix of global tech and Indian NSE stocks)
default_tickers = [
    "AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", 
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "ZOMATO.NS", "VODAFONE.NS"
]

selected_tickers = st.sidebar.multiselect(
    "Select or Add Stock Tickers",
    options=default_tickers,
    default=default_tickers[:6]
)

custom_ticker_input = st.sidebar.text_input("Add Custom Ticker (e.g., NVDA, TATAMOTORS.NS)")
if custom_ticker_input:
    clean_ticker = custom_ticker_input.strip().upper()
    if clean_ticker not in selected_tickers:
        selected_tickers.append(clean_ticker)

st.sidebar.markdown("---")
st.sidebar.subheader("Dead Stock Risk Thresholds")
min_volume = st.sidebar.slider("Min Daily Trading Volume", 10000, 1000000, 100000, step=50000)
max_return = st.sidebar.slider("Max 1-Year Price Change (%)", -80.0, 10.0, -10.0, step=5.0)
max_de = st.sidebar.slider("Max Debt-to-Equity Ratio", 0.5, 10.0, 3.0, step=0.5)

# --- REAL-TIME DATA FETCHING WITH CACHING ---
@st.cache_data(ttl=3600)  # Cache data for 1 hour to prevent hitting rate limits
def fetch_live_stock_data(tickers):
    stock_records = []
    
    for symbol in tickers:
        try:
            ticker_obj = yfinance_wrapper(symbol) # helper logic
            stock = yf.Ticker(symbol)
            info = stock.info
            
            # Fetch 1 year historical data for price performance
            hist = stock.history(period="1y")
            
            if hist.empty:
                continue
                
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            price_change_1y = ((end_price - start_price) / start_price) * 100
            
            # Extract basic fundamental attributes safely
            company_name = info.get('shortName', symbol)
            sector = info.get('sector', 'Unknown')
            avg_volume = info.get('averageVolume', hist['Volume'].mean())
            debt_to_equity = info.get('debtToEquity', 1.5) / 100.0 if info.get('debtToEquity') else 1.0
            roe = info.get('returnOnEquity', 0.1) * 100 if info.get('returnOnEquity') else 5.0
            eps = info.get('trailingEps', 0.0)
            
            stock_records.append({
                'Ticker': symbol,
                'CompanyName': company_name,
                'Sector': sector,
                'Daily_Volume': int(avg_volume if not pd.isna(avg_volume) else 100000),
                'Price_Change_1Y_Pct': round(price_change_1y, 2),
                'Debt_to_Equity': round(float(debt_to_equity), 2),
                'ROE_Pct': round(float(roe), 2),
                'EPS': round(float(eps if eps else 0.0), 2)
            })
        except Exception as e:
            # Skip invalid tickers gracefully
            continue
            
    return pd.DataFrame(stock_records)

def yfinance_wrapper(sym):
    return sym

# Load data when user initiates
if not selected_tickers:
    st.warning("Please select at least one stock ticker from the sidebar.")
    st.stop()

with st.spinner("Fetching live market data from Yahoo Finance... ⏳"):
    df = fetch_live_stock_data(selected_tickers)

if df.empty:
    st.error("Could not fetch data for the selected tickers. Please verify symbol names (e.g., NSE stocks require '.NS' suffix).")
    st.stop()

# --- EVALUATION & RISK SCORING ENGINE ---
def evaluate_dead_stocks(data, vol_thresh, ret_thresh, de_thresh):
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

# --- DASHBOARD LAYOUT ---
tab1, tab2, tab3 = st.tabs(["📊 Live Screener Overview", "💀 Risk Heatmap", "⚙️ Raw Data & Diagnostics"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    total_stocks = len(processed_df)
    dead_count = len(processed_df[processed_df['Classification'].str.contains("Dead Stock")])
    stagnant_count = len(processed_df[processed_df['Classification'].str.contains("Stagnant")])
    healthy_count = len(processed_df[processed_df['Classification'].str.contains("Healthy")])
    
    col1.metric("Analyzed Tickers", total_stocks)
    col2.metric("💀 Dead Stocks", dead_count)
    col3.metric("⚠️ Stagnant Stocks", stagnant_count)
    col4.metric("✅ Healthy Stocks", healthy_count)
    
    st.markdown("### 📋 Filtered Market Results")
    
    status_filter = st.multiselect(
        "Filter by Status",
        options=["💀 Dead Stock (Avoid)", "⚠️ Stagnant / Watch", "✅ Healthy"],
        default=["💀 Dead Stock (Avoid)", "⚠️ Stagnant / Watch", "✅ Healthy"]
    )
    
    filtered_view = processed_df[processed_df['Classification'].isin(status_filter)]
    st.dataframe(filtered_view, use_container_width=True)
    
    csv_data = filtered_view.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Live Screening Report (CSV)",
        data=csv_data,
        file_name="live_dead_stock_report.csv",
        mime="text/csv"
    )

with tab2:
    st.markdown("### 🔬 Risk Matrix: Volume vs. 1-Year Price Return")
    if not processed_df.empty:
        fig = px.scatter(
            processed_df,
            x="Daily_Volume",
            y="Price_Change_1Y_Pct",
            size=processed_df["Risk_Score"] + 5,
            color="Classification",
            hover_name="Ticker",
            text="CompanyName",
            title="Live Market Position vs Risk Score",
            labels={"Daily_Volume": "Average Daily Volume", "Price_Change_1Y_Pct": "1-Year Price Change (%)"}
        )
        fig.update_traces(textposition='top center')
        fig.update_layout(height=550)
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("### 🛠️ Execution Diagnostics")
    st.write("Fetched live metrics successfully from Yahoo Finance API.")
    st.write(processed_df.describe())
