import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as bg
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="StockDetective | Dead Stock & Risk Intelligence Suite",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HIGH-TECH DARK THEME & GLASSMORPHISM CSS ---
st.markdown("""
    <style>
    /* Dark Theme Core */
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Top Header Navbar */
    .top-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(19, 27, 46, 0.85);
        backdrop-filter: blur(16px);
        padding: 16px 24px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .brand-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .brand-cyan { color: #00f2fe; }
    .brand-red { color: #ff3b5c; }
    
    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background: rgba(19, 27, 46, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 16px;
        border-radius: 14px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    /* Native Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #131b2e;
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .stTabs [data-baseweb="tab"] {
        height: 42px;
        border-radius: 8px;
        color: #94a3b8;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 0 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 242, 254, 0.15) !important;
        color: #00f2fe !important;
        border: 1px solid rgba(0, 242, 254, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
st.markdown("""
    <div class="top-navbar">
        <div class="brand-title">
            <span>💀</span>
            <span>Stock<span class="brand-cyan">Detective</span> <span style="font-size: 0.8rem; background: rgba(0,242,254,0.1); color: #00f2fe; padding: 2px 8px; border-radius: 10px; border: 1px solid rgba(0,242,254,0.3);">v2.0 PRO</span></span>
        </div>
        <div style="font-size: 0.85rem; color: #00e676; font-family: monospace;">
            ● LIVE YFINANCE API CONNECTED
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🔍 Market Universe & Controls")

preset_choice = st.sidebar.selectbox(
    "Select Market Preset",
    ["High Risk / Midcap Equities", "Indian NSE Equities", "US Tech & Volatile Equities"]
)

if preset_choice == "Indian NSE Equities":
    default_tickers = ["RELIANCE.NS", "SUZLON.NS", "YESBANK.NS", "VODAFONE.NS", "ZOMATO.NS", "TCS.NS", "INFY.NS"]
elif preset_choice == "US Tech & Volatile Equities":
    default_tickers = ["AAPL", "TSLA", "GME", "AMC", "FSR", "RIVN", "DEAD"]
else:
    default_tickers = ["SUZLON.NS", "YESBANK.NS", "VODAFONE.NS", "AAPL", "TSLA", "GME", "ZOMATO.NS", "RELIANCE.NS"]

selected_tickers = st.sidebar.multiselect(
    "Active Tickers for Inspection",
    options=default_tickers,
    default=default_tickers
)

custom_ticker = st.sidebar.text_input("Add Custom Ticker (e.g. TATAMOTORS.NS, NVDA)")
if custom_ticker:
    clean_sym = custom_ticker.strip().upper()
    if clean_sym not in selected_tickers:
        selected_tickers.append(clean_sym)

st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Dead Stock Risk Thresholds")
min_volume = st.sidebar.slider("Min 30D Volume Trap Line", 5000, 500000, 50000, step=5000)
max_return = st.sidebar.slider("Max 1Y Return Cutoff (%)", -80.0, 20.0, -10.0, step=5.0)
max_de = st.sidebar.slider("Max Debt-to-Equity Danger Level", 0.5, 8.0, 2.5, step=0.5)

# --- REAL-TIME DATA FETCHING ENGINE ---
@st.cache_data(ttl=1800)
def fetch_stock_data(tickers):
    records = []
    for symbol in tickers:
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="1y")
            info = stock.info
            
            if hist.empty:
                continue
                
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            price_change_1y = ((end_price - start_price) / start_price) * 100
            
            avg_vol = int(info.get('averageVolume', hist['Volume'].mean()))
            de_ratio = float(info.get('debtToEquity', 150) / 100.0 if info.get('debtToEquity') else 1.5)
            roe = float(info.get('returnOnEquity', 0.02) * 100 if info.get('returnOnEquity') else -5.0)
            
            records.append({
                'Ticker': symbol,
                'CompanyName': info.get('shortName', symbol),
                'Exchange': 'NSE' if '.NS' in symbol else 'NASDAQ/NYSE',
                'Price': round(end_price, 2),
                'Daily_Volume': avg_vol,
                'Price_Change_1Y_Pct': round(price_change_1y, 2),
                'Debt_to_Equity': round(de_ratio, 2),
                'ROE_Pct': round(roe, 2)
            })
        except Exception:
            continue
    return pd.DataFrame(records)

if not selected_tickers:
    st.warning("Please select at least one stock ticker from the sidebar.")
    st.stop()

with st.spinner("Fetching live market data from Yahoo Finance... ⏳"):
    df = fetch_stock_data(selected_tickers)

if df.empty:
    st.error("Unable to load stock data. Check symbol spelling (NSE stocks require '.NS').")
    st.stop()

# --- RISK SCORING ALGORITHM ---
def evaluate_risk(data, vol_t, ret_t, de_t):
    evaluated = []
    for _, row in data.iterrows():
        score = 0
        flags = []
        
        if row['Daily_Volume'] < vol_t:
            score += 35
            flags.append("Illiquid Trap")
        if row['Price_Change_1Y_Pct'] < ret_t:
            score += 30
            flags.append("Price Freefall")
        if row['Debt_to_Equity'] > de_t:
            score += 25
            flags.append("Debt Spiral")
        if row['ROE_Pct'] < 0:
            score += 10
            flags.append("Negative ROE")
            
        if score >= 55:
            status = "💀 DEAD STOCK"
        elif score >= 30:
            status = "⚠️ STAGNANT"
        else:
            status = "✅ HEALTHY"
            
        evaluated.append({
            'Risk_Score': score,
            'Classification': status,
            'PrimaryFlags': ", ".join(flags) if flags else "Nominal Fundamentals"
        })
    return pd.concat([data.reset_index(drop=True), pd.DataFrame(evaluated)], axis=1)

processed_df = evaluate_risk(df, min_volume, max_return, max_de)

# --- KPI METRIC CARDS ---
c1, c2, c3, c4, c5 = st.columns(5)
total = len(processed_df)
dead = len(processed_df[processed_df['Classification'] == "💀 DEAD STOCK"])
stagnant = len(processed_df[processed_df['Classification'] == "⚠️ STAGNANT"])
healthy = len(processed_df[processed_df['Classification'] == "✅ HEALTHY"])

c1.metric("TOTAL ANALYZED", total)
c2.metric("💀 DEAD STOCKS", dead, delta=f"{round((dead/total)*100)}% hazard" if total else "0%", delta_color="inverse")
c3.metric("⚠️ STAGNANT", stagnant)
c4.metric("✅ HEALTHY", healthy)
c5.metric("LIQUIDITY INDEX", f"{min(100, int(processed_df['Daily_Volume'].mean()/5000))}/100")

st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN NATIVE TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📡 Live Screener", 
    "💀 Risk Matrix & Radar", 
    "🛡️ Forensic Engine", 
    "📥 Export Data"
])

with tab1:
    st.markdown("### 📋 Filterable Market Screening Matrix")
    
    col_filter, col_search = st.columns([2, 2])
    with col_filter:
        status_filter = st.multiselect(
            "Filter Classification",
            ["💀 DEAD STOCK", "⚠️ STAGNANT", "✅ HEALTHY"],
            default=["💀 DEAD STOCK", "⚠️ STAGNANT", "✅ HEALTHY"]
        )
    with col_search:
        search_query = st.text_input("Search Ticker or Company Name", "")
        
    filtered = processed_df[processed_df['Classification'].isin(status_filter)]
    if search_query:
        filtered = filtered[filtered['Ticker'].str.contains(search_query.upper()) | filtered['CompanyName'].str.contains(search_query, case=False)]
        
    st.dataframe(
        filtered,
        column_config={
            "Price_Change_1Y_Pct": st.column_config.NumberColumn("1Y Return %", format="%.2f%%"),
            "Daily_Volume": st.column_config.NumberColumn("30D Avg Vol", format="%d"),
            "Debt_to_Equity": st.column_config.NumberColumn("D/E Ratio", format="%.2fx"),
            "Risk_Score": st.column_config.ProgressColumn("Risk Score", min_value=0, max_value=100, format="%d/100")
        },
        use_container_width=True
    )

with tab2:
    st.markdown("### 🔬 Multi-Factor Risk Matrix (Volume vs. 1-Year Return)")
    
    fig = px.scatter(
        processed_df,
        x="Daily_Volume",
        y="Price_Change_1Y_Pct",
        size=processed_df["Risk_Score"] + 10,
        color="Classification",
        hover_name="Ticker",
        hover_data=["CompanyName", "Debt_to_Equity", "Risk_Score"],
        color_discrete_map={
            "💀 DEAD STOCK": "#ff3b5c",
            "⚠️ STAGNANT": "#ffb300",
            "✅ HEALTHY": "#00e676"
        },
        labels={"Daily_Volume": "30-Day Avg Volume (Log Scale)", "Price_Change_1Y_Pct": "1-Year Return (%)"},
        log_x=True
    )
    fig.update_layout(
        height=500,
        plot_bgcolor='#131b2e',
        paper_bgcolor='#0b0f19',
        font_color="#f1f5f9"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("### 🛡️ Deep Forensic Stock Inspector")
    selected_stock = st.selectbox("Select Equity Target to Diagnose", processed_df['Ticker'].tolist())
    
    if selected_stock:
        stock_row = processed_df[processed_df['Ticker'] == selected_stock].iloc[0]
        
        ic1, ic2 = st.columns([1, 2])
        
        with ic1:
            st.markdown(f"#### **{stock_row['Ticker']}**")
            st.caption(stock_row['CompanyName'])
            st.markdown(f"**Classification:** `{stock_row['Classification']}`")
            st.markdown(f"**Risk Score:** `{stock_row['Risk_Score']} / 100`")
            st.markdown(f"**1Y Return:** `{stock_row['Price_Change_1Y_Pct']}%`")
            st.markdown(f"**Avg Vol:** `{stock_row['Daily_Volume']:,}`")
            st.markdown(f"**Debt/Equity:** `{stock_row['Debt_to_Equity']}x`")
            st.markdown(f"**ROE:** `{stock_row['ROE_Pct']}%`")
            
        with ic2:
            st.markdown("#### 🚨 Forensic Audit Warnings")
            if stock_row['Risk_Score'] >= 55:
                st.error(f"**CRITICAL HAZARD:** {stock_row['PrimaryFlags']}. High risk of capital loss and liquidity entrapment.")
            elif stock_row['Risk_Score'] >= 30:
                st.warning(f"**ELEVATED RISK:** {stock_row['PrimaryFlags']}. Poor momentum or financial leverage detected.")
            else:
                st.success("**STABLE ASSET:** No structural red flags detected.")
                
            # Historical trend chart
            hist_data = yf.Ticker(selected_stock).history(period="1y")
            if not hist_data.empty:
                fig_line = px.line(
                    hist_data, 
                    y="Close", 
                    title=f"12-Month Price Trajectory ({selected_stock})",
                    color_discrete_sequence=["#ff3b5c" if stock_row['Price_Change_1Y_Pct'] < 0 else "#00e676"]
                )
                fig_line.update_layout(height=250, plot_bgcolor='#131b2e', paper_bgcolor='#0b0f19', font_color="#f1f5f9")
                st.plotly_chart(fig_line, use_container_width=True)

with tab4:
    st.markdown("### 📥 Export Intelligence Reports")
    csv_bytes = processed_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Report (.CSV)",
        data=csv_bytes,
        file_name="stock_detective_report.csv",
        mime="text/csv"
    )
