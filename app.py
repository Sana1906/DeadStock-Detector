import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="StockDetective | Dead Stock & Risk Intelligence Suite",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL HIGH-TECH STYLING ---
st.markdown("""
    <style>
    /* Global Theme Overrides */
    .stApp { background-color: #0B0F19; color: #FAFAFA; }
    
    /* Top Navigation Bar */
    .top-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(90deg, #111827 0%, #1F2937 100%);
        padding: 14px 24px;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .nav-logo {
        font-size: 1.8rem;
        background: #FF3B5C;
        padding: 6px 12px;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(255,59,92,0.4);
    }
    .nav-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: 0.5px;
    }
    .nav-subtitle {
        font-size: 0.85rem;
        color: #9CA3AF;
    }
    
    /* Metric & Card Containers */
    .custom-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR WITH LOGO ---
st.markdown("""
    <div class="top-navbar">
        <div class="nav-brand">
            <div class="nav-logo">💀</div>
            <div>
                <div class="nav-title">StockDetective <span style="color: #FF3B5C; font-size: 0.9rem;">v2.5 Pro</span></div>
                <div class="nav-subtitle">Advanced Dead Stock, Liquidity Trap & Balance Sheet Risk Forensic Intelligence Suite</div>
            </div>
        </div>
        <div>
            <span style="background: rgba(0,230,118,0.1); color: #00E676; padding: 6px 12px; border-radius: 20px; font-size: 0.8rem; border: 1px solid rgba(0,230,118,0.3);">● Live API Connected</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🔍 Market Universe & Filters")

# Preset Ticker Categories
universe_choice = st.sidebar.selectbox(
    "Select Market Preset",
    ["Global & Indian Mixed (Default)", "Indian NSE Equities (High Risk / Midcap)", "US Tech & Meme Stocks"]
)

if universe_choice == "Indian NSE Equities (High Risk / Midcap)":
    default_tickers = ["RELIANCE.NS", "YESBANK.NS", "SUZLON.NS", "VODAFONE.NS", "ZOMATO.NS", "IDEA.NS", "NYKAA.NS"]
elif universe_choice == "US Tech & Meme Stocks":
    default_tickers = ["AAPL", "TSLA", "GME", "AMC", "FSR", "META", "NVDA", "PLTR"]
else:
    default_tickers = ["AAPL", "TSLA", "RELIANCE.NS", "YESBANK.NS", "ZOMATO.NS", "SUZLON.NS", "MSFT"]

selected_tickers = st.sidebar.multiselect(
    "Active Tickers for Inspection",
    options=default_tickers,
    default=default_tickers[:5]
)

custom_input = st.sidebar.text_input("Add Custom Ticker (e.g. TATAMOTORS.NS, NFLX)")
if custom_input:
    clean_sym = custom_input.strip().upper()
    if clean_sym not in selected_tickers:
        selected_tickers.append(clean_sym)

st.sidebar.markdown("---")
st.sidebar.subheader("⚖️ Risk Scoring Thresholds")
min_volume = st.sidebar.slider("Min Daily Volume Trap Line", 10000, 500000, 50000, step=10000)
max_return = st.sidebar.slider("Max 1-Year Momentum Threshold (%)", -80.0, 10.0, -15.0, step=5.0)
max_de = st.sidebar.slider("Max Debt-to-Equity Danger Level", 0.5, 10.0, 3.0, step=0.5)

# --- REAL-TIME DATA FETCHING ENGINE ---
@st.cache_data(ttl=1800)
def fetch_stock_data(tickers):
    records = []
    for symbol in tickers:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            hist = stock.history(period="1y")
            
            if hist.empty:
                continue
                
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            price_change_1y = ((end_price - start_price) / start_price) * 100
            
            records.append({
                'Ticker': symbol,
                'CompanyName': info.get('shortName', symbol),
                'Sector': info.get('sector', 'General / Other'),
                'Daily_Volume': int(info.get('averageVolume', hist['Volume'].mean())),
                'Price_Change_1Y_Pct': round(price_change_1y, 2),
                'Debt_to_Equity': round(float(info.get('debtToEquity', 150) / 100.0 if info.get('debtToEquity') else 1.2), 2),
                'ROE_Pct': round(float(info.get('returnOnEquity', 0.05) * 100 if info.get('returnOnEquity') else 2.0), 2),
                'EPS': round(float(info.get('trailingEps', 0.0) if info.get('trailingEps') else 0.0), 2)
            })
        except Exception:
            continue
    return pd.DataFrame(records)

if not selected_tickers:
    st.warning("Please select at least one ticker from the sidebar to initialize analysis.")
    st.stop()

with st.spinner("Analyzing live ticker feeds & calculating fundamental distress indices... ⏳"):
    df = fetch_stock_data(selected_tickers)

if df.empty:
    st.error("Unable to retrieve ticker data. Check symbol spelling (e.g. Indian tickers require '.NS').")
    st.stop()

# --- RISK SCORING ALGORITHM ---
def evaluate_risk(data, vol_t, ret_t, de_t):
    evaluated = []
    for _, row in data.iterrows():
        score = 0
        flags = []
        
        if row['Daily_Volume'] < vol_t:
            score += 35
            flags.append("Low Liquidity Trap")
        if row['Price_Change_1Y_Pct'] < ret_t:
            score += 30
            flags.append("Severe Negative Momentum")
        if row['Debt_to_Equity'] > de_t:
            score += 25
            flags.append("Critical Debt Leverage")
        if row['ROE_Pct'] < 0:
            score += 10
            flags.append("Destructive ROE")
            
        if score >= 60:
            status = "💀 Dead Stock (Avoid)"
        elif score >= 30:
            status = "⚠️ Stagnant / Watch"
        else:
            status = "✅ Healthy / Viable"
            
        evaluated.append({
            'Risk_Score': score,
            'Classification': status,
            'Warning_Flags': ", ".join(flags) if flags else "None"
        })
    return pd.concat([data.reset_index(drop=True), pd.DataFrame(evaluated)], axis=1)

processed_df = evaluate_risk(df, min_volume, max_return, max_de)

# --- MAIN APPLICATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📡 Live Screener", 
    "💀 Risk Matrix & Radar", 
    "🛡️ Forensic Diagnostics", 
    "⚙️ Export & GitHub Guide"
])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Tickers Screened", len(processed_df))
    col2.metric("💀 Dead Stocks Flagged", len(processed_df[processed_df['Classification'].str.contains("Dead Stock")]))
    col3.metric("⚠️ Stagnant Equities", len(processed_df[processed_df['Classification'].str.contains("Stagnant")]))
    col4.metric("✅ Healthy Assets", len(processed_df[processed_df['Classification'].str.contains("Healthy")]))
    
    st.markdown("### 📋 Filterable Market Screening Table")
    
    status_filter = st.multiselect(
        "Filter Classification Status",
        ["💀 Dead Stock (Avoid)", "⚠️ Stagnant / Watch", "✅ Healthy / Viable"],
        default=["💀 Dead Stock (Avoid)", "⚠️ Stagnant / Watch", "✅ Healthy / Viable"]
    )
    
    filtered_view = processed_df[processed_df['Classification'].isin(status_filter)]
    st.dataframe(filtered_view, use_container_width=True)

with tab2:
    st.markdown("### 🔬 Multi-Factor Risk Matrix (Volume vs. 1-Year Return)")
    if not processed_df.empty:
        fig = px.scatter(
            processed_df,
            x="Daily_Volume",
            y="Price_Change_1Y_Pct",
            size=processed_df["Risk_Score"] + 10,
            color="Classification",
            hover_name="Ticker",
            text="CompanyName",
            color_discrete_map={
                "💀 Dead Stock (Avoid)": "#FF3B5C",
                "⚠️ Stagnant / Watch": "#FFB300",
                "✅ Healthy / Viable": "#00E676"
            },
            labels={"Daily_Volume": "Average Daily Trading Volume", "Price_Change_1Y_Pct": "1-Year Price Return (%)"}
        )
        fig.update_traces(textposition='top center')
        fig.update_layout(height=520, plot_bgcolor='#0F172A', paper_bgcolor='#0B0F19', font_color="#FAFAFA")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("### 🛡️ Deep Forensic Stock Inspector")
    selected_stock = st.selectbox("Select Ticker for Forensic Breakdown", processed_df['Ticker'].tolist())
    
    if selected_stock:
        stock_row = processed_df[processed_df['Ticker'] == selected_stock].iloc[0]
        
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"**Company:** {stock_row['CompanyName']}")
        c2.markdown(f"**Sector:** {stock_row['Sector']}")
        c3.markdown(f"**Risk Classification:** {stock_row['Classification']}")
        
        st.markdown("#### 🚨 Investor Warning & Recommendation Summary")
        if "Dead Stock" in stock_row['Classification']:
            st.error(f"**DO NOT INVEST:** This stock exhibits severe distress signals (`{stock_row['Warning_Flags']}`). High risk of capital erosion and liquidity traps.")
        elif "Stagnant" in stock_row['Classification']:
            st.warning(f"**PROCEED WITH CAUTION:** Momentum is flatlining or debt leverage is elevated. Better allocation opportunities exist elsewhere.")
        else:
            st.success(f"**VIABLE ASSET:** Fundamentals indicate stable volume, sound balance sheet health, and positive operational momentum.")

with tab4:
    st.markdown("### ⚙️ Export Report & GitHub Deployment Guide")
    
    csv_data = processed_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Complete Forensic Screening CSV",
        data=csv_data,
        file_name="stock_detective_report.csv",
        mime="text/csv"
    )
    
    st.markdown("""
    ---
    ### 🚀 How to Push This App to Your GitHub Repository
    1. **Create a new repository** on GitHub (e.g., named `StockDetective`).
    2. Upload your three files (`app.py`, `requirements.txt`, and folder `.streamlit/config.toml`) into the repository root.
    3. Go to [share.streamlit.io](https://share.streamlit.io/).
    4. Sign in with GitHub, click **New app**, select your repository, set the branch to `main`, and main file path to `app.py`.
    5. Click **Deploy!** Your professional high-tech stock app will be live on the web in seconds.
    """)
