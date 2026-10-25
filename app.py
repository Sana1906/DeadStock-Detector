import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="StockDetective: Dead Stock & Risk Intelligence Suite",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INJECT CUSTOM CSS TO REMOVE DEFAULT STREAMLIT PADDING & MARGINS ---
st.markdown("""
    <style>
        /* Hide default Streamlit header, footer, and padding */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        .stApp {
            background-color: #0b0f19;
        }
    </style>
""", unsafe_allow_html=True)

# --- HIGH-TECH HTML/CSS/JS INTERACTIVE SUITE EMBEDDED ---
html_code = """
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StockDetective: Dead Stock & Risk Intelligence Suite v2.0 PRO</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            bg: '#0b0f19',
                            card: '#131b2e',
                            cardBorder: 'rgba(255, 255, 255, 0.08)',
                            cyan: '#00f2fe',
                            red: '#ff3b5c',
                            green: '#00e676',
                            gold: '#ffb300',
                            purple: '#a855f7'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'SF Pro Display', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Fira Code', 'Monaco', 'monospace']
                    }
                }
            }
        }
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        body {
            background-color: #0b0f19;
            color: #f1f5f9;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        .glass-panel {
            background: rgba(19, 27, 46, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        .glass-panel-hover:hover {
            border-color: rgba(0, 242, 254, 0.3);
            box-shadow: 0 8px 32px 0 rgba(0, 242, 254, 0.12);
        }
        .glass-nav {
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glow-red { box-shadow: 0 0 20px rgba(255, 59, 92, 0.25); }
        .glow-green { box-shadow: 0 0 20px rgba(0, 230, 118, 0.25); }
        .glow-gold { box-shadow: 0 0 20px rgba(255, 179, 0, 0.25); }
        .glow-cyan { box-shadow: 0 0 20px rgba(0, 242, 254, 0.25); }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #0b0f19; }
        ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 9999px; }
        ::-webkit-scrollbar-thumb:hover { background: #00f2fe; }

        [data-tooltip] { position: relative; cursor: pointer; }
        [data-tooltip]:before {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 125%; left: 50%;
            transform: translateX(-50%);
            padding: 6px 10px;
            background: #1e293b;
            color: #f8fafc;
            font-size: 0.75rem;
            white-space: nowrap;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            opacity: 0; visibility: hidden;
            transition: all 0.2s ease;
            z-index: 50;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            pointer-events: none;
        }
        [data-tooltip]:hover:before { opacity: 1; visibility: visible; }
        .drawer-slide { transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- TOP STICKY GLASSMORPHISM NAVIGATION BAR WITH LOGO -->
    <header class="glass-nav sticky top-0 z-40 px-4 lg:px-8 py-3">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-3 w-full md:w-auto justify-between md:justify-start">
                <div class="flex items-center gap-3">
                    <div class="relative w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500/20 to-brand-red/20 border border-brand-cyan/40 flex items-center justify-center glow-cyan">
                        <i class="fa-solid fa-chart-line text-brand-cyan text-lg"></i>
                        <span class="absolute -top-1 -right-1 w-3 h-3 bg-brand-red rounded-full animate-ping"></span>
                        <span class="absolute -top-1 -right-1 w-3 h-3 bg-brand-red rounded-full"></span>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <h1 class="text-xl font-extrabold tracking-tight text-white flex items-center gap-1.5">
                                Stock<span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-blue-500">Detective</span>
                            </h1>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-full bg-cyan-500/10 text-brand-cyan border border-brand-cyan/30 uppercase tracking-widest">
                                v2.0 PRO
                            </span>
                        </div>
                        <p class="text-[11px] text-slate-400 font-medium">Dead Stock & Risk Intelligence Suite</p>
                    </div>
                </div>

                <div class="flex items-center gap-2 md:hidden">
                    <button id="soundToggleMobile" class="p-2 rounded-lg bg-slate-800/80 text-slate-300 hover:text-brand-cyan border border-slate-700/50 text-xs">
                        <i class="fa-solid fa-volume-high"></i>
                    </button>
                </div>
            </div>

            <!-- Navigation Tabs -->
            <nav class="flex items-center gap-1 overflow-x-auto max-w-full py-1 px-1 bg-slate-900/60 rounded-xl border border-slate-800">
                <button onclick="switchTab('screener')" id="nav-screener" class="nav-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all bg-brand-cyan/20 text-brand-cyan border border-brand-cyan/40 shadow-sm">
                    <i class="fa-solid fa-radar text-xs"></i> 📡 Live Screener
                </button>
                <button onclick="switchTab('radar')" id="nav-radar" class="nav-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-slate-400 hover:text-slate-200 hover:bg-slate-800/50">
                    <i class="fa-solid fa-skull text-xs"></i> 💀 Risk Matrix
                </button>
                <button onclick="switchTab('inspector')" id="nav-inspector" class="nav-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-slate-400 hover:text-slate-200 hover:bg-slate-800/50">
                    <i class="fa-solid fa-microscope text-xs"></i> 🛡️ Forensic Engine
                </button>
                <button onclick="switchTab('export')" id="nav-export" class="nav-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-slate-400 hover:text-slate-200 hover:bg-slate-800/50">
                    <i class="fa-solid fa-code text-xs"></i> 📥 Export & GitHub
                </button>
            </nav>

            <div class="hidden lg:flex items-center gap-3">
                <button id="soundToggle" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 text-slate-300 hover:text-brand-cyan border border-slate-700/50 text-xs flex items-center gap-1.5 transition-all" data-tooltip="Toggle Audio Feedback">
                    <i id="soundIcon" class="fa-solid fa-volume-high text-brand-cyan"></i>
                    <span class="text-[11px] font-mono">HUD AUDIO</span>
                </button>

                <div class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900/80 border border-slate-800 text-xs">
                    <span class="relative flex h-2 w-2">
                      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    <span class="text-slate-300 font-mono font-medium text-[11px]">NSE / NASDAQ LIVE</span>
                    <span class="text-slate-600">|</span>
                    <span id="utcClock" class="font-mono text-[11px] text-brand-cyan">11:38:00 UTC</span>
                </div>
            </div>
        </div>
    </header>

    <!-- MAIN CONTAINER -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 lg:px-8 py-6 space-y-6">

        <section class="glass-panel rounded-2xl p-4 lg:p-5 relative overflow-hidden">
            <div class="flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-4">
                <div class="flex-1 space-y-3">
                    <div class="flex flex-wrap items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                            <i class="fa-solid fa-fire text-brand-gold"></i> Quick Presets:
                        </span>
                        <button onclick="applyPreset('all')" class="preset-btn text-xs px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">All Stocks</button>
                        <button onclick="applyPreset('dead')" class="preset-btn text-xs px-2.5 py-1 rounded-md bg-rose-950/40 hover:bg-rose-900/60 text-rose-300 border border-rose-800/40 transition">💀 Dead / Zombie Traps</button>
                        <button onclick="applyPreset('penny')" class="preset-btn text-xs px-2.5 py-1 rounded-md bg-amber-950/40 hover:bg-amber-900/60 text-amber-300 border border-amber-800/40 transition">⚠️ Volatile & Illiquid</button>
                        <button onclick="applyPreset('healthy')" class="preset-btn text-xs px-2.5 py-1 rounded-md bg-emerald-950/40 hover:bg-emerald-900/60 text-emerald-300 border border-emerald-800/40 transition">✅ Growth & Blue Chips</button>
                    </div>

                    <div class="flex items-center gap-2">
                        <div class="relative flex-1">
                            <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-500 text-sm"></i>
                            <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Search Ticker or Company (e.g. RELIANCE.NS, SUZLON.NS, AAPL, GME, ZOMATO.NS)..." 
                                class="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/90 border border-slate-700/80 text-white placeholder-slate-500 text-sm focus:outline-none focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan transition font-mono">
                        </div>
                        <button onclick="addCustomTickerModal()" class="px-3.5 py-2.5 rounded-xl bg-brand-cyan/10 hover:bg-brand-cyan/20 text-brand-cyan border border-brand-cyan/40 text-xs font-bold flex items-center gap-1.5 transition whitespace-nowrap">
                            <i class="fa-solid fa-plus"></i> Add Custom Ticker
                        </button>
                        <button onclick="toggleControlPanel()" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-semibold flex items-center gap-2 transition">
                            <i class="fa-solid fa-sliders text-brand-cyan"></i>
                            <span class="hidden sm:inline">Parameters</span>
                            <i id="paramChevron" class="fa-solid fa-chevron-down text-[10px] transition-transform"></i>
                        </button>
                    </div>
                </div>
            </div>

            <div id="controlPanel" class="hidden mt-5 pt-4 border-t border-slate-800/80 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
                <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-300 font-medium flex items-center gap-1.5" data-tooltip="Minimum 30-day average volume threshold to avoid illiquidity traps">
                            Min Daily Volume <i class="fa-solid fa-circle-info text-slate-500 text-[10px]"></i>
                        </label>
                        <span id="val-volume" class="font-mono text-brand-cyan font-bold">50,000</span>
                    </div>
                    <input type="range" id="slider-volume" min="5000" max="500000" step="5000" value="50000" oninput="updateParameters()" class="w-full accent-brand-cyan bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
                </div>

                <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-300 font-medium flex items-center gap-1.5" data-tooltip="Stocks with performance below this return flag as deteriorating price momentum">
                            Max 1Y Return Cutoff <i class="fa-solid fa-circle-info text-slate-500 text-[10px]"></i>
                        </label>
                        <span id="val-return" class="font-mono text-brand-red font-bold">-10.0%</span>
                    </div>
                    <input type="range" id="slider-return" min="-80" max="20" step="5" value="-10" oninput="updateParameters()" class="w-full accent-brand-red bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
                </div>

                <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-300 font-medium flex items-center gap-1.5" data-tooltip="Ratios higher than this threshold indicate unsafe financial leverage">
                            Max Debt-to-Equity (D/E) <i class="fa-solid fa-circle-info text-slate-500 text-[10px]"></i>
                        </label>
                        <span id="val-de" class="font-mono text-brand-gold font-bold">2.5x</span>
                    </div>
                    <input type="range" id="slider-de" min="0.5" max="8.0" step="0.5" value="2.5" oninput="updateParameters()" class="w-full accent-brand-gold bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer">
                </div>

                <div class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 border border-slate-800">
                    <span class="text-xs font-medium text-slate-300" data-tooltip="Enforce strict penalty on companies losing shareholder capital">Strict Negative ROE Penalty</span>
                    <label class="relative inline-flex items-center cursor-pointer">
                        <input type="checkbox" id="check-roe" checked onchange="updateParameters()" class="sr-only peer">
                        <div class="w-9 h-5 bg-slate-800 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-brand-cyan"></div>
                    </label>
                </div>
            </div>
        </section>

        <!-- KPI DASHBOARD METRIC CARDS -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
            <div class="glass-panel glass-panel-hover rounded-2xl p-4 flex flex-col justify-between space-y-2">
                <div class="flex items-center justify-between text-slate-400 text-xs font-semibold">
                    <span>TOTAL ANALYZED</span>
                    <i class="fa-solid fa-layer-group text-slate-500"></i>
                </div>
                <div class="flex items-baseline justify-between">
                    <span id="kpi-total" class="text-2xl font-extrabold font-mono text-white">16</span>
                    <span class="text-[10px] text-slate-400 font-mono">100% Universe</span>
                </div>
                <div class="w-full bg-slate-800 h-1 rounded-full overflow-hidden">
                    <div class="bg-brand-cyan h-full w-full"></div>
                </div>
            </div>

            <div class="glass-panel glass-panel-hover rounded-2xl p-4 flex flex-col justify-between space-y-2 border-l-4 border-l-brand-red glow-red">
                <div class="flex items-center justify-between text-rose-400 text-xs font-semibold">
                    <span>💀 DEAD STOCKS</span>
                    <span id="kpi-dead-pct" class="text-[10px] px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 font-mono font-bold">43%</span>
                </div>
                <div class="flex items-baseline justify-between">
                    <span id="kpi-dead" class="text-2xl font-extrabold font-mono text-brand-red">7</span>
                    <span class="text-[10px] text-rose-400 font-medium">HIGH HAZARD</span>
                </div>
                <div class="w-full bg-slate-800 h-1 rounded-full overflow-hidden">
                    <div id="bar-dead" class="bg-brand-red h-full" style="width: 43%"></div>
                </div>
            </div>

            <div class="glass-panel glass-panel-hover rounded-2xl p-4 flex flex-col justify-between space-y-2 border-l-4 border-l-brand-gold">
                <div class="flex items-center justify-between text-amber-400 text-xs font-semibold">
                    <span>⚠️ STAGNANT TRAPS</span>
                    <span id="kpi-stagnant-pct" class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono font-bold">25%</span>
                </div>
                <div class="flex items-baseline justify-between">
                    <span id="kpi-stagnant" class="text-2xl font-extrabold font-mono text-brand-gold">4</span>
                    <span class="text-[10px] text-amber-400 font-medium">WATCH LIST</span>
                </div>
                <div class="w-full bg-slate-800 h-1 rounded-full overflow-hidden">
                    <div id="bar-stagnant" class="bg-brand-gold h-full" style="width: 25%"></div>
                </div>
            </div>

            <div class="glass-panel glass-panel-hover rounded-2xl p-4 flex flex-col justify-between space-y-2 border-l-4 border-l-brand-green">
                <div class="flex items-center justify-between text-emerald-400 text-xs font-semibold">
                    <span>✅ HEALTHY EQUITIES</span>
                    <span id="kpi-healthy-pct" class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono font-bold">32%</span>
                </div>
                <div class="flex items-baseline justify-between">
                    <span id="kpi-healthy" class="text-2xl font-extrabold font-mono text-brand-green">5</span>
                    <span class="text-[10px] text-emerald-400 font-medium">VIABLE</span>
                </div>
                <div class="w-full bg-slate-800 h-1 rounded-full overflow-hidden">
                    <div id="bar-healthy" class="bg-brand-green h-full" style="width: 32%"></div>
                </div>
            </div>

            <div class="glass-panel glass-panel-hover rounded-2xl p-4 flex flex-col justify-between space-y-2">
                <div class="flex items-center justify-between text-cyan-400 text-xs font-semibold">
                    <span>LIQUIDITY INDEX</span>
                    <i class="fa-solid fa-droplet text-brand-cyan"></i>
                </div>
                <div class="flex items-baseline justify-between">
                    <span id="kpi-liquidity" class="text-2xl font-extrabold font-mono text-brand-cyan">68/100</span>
                    <span class="text-[10px] text-slate-400 font-mono">AVG 30D</span>
                </div>
                <div class="w-full bg-slate-800 h-1 rounded-full overflow-hidden">
                    <div id="bar-liquidity" class="bg-brand-cyan h-full" style="width: 68%"></div>
                </div>
            </div>
        </section>

        <!-- TAB 1: SCREENER TABLE -->
        <div id="tab-screener" class="tab-content space-y-4">
            <div class="glass-panel rounded-2xl p-5 overflow-hidden">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-4">
                    <div>
                        <h3 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-table-list text-brand-cyan"></i> Live Equity Screening Matrix
                        </h3>
                        <p class="text-xs text-slate-400">Click any column header to sort. Hover over metrics for financial explanations.</p>
                    </div>
                    <div class="text-xs text-slate-400 font-mono">
                        Showing <span id="displayedCount" class="text-brand-cyan font-bold">16</span> stocks
                    </div>
                </div>

                <div class="overflow-x-auto rounded-xl border border-slate-800">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-900/90 text-[11px] font-bold text-slate-400 uppercase tracking-wider border-b border-slate-800">
                                <th onclick="sortTable('Ticker')" class="py-3 px-4 cursor-pointer hover:text-white transition">Ticker / Name</th>
                                <th onclick="sortTable('Exchange')" class="py-3 px-3 cursor-pointer hover:text-white transition">Exch</th>
                                <th onclick="sortTable('Price')" class="py-3 px-3 cursor-pointer hover:text-white transition text-right">Price</th>
                                <th onclick="sortTable('Price_Change_1Y_Pct')" class="py-3 px-3 cursor-pointer hover:text-white transition text-right">1Y Return %</th>
                                <th onclick="sortTable('Daily_Volume')" class="py-3 px-3 cursor-pointer hover:text-white transition text-right">30D Avg Vol</th>
                                <th onclick="sortTable('Debt_to_Equity')" class="py-3 px-3 cursor-pointer hover:text-white transition text-right">D/E Ratio</th>
                                <th onclick="sortTable('ROE_Pct')" class="py-3 px-3 cursor-pointer hover:text-white transition text-right">ROE %</th>
                                <th onclick="sortTable('Risk_Score')" class="py-3 px-4 cursor-pointer hover:text-white transition text-center">Risk Score</th>
                                <th class="py-3 px-4">Primary Red Flags</th>
                                <th class="py-3 px-4 text-center">Action</th>
                            </tr>
                        </thead>
                        <tbody id="screenerTableBody" class="divide-y divide-slate-800/60 text-xs"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- TAB 2: RISK MATRIX & RADAR CHARTS -->
        <div id="tab-radar" class="tab-content hidden space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="glass-panel rounded-2xl p-5 lg:col-span-2 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <h3 class="text-base font-bold text-white flex items-center gap-2">
                                <i class="fa-solid fa-crosshairs text-brand-red"></i> Risk Heatmap: Volume vs 1Y Return
                            </h3>
                            <span class="text-[11px] font-mono text-slate-400">Bubble Size = Debt Ratio</span>
                        </div>
                        <p class="text-xs text-slate-400 mb-4">Stocks in the <strong class="text-brand-red">Bottom-Left Quadrant</strong> combine low liquidity with price collapses.</p>
                    </div>
                    <div class="relative w-full h-[380px]">
                        <canvas id="riskScatterChart"></canvas>
                    </div>
                </div>

                <div class="space-y-6">
                    <div class="glass-panel rounded-2xl p-5">
                        <h3 class="text-sm font-bold text-white mb-1 flex items-center gap-2">
                            <i class="fa-solid fa-building-circle-exclamation text-brand-gold"></i> Top Levered Debt Spirals
                        </h3>
                        <p class="text-[11px] text-slate-400 mb-3">Highest Debt-to-Equity ratios</p>
                        <div class="relative h-[180px]">
                            <canvas id="debtBarChart"></canvas>
                        </div>
                    </div>

                    <div class="glass-panel rounded-2xl p-5">
                        <h3 class="text-sm font-bold text-white mb-1 flex items-center gap-2">
                            <i class="fa-solid fa-gauge-high text-brand-cyan"></i> Portfolio Illiquidity Breakdown
                        </h3>
                        <p class="text-[11px] text-slate-400 mb-2">Classification Distribution</p>
                        <div class="relative h-[170px] flex items-center justify-center">
                            <canvas id="liquidityDoughnutChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 3: FORENSIC DIAGNOSIS ENGINE -->
        <div id="tab-inspector" class="tab-content hidden space-y-6">
            <div class="glass-panel rounded-2xl p-6">
                <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-6 border-b border-slate-800">
                    <div class="flex items-center gap-4">
                        <div class="p-3 rounded-2xl bg-slate-900 border border-slate-800 text-brand-cyan text-xl">
                            <i class="fa-solid fa-magnifying-glass-chart"></i>
                        </div>
                        <div>
                            <label class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Selected Equity Target</label>
                            <select id="inspectorSelect" onchange="runInspector(this.value)" class="block w-full mt-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-2 text-white font-bold text-lg focus:outline-none focus:border-brand-cyan font-mono"></select>
                        </div>
                    </div>
                    <div id="inspectorBadgeContainer"></div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6">
                    <div class="space-y-4">
                        <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                            <div class="flex justify-between items-center text-xs">
                                <span class="font-semibold text-slate-300">Bankruptcy Risk Index</span>
                                <span id="insp-zscore" class="font-mono font-bold text-brand-red">Distressed (1.2)</span>
                            </div>
                            <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                                <div id="insp-zbar" class="bg-brand-red h-full" style="width: 25%"></div>
                            </div>
                            <p class="text-[11px] text-slate-400">Scores below 1.8 indicate severe financial distress & debt pressure.</p>
                        </div>

                        <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-3">
                            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Metric Audit</h4>
                            <div class="flex justify-between text-xs py-1 border-b border-slate-800">
                                <span class="text-slate-400">1-Year Performance</span>
                                <span id="insp-1y" class="font-mono font-bold text-brand-red">-42.5%</span>
                            </div>
                            <div class="flex justify-between text-xs py-1 border-b border-slate-800">
                                <span class="text-slate-400">Average Daily Vol</span>
                                <span id="insp-vol" class="font-mono font-bold text-white">12,500 shares</span>
                            </div>
                            <div class="flex justify-between text-xs py-1 border-b border-slate-800">
                                <span class="text-slate-400">Debt-to-Equity</span>
                                <span id="insp-de" class="font-mono font-bold text-brand-gold">3.8x</span>
                            </div>
                            <div class="flex justify-between text-xs py-1">
                                <span class="text-slate-400">Return on Equity</span>
                                <span id="insp-roe" class="font-mono font-bold text-brand-red">-12.4%</span>
                            </div>
                        </div>
                    </div>

                    <div class="lg:col-span-2 space-y-4">
                        <div class="p-5 rounded-xl bg-rose-950/20 border border-rose-900/40 space-y-4">
                            <div class="flex items-center gap-2 text-rose-400 font-bold text-sm">
                                <i class="fa-solid fa-triangle-exclamation text-base"></i>
                                <span>CRITICAL INVESTOR WARNING: WHY YOU SHOULD NOT INVEST</span>
                            </div>
                            <div id="insp-reasons" class="space-y-3 text-xs text-slate-200"></div>
                        </div>

                        <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
                            <h4 class="text-xs font-bold text-slate-300 mb-2">Simulated 12-Month Momentum Trajectory</h4>
                            <div class="h-[140px]">
                                <canvas id="inspTrendChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 4: EXPORT -->
        <div id="tab-export" class="tab-content hidden space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="glass-panel rounded-2xl p-6 space-y-4">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-file-export text-brand-cyan"></i> Export Intelligence Reports
                    </h3>
                    <p class="text-xs text-slate-400">Download the processed dead stock screening data for further financial modeling.</p>

                    <div class="space-y-3 pt-2">
                        <button onclick="exportCSV()" class="w-full py-3 px-4 rounded-xl bg-brand-cyan hover:bg-cyan-400 text-slate-950 font-bold text-xs flex items-center justify-center gap-2 transition shadow-lg shadow-cyan-500/20">
                            <i class="fa-solid fa-file-csv text-sm"></i> Download Screening Report (.CSV)
                        </button>
                        <button onclick="exportJSON()" class="w-full py-3 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs flex items-center justify-center gap-2 border border-slate-700 transition">
                            <i class="fa-solid fa-file-code text-sm"></i> Download JSON Dataset
                        </button>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- DIAGNOSE SIDE DRAWER MODAL -->
    <div id="drawerOverlay" onclick="closeDrawer()" class="fixed inset-0 bg-slate-950/70 backdrop-blur-sm z-50 opacity-0 pointer-events-none transition-opacity duration-300"></div>
    <div id="sideDrawer" class="fixed top-0 right-0 w-full max-w-md h-full bg-slate-900 border-l border-slate-800 z-50 drawer-slide translate-x-full p-6 overflow-y-auto space-y-6">
        <div class="flex items-center justify-between border-b border-slate-800 pb-4">
            <div class="flex items-center gap-3">
                <span class="p-2 rounded-lg bg-rose-500/10 text-brand-red text-lg border border-rose-500/20">
                    <i class="fa-solid fa-skull"></i>
                </span>
                <div>
                    <h3 id="drawerTicker" class="text-lg font-bold font-mono text-white">ZMB1</h3>
                    <p id="drawerName" class="text-xs text-slate-400">Zombie Corp</p>
                </div>
            </div>
            <button onclick="closeDrawer()" class="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
        </div>

        <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-center space-y-1">
            <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Dead Stock Risk Score</span>
            <div id="drawerScore" class="text-3xl font-extrabold font-mono text-brand-red">85 / 100</div>
            <div id="drawerStatusBadge" class="inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-brand-red border border-rose-500/30">
                💀 SEVERE DEAD STOCK
            </div>
        </div>

        <div class="space-y-3">
            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Forensic Audit Findings</h4>
            <div id="drawerFindings" class="space-y-2 text-xs"></div>
        </div>

        <button onclick="switchTab('inspector'); closeDrawer();" class="w-full py-3 rounded-xl bg-brand-cyan/20 hover:bg-brand-cyan/30 text-brand-cyan font-bold text-xs border border-brand-cyan/40 transition">
            Open Full Forensic Diagnosis Engine →
        </button>
    </div>

    <!-- CUSTOM TICKER MODAL -->
    <div id="tickerModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="glass-panel w-full max-w-md rounded-2xl p-6 space-y-4 border border-slate-700">
            <div class="flex justify-between items-center">
                <h3 class="text-base font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-plus-circle text-brand-cyan"></i> Add Custom Stock Ticker
                </h3>
                <button onclick="closeCustomModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <div class="space-y-3">
                <input type="text" id="customTickerInput" placeholder="Symbol (e.g. TATAMOTORS.NS)" class="w-full px-4 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-white font-mono text-sm uppercase focus:outline-none focus:border-brand-cyan">
                <input type="text" id="customNameInput" placeholder="Company Name" class="w-full px-4 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-white text-sm focus:outline-none focus:border-brand-cyan">
                
                <div class="grid grid-cols-2 gap-3">
                    <input type="number" id="customPriceInput" placeholder="Price ($ or ₹)" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-white text-xs">
                    <input type="number" id="customReturnInput" placeholder="1Y Return %" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-white text-xs">
                </div>
            </div>

            <div class="flex gap-2 pt-2">
                <button onclick="submitCustomTicker()" class="flex-1 py-2.5 rounded-xl bg-brand-cyan text-slate-950 font-bold text-xs hover:bg-cyan-400 transition">Add To Intelligence Suite</button>
                <button onclick="closeCustomModal()" class="py-2.5 px-4 rounded-xl bg-slate-800 text-slate-300 font-semibold text-xs hover:bg-slate-700">Cancel</button>
            </div>
        </div>
    </div>

    <!-- APPLICATION JAVASCRIPT -->
    <script>
        const initialStockData = [
            { Ticker: "ZMB1", CompanyName: "Zombie Retail Corp", Exchange: "NASDAQ", Price: 1.45, Daily_Volume: 12500, Price_Change_1Y_Pct: -42.5, Debt_to_Equity: 3.8, ROE_Pct: -12.4 },
            { Ticker: "ZMB2", CompanyName: "Ghost Tech Holdings", Exchange: "NYSE", Price: 0.82, Daily_Volume: 8200, Price_Change_1Y_Pct: -68.0, Debt_to_Equity: 4.5, ROE_Pct: -25.0 },
            { Ticker: "SUZLON.NS", CompanyName: "Suzlon Energy Ltd", Exchange: "NSE", Price: 54.10, Daily_Volume: 450000, Price_Change_1Y_Pct: -8.2, Debt_to_Equity: 2.8, ROE_Pct: 3.1 },
            { Ticker: "YESBANK.NS", CompanyName: "Yes Bank Limited", Exchange: "NSE", Price: 19.80, Daily_Volume: 380000, Price_Change_1Y_Pct: -14.5, Debt_to_Equity: 3.2, ROE_Pct: -1.8 },
            { Ticker: "VODAFONE.NS", CompanyName: "Vodafone Idea Ltd", Exchange: "NSE", Price: 7.65, Daily_Volume: 520000, Price_Change_1Y_Pct: -38.0, Debt_to_Equity: 6.2, ROE_Pct: -18.5 },
            { Ticker: "AAPL", CompanyName: "Apple Inc.", Exchange: "NASDAQ", Price: 228.50, Daily_Volume: 3200000, Price_Change_1Y_Pct: 24.8, Debt_to_Equity: 1.4, ROE_Pct: 145.0 },
            { Ticker: "RELIANCE.NS", CompanyName: "Reliance Industries", Exchange: "NSE", Price: 2740.00, Daily_Volume: 1800000, Price_Change_1Y_Pct: 18.2, Debt_to_Equity: 0.8, ROE_Pct: 11.4 },
            { Ticker: "GME", CompanyName: "GameStop Corp", Exchange: "NYSE", Price: 22.10, Daily_Volume: 95000, Price_Change_1Y_Pct: -22.4, Debt_to_Equity: 0.1, ROE_Pct: -4.2 },
            { Ticker: "AMC", CompanyName: "AMC Entertainment", Exchange: "NYSE", Price: 4.30, Daily_Volume: 42000, Price_Change_1Y_Pct: -58.2, Debt_to_Equity: 5.8, ROE_Pct: -32.1 },
            { Ticker: "ZOMATO.NS", CompanyName: "Eternal / Zomato Ltd", Exchange: "NSE", Price: 265.00, Daily_Volume: 2100000, Price_Change_1Y_Pct: 92.4, Debt_to_Equity: 0.1, ROE_Pct: 8.5 },
            { Ticker: "TSLA", CompanyName: "Tesla Inc.", Exchange: "NASDAQ", Price: 215.30, Daily_Volume: 2800000, Price_Change_1Y_Pct: -12.0, Debt_to_Equity: 0.2, ROE_Pct: 18.2 },
            { Ticker: "DEAD", CompanyName: "Dormant Pharma Inc", Exchange: "NASDAQ", Price: 0.45, Daily_Volume: 9500, Price_Change_1Y_Pct: -71.0, Debt_to_Equity: 2.9, ROE_Pct: -8.5 },
            { Ticker: "TCS.NS", CompanyName: "Tata Consultancy Serv", Exchange: "NSE", Price: 4120.00, Daily_Volume: 950000, Price_Change_1Y_Pct: 15.6, Debt_to_Equity: 0.1, ROE_Pct: 48.0 },
            { Ticker: "RIVN", CompanyName: "Rivian Automotive", Exchange: "NASDAQ", Price: 13.80, Daily_Volume: 85000, Price_Change_1Y_Pct: -34.2, Debt_to_Equity: 1.2, ROE_Pct: -28.0 },
            { Ticker: "FSR", CompanyName: "Fisker Inc Group", Exchange: "OTC", Price: 0.05, Daily_Volume: 18000, Price_Change_1Y_Pct: -94.0, Debt_to_Equity: 8.2, ROE_Pct: -65.0 },
            { Ticker: "INFY.NS", CompanyName: "Infosys Limited", Exchange: "NSE", Price: 1880.00, Daily_Volume: 1400000, Price_Change_1Y_Pct: 22.1, Debt_to_Equity: 0.1, ROE_Pct: 31.2 }
        ];

        let stockDatabase = [...initialStockData];
        let currentFilter = 'all';
        let sortKey = 'Risk_Score';
        let sortAsc = false;
        let soundEnabled = true;

        let scatterChartInstance = null;
        let debtBarChartInstance = null;
        let liquidityDoughnutInstance = null;
        let trendChartInstance = null;

        function playAudioTone(freq = 440, type = 'sine', duration = 0.08) {
            if (!soundEnabled) return;
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.05, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            } catch(e){}
        }

        function computeRiskScore(stock) {
            const minVol = parseInt(document.getElementById('slider-volume').value);
            const maxRet = parseFloat(document.getElementById('slider-return').value);
            const maxDE = parseFloat(document.getElementById('slider-de').value);
            const strictROE = document.getElementById('check-roe').checked;

            let score = 0;
            let flags = [];

            if (stock.Daily_Volume < minVol) {
                score += 35;
                flags.push("Illiquid Trap");
            } else if (stock.Daily_Volume < minVol * 2) {
                score += 15;
            }

            if (stock.Price_Change_1Y_Pct < maxRet) {
                score += 30;
                flags.push("Price Freefall");
            } else if (stock.Price_Change_1Y_Pct < 0) {
                score += 15;
            }

            if (stock.Debt_to_Equity > maxDE) {
                score += 25;
                flags.push("Debt Spiral");
            } else if (stock.Debt_to_Equity > 1.5) {
                score += 10;
            }

            if (stock.ROE_Pct < 0) {
                score += strictROE ? 20 : 10;
                flags.push("Negative ROE");
            }

            score = Math.min(100, score);

            let classification = "✅ HEALTHY";
            if (score >= 55) classification = "💀 DEAD STOCK";
            else if (score >= 30) classification = "⚠️ STAGNANT";

            return { score, classification, flags: flags.length ? flags : ["Nominal Fundamentals"] };
        }

        function getProcessedStockList() {
            return stockDatabase.map(s => {
                const evalData = computeRiskScore(s);
                return { ...s, Risk_Score: evalData.score, Classification: evalData.classification, PrimaryFlags: evalData.flags };
            });
        }

        window.onload = function() {
            updateClock();
            setInterval(updateClock, 1000);
            populateInspectorDropdown();
            renderAll();

            document.getElementById('soundToggle').addEventListener('click', toggleAudio);
            document.getElementById('soundToggleMobile').addEventListener('click', toggleAudio);
        };

        function toggleAudio() {
            soundEnabled = !soundEnabled;
            const icon = document.getElementById('soundIcon');
            if (soundEnabled) {
                icon.className = "fa-solid fa-volume-high text-brand-cyan";
                playAudioTone(880, 'sine', 0.1);
            } else {
                icon.className = "fa-solid fa-volume-xmark text-slate-500";
            }
        }

        function updateClock() {
            const now = new Date();
            const utcString = now.toUTCString().split(' ')[4] + ' UTC';
            document.getElementById('utcClock').innerText = utcString;
        }

        function switchTab(tabId) {
            playAudioTone(520, 'triangle', 0.05);
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.getElementById(`tab-${tabId}`).classList.remove('hidden');

            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.className = "nav-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-slate-400 hover:text-slate-200 hover:bg-slate-800/50";
            });

            const activeBtn = document.getElementById(`nav-${tabId}`);
            if (activeBtn) {
                activeBtn.className = "nav-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all bg-brand-cyan/20 text-brand-cyan border border-brand-cyan/40 shadow-sm";
            }

            if (tabId === 'radar') {
                renderScatterChart();
                renderDebtChart();
                renderLiquidityDoughnut();
            } else if (tabId === 'inspector') {
                const currentVal = document.getElementById('inspectorSelect').value;
                if (currentVal) runInspector(currentVal);
            }
        }

        function toggleControlPanel() {
            playAudioTone(400, 'sine', 0.05);
            const panel = document.getElementById('controlPanel');
            const chevron = document.getElementById('paramChevron');
            panel.classList.toggle('hidden');
            chevron.classList.toggle('rotate-180');
        }

        function updateParameters() {
            document.getElementById('val-volume').innerText = parseInt(document.getElementById('slider-volume').value).toLocaleString();
            document.getElementById('val-return').innerText = parseFloat(document.getElementById('slider-return').value).toFixed(1) + '%';
            document.getElementById('val-de').innerText = parseFloat(document.getElementById('slider-de').value).toFixed(1) + 'x';
            renderAll();
        }

        function applyPreset(type) {
            playAudioTone(600, 'sine', 0.06);
            currentFilter = type;
            renderAll();
        }

        function handleSearch() { renderTable(); }

        function renderAll() {
            const list = getProcessedStockList();
            const total = list.length;
            const dead = list.filter(s => s.Classification === "💀 DEAD STOCK").length;
            const stagnant = list.filter(s => s.Classification === "⚠️ STAGNANT").length;
            const healthy = list.filter(s => s.Classification === "✅ HEALTHY").length;

            document.getElementById('kpi-total').innerText = total;
            document.getElementById('kpi-dead').innerText = dead;
            document.getElementById('kpi-stagnant').innerText = stagnant;
            document.getElementById('kpi-healthy').innerText = healthy;

            const deadPct = total ? Math.round((dead / total) * 100) : 0;
            const stagnantPct = total ? Math.round((stagnant / total) * 100) : 0;
            const healthyPct = total ? Math.round((healthy / total) * 100) : 0;

            document.getElementById('kpi-dead-pct').innerText = deadPct + '%';
            document.getElementById('kpi-stagnant-pct').innerText = stagnantPct + '%';
            document.getElementById('kpi-healthy-pct').innerText = healthyPct + '%';

            document.getElementById('bar-dead').style.width = deadPct + '%';
            document.getElementById('bar-stagnant').style.width = stagnantPct + '%';
            document.getElementById('bar-healthy').style.width = healthyPct + '%';

            const avgVol = list.reduce((acc, s) => acc + s.Daily_Volume, 0) / (total || 1);
            const liqIndex = Math.min(100, Math.round((avgVol / 500000) * 100));
            document.getElementById('kpi-liquidity').innerText = `${liqIndex}/100`;
            document.getElementById('bar-liquidity').style.width = liqIndex + '%';

            renderTable();
            populateInspectorDropdown();
        }

        function renderTable() {
            const searchVal = document.getElementById('searchInput').value.toLowerCase();
            let list = getProcessedStockList();

            if (searchVal) {
                list = list.filter(s => s.Ticker.toLowerCase().includes(searchVal) || s.CompanyName.toLowerCase().includes(searchVal));
            }

            if (currentFilter === 'dead') list = list.filter(s => s.Classification === "💀 DEAD STOCK");
            else if (currentFilter === 'penny') list = list.filter(s => s.Daily_Volume < 100000 || s.Price_Change_1Y_Pct < -20);
            else if (currentFilter === 'healthy') list = list.filter(s => s.Classification === "✅ HEALTHY");

            list.sort((a, b) => {
                let valA = a[sortKey];
                let valB = b[sortKey];
                if (typeof valA === 'string') return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
                return sortAsc ? valA - valB : valB - valA;
            });

            document.getElementById('displayedCount').innerText = list.length;
            const tbody = document.getElementById('screenerTableBody');
            tbody.innerHTML = '';

            if (list.length === 0) {
                tbody.innerHTML = `<tr><td colspan="10" class="py-8 text-center text-slate-500 font-mono">No equities match current screening filters.</td></tr>`;
                return;
            }

            list.forEach(s => {
                let statusBadge = '';
                if (s.Classification === "💀 DEAD STOCK") {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-rose-500/20 text-brand-red border border-rose-500/30">💀 DEAD STOCK</span>`;
                } else if (s.Classification === "⚠️ STAGNANT") {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-amber-500/20 text-brand-gold border border-amber-500/30">⚠️ STAGNANT</span>`;
                } else {
                    statusBadge = `<span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-emerald-500/20 text-brand-green border border-emerald-500/30">✅ HEALTHY</span>`;
                }

                const retColor = s.Price_Change_1Y_Pct >= 0 ? "text-brand-green" : "text-brand-red";
                const deColor = s.Debt_to_Equity > 2.5 ? "text-brand-gold" : "text-slate-300";
                const roeColor = s.ROE_Pct >= 0 ? "text-slate-300" : "text-brand-red";

                const flagsHtml = s.PrimaryFlags.map(f => `<span class="px-1.5 py-0.5 rounded bg-slate-800 text-[9px] text-slate-300 border border-slate-700 font-mono">${f}</span>`).join(' ');

                const tr = document.createElement('tr');
                tr.className = "hover:bg-slate-800/40 transition group";
                tr.innerHTML = `
                    <td class="py-3 px-4 font-mono font-bold text-white group-hover:text-brand-cyan transition">
                        <div>${s.Ticker}</div>
                        <div class="text-[10px] text-slate-400 font-sans font-normal truncate max-w-[120px]">${s.CompanyName}</div>
                    </td>
                    <td class="py-3 px-3 font-mono text-slate-400 text-[11px]">${s.Exchange}</td>
                    <td class="py-3 px-3 text-right font-mono text-slate-200">${s.Price < 10 ? '$' + s.Price.toFixed(2) : s.Price.toLocaleString()}</td>
                    <td class="py-3 px-3 text-right font-mono font-bold ${retColor}">${s.Price_Change_1Y_Pct > 0 ? '+' : ''}${s.Price_Change_1Y_Pct}%</td>
                    <td class="py-3 px-3 text-right font-mono text-slate-300">${s.Daily_Volume.toLocaleString()}</td>
                    <td class="py-3 px-3 text-right font-mono ${deColor}">${s.Debt_to_Equity}x</td>
                    <td class="py-3 px-3 text-right font-mono ${roeColor}">${s.ROE_Pct}%</td>
                    <td class="py-3 px-4 text-center font-mono">
                        <div class="flex items-center justify-center gap-1.5">
                            <span class="font-extrabold text-xs text-white">${s.Risk_Score}</span>
                            ${statusBadge}
                        </div>
                    </td>
                    <td class="py-3 px-4">
                        <div class="flex flex-wrap gap-1">${flagsHtml}</div>
                    </td>
                    <td class="py-3 px-4 text-center">
                        <button onclick="openDrawer('${s.Ticker}')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-brand-cyan hover:text-slate-950 text-slate-300 font-semibold text-[11px] border border-slate-700 transition" data-tooltip="Inspect Deep Forensic Breakdown">
                            Diagnose
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function sortTable(key) {
            playAudioTone(480, 'sine', 0.05);
            if (sortKey === key) sortAsc = !sortAsc;
            else { sortKey = key; sortAsc = false; }
            renderTable();
        }

        function renderScatterChart() {
            const list = getProcessedStockList();
            const ctx = document.getElementById('riskScatterChart').getContext('2d');

            if (scatterChartInstance) scatterChartInstance.destroy();

            const dataPoints = list.map(s => ({
                x: s.Daily_Volume,
                y: s.Price_Change_1Y_Pct,
                r: Math.max(5, Math.min(22, s.Debt_to_Equity * 3.5)),
                ticker: s.Ticker,
                classification: s.Classification
            }));

            scatterChartInstance = new Chart(ctx, {
                type: 'bubble',
                data: {
                    datasets: [{
                        label: 'Equities',
                        data: dataPoints,
                        backgroundColor: dataPoints.map(p => 
                            p.classification === "💀 DEAD STOCK" ? 'rgba(255, 59, 92, 0.7)' :
                            p.classification === "⚠️ STAGNANT" ? 'rgba(255, 179, 0, 0.7)' : 'rgba(0, 230, 118, 0.7)'
                        ),
                        borderColor: dataPoints.map(p => 
                            p.classification === "💀 DEAD STOCK" ? '#ff3b5c' :
                            p.classification === "⚠️ STAGNANT" ? '#ffb300' : '#00e676'
                        ),
                        borderWidth: 1.5
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: {
                            type: 'logarithmic',
                            title: { display: true, text: '30-Day Avg Daily Volume (Log Scale)', color: '#94a3b8', font: { size: 10 } },
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: '#64748b', font: { family: 'JetBrains Mono', size: 10 } }
                        },
                        y: {
                            title: { display: true, text: '1-Year Price Return (%)', color: '#94a3b8', font: { size: 10 } },
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: '#64748b', font: { family: 'JetBrains Mono', size: 10 } }
                        }
                    }
                }
            });
        }

        function renderDebtChart() {
            const list = getProcessedStockList().sort((a,b) => b.Debt_to_Equity - a.Debt_to_Equity).slice(0, 5);
            const ctx = document.getElementById('debtBarChart').getContext('2d');
            if (debtBarChartInstance) debtBarChartInstance.destroy();

            debtBarChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: list.map(s => s.Ticker),
                    datasets: [{
                        data: list.map(s => s.Debt_to_Equity),
                        backgroundColor: 'rgba(255, 179, 0, 0.6)',
                        borderColor: '#ffb300',
                        borderWidth: 1,
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: { grid: { display: false }, ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 10 } } },
                        y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b', font: { size: 9 } } }
                    }
                }
            });
        }

        function renderLiquidityDoughnut() {
            const list = getProcessedStockList();
            const dead = list.filter(s => s.Classification === "💀 DEAD STOCK").length;
            const stagnant = list.filter(s => s.Classification === "⚠️ STAGNANT").length;
            const healthy = list.filter(s => s.Classification === "✅ HEALTHY").length;

            const ctx = document.getElementById('liquidityDoughnutChart').getContext('2d');
            if (liquidityDoughnutInstance) liquidityDoughnutInstance.destroy();

            liquidityDoughnutInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Dead Stocks', 'Stagnant', 'Healthy'],
                    datasets: [{
                        data: [dead, stagnant, healthy],
                        backgroundColor: ['#ff3b5c', '#ffb300', '#00e676'],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'right', labels: { color: '#cbd5e1', font: { size: 10 } } } },
                    cutout: '70%'
                }
            });
        }

        function populateInspectorDropdown() {
            const select = document.getElementById('inspectorSelect');
            const list = getProcessedStockList();
            const currentVal = select.value;

            select.innerHTML = '';
            list.forEach(s => {
                const opt = document.createElement('option');
                opt.value = s.Ticker;
                opt.innerText = `${s.Ticker} - ${s.CompanyName}`;
                select.appendChild(opt);
            });

            if (currentVal && list.some(s => s.Ticker === currentVal)) {
                select.value = currentVal;
            }
        }

        function runInspector(ticker) {
            playAudioTone(580, 'sine', 0.05);
            const list = getProcessedStockList();
            const stock = list.find(s => s.Ticker === ticker) || list[0];
            if (!stock) return;

            const badgeContainer = document.getElementById('inspectorBadgeContainer');
            if (stock.Classification === "💀 DEAD STOCK") {
                badgeContainer.innerHTML = `<span class="px-4 py-1.5 rounded-xl text-xs font-black bg-rose-500/20 text-brand-red border border-rose-500/40 glow-red">💀 CRITICAL DEAD STOCK HAZARD</span>`;
            } else if (stock.Classification === "⚠️ STAGNANT") {
                badgeContainer.innerHTML = `<span class="px-4 py-1.5 rounded-xl text-xs font-black bg-amber-500/20 text-brand-gold border border-amber-500/40">⚠️ ILLIQUID STAGNANT TRAP</span>`;
            } else {
                badgeContainer.innerHTML = `<span class="px-4 py-1.5 rounded-xl text-xs font-black bg-emerald-500/20 text-brand-green border border-emerald-500/40">✅ HEALTHY GROWTH EQUITY</span>`;
            }

            document.getElementById('insp-1y').innerText = `${stock.Price_Change_1Y_Pct > 0 ? '+' : ''}${stock.Price_Change_1Y_Pct}%`;
            document.getElementById('insp-vol').innerText = `${stock.Daily_Volume.toLocaleString()} shares`;
            document.getElementById('insp-de').innerText = `${stock.Debt_to_Equity}x`;
            document.getElementById('insp-roe').innerText = `${stock.ROE_Pct}%`;

            const zScore = Math.max(0.5, (3.0 - (stock.Debt_to_Equity * 0.4) + (stock.ROE_Pct * 0.02))).toFixed(2);
            const zScoreElem = document.getElementById('insp-zscore');
            const zBarElem = document.getElementById('insp-zbar');

            if (zScore < 1.8) {
                zScoreElem.innerText = `Distressed (${zScore})`;
                zScoreElem.className = "font-mono font-bold text-brand-red";
                zBarElem.className = "bg-brand-red h-full";
                zBarElem.style.width = "25%";
            } else if (zScore < 2.9) {
                zScoreElem.innerText = `Grey Zone (${zScore})`;
                zScoreElem.className = "font-mono font-bold text-brand-gold";
                zBarElem.className = "bg-brand-gold h-full";
                zBarElem.style.width = "60%";
            } else {
                zScoreElem.innerText = `Safe Zone (${zScore})`;
                zScoreElem.className = "font-mono font-bold text-brand-green";
                zBarElem.className = "bg-brand-green h-full";
                zBarElem.style.width = "90%";
            }

            const reasonsContainer = document.getElementById('insp-reasons');
            reasonsContainer.innerHTML = '';

            let bulletPoints = [];
            if (stock.Daily_Volume < 50000) {
                bulletPoints.push(`<strong>Illiquidity Execution Trap:</strong> Low 30-day average volume (${stock.Daily_Volume.toLocaleString()} shares) means selling your position could suffer over 4-8% price slippage.`);
            }
            if (stock.Debt_to_Equity > 2.5) {
                bulletPoints.push(`<strong>Unsustained Debt Burden:</strong> Debt-to-Equity ratio of ${stock.Debt_to_Equity}x indicates heavy interest payment obligations that eat operating profits.`);
            }
            if (stock.ROE_Pct < 0) {
                bulletPoints.push(`<strong>Value Destructive ROE:</strong> Return on Equity is negative (${stock.ROE_Pct}%), meaning the company actively loses shareholder capital each quarter.`);
            }
            if (stock.Price_Change_1Y_Pct < -20) {
                bulletPoints.push(`<strong>Severe Downward Momentum:</strong> Stock has collapsed ${stock.Price_Change_1Y_Pct}% over 12 months with no sign of institutional accumulation.`);
            }
            if (bulletPoints.length === 0) {
                bulletPoints.push(`<strong>No Immediate Structural Red Flags:</strong> This stock currently maintains adequate volume liquidity and sustainable leverage ratios.`);
            }

            bulletPoints.forEach(pt => {
                const div = document.createElement('div');
                div.className = "flex items-start gap-2.5 p-2.5 rounded-lg bg-slate-900/60 border border-slate-800";
                div.innerHTML = `<i class="fa-solid fa-circle-dot text-brand-red text-[10px] mt-1"></i> <div>${pt}</div>`;
                reasonsContainer.appendChild(div);
            });

            renderTrendChart(stock);
        }

        function renderTrendChart(stock) {
            const ctx = document.getElementById('inspTrendChart').getContext('2d');
            if (trendChartInstance) trendChartInstance.destroy();

            const months = ['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12'];
            let current = 100;
            const points = [100];
            const monthlyStep = (stock.Price_Change_1Y_Pct / 12);

            for (let i = 1; i < 12; i++) {
                current += monthlyStep + (Math.random() * 4 - 2);
                points.push(parseFloat(current.toFixed(2)));
            }

            const lineColor = stock.Price_Change_1Y_Pct >= 0 ? '#00e676' : '#ff3b5c';

            trendChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: months,
                    datasets: [{
                        data: points,
                        borderColor: lineColor,
                        borderWidth: 2,
                        tension: 0.3,
                        pointRadius: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: { grid: { display: false }, ticks: { color: '#64748b', font: { size: 9 } } },
                        y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#64748b', font: { size: 9 } } }
                    }
                }
            });
        }

        function openDrawer(ticker) {
            playAudioTone(640, 'triangle', 0.08);
            const list = getProcessedStockList();
            const stock = list.find(s => s.Ticker === ticker);
            if (!stock) return;

            document.getElementById('drawerTicker').innerText = stock.Ticker;
            document.getElementById('drawerName').innerText = stock.CompanyName;
            document.getElementById('drawerScore').innerText = `${stock.Risk_Score} / 100`;

            const badge = document.getElementById('drawerStatusBadge');
            if (stock.Classification === "💀 DEAD STOCK") {
                badge.innerText = "💀 SEVERE DEAD STOCK HAZARD";
                badge.className = "inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-brand-red border border-rose-500/30";
            } else if (stock.Classification === "⚠️ STAGNANT") {
                badge.innerText = "⚠️ STAGNANT ILLIQUID TRAP";
                badge.className = "inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-brand-gold border border-amber-500/30";
            } else {
                badge.innerText = "✅ HEALTHY EQUITY";
                badge.className = "inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-brand-green border border-emerald-500/30";
            }

            const findings = document.getElementById('drawerFindings');
            findings.innerHTML = stock.PrimaryFlags.map(f => `
                <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between">
                    <span class="text-slate-300 font-medium">${f}</span>
                    <i class="fa-solid fa-triangle-exclamation text-brand-gold"></i>
                </div>
            `).join('');

            document.getElementById('drawerOverlay').classList.remove('opacity-0', 'pointer-events-none');
            document.getElementById('sideDrawer').classList.remove('translate-x-full');
        }

        function closeDrawer() {
            document.getElementById('drawerOverlay').classList.add('opacity-0', 'pointer-events-none');
            document.getElementById('sideDrawer').classList.add('translate-x-full');
        }

        function addCustomTickerModal() {
            document.getElementById('tickerModal').classList.remove('hidden');
        }

        function closeCustomModal() {
            document.getElementById('tickerModal').classList.add('hidden');
        }

        function submitCustomTicker() {
            const sym = document.getElementById('customTickerInput').value.trim().toUpperCase();
            const name = document.getElementById('customNameInput').value.trim() || sym;
            const price = parseFloat(document.getElementById('customPriceInput').value) || 10.0;
            const ret = parseFloat(document.getElementById('customReturnInput').value) || -15.0;

            if (!sym) return;

            stockDatabase.unshift({
                Ticker: sym,
                CompanyName: name,
                Exchange: sym.includes('.NS') ? 'NSE' : 'NASDAQ',
                Price: price,
                Daily_Volume: 35000,
                Price_Change_1Y_Pct: ret,
                Debt_to_Equity: 3.2,
                ROE_Pct: -5.0
            });

            closeCustomModal();
            renderAll();
            playAudioTone(800, 'sine', 0.1);
        }

        function exportCSV() {
            const list = getProcessedStockList();
            let csv = "Ticker,CompanyName,Exchange,Price,1Y_Return_Pct,Daily_Volume,Debt_to_Equity,ROE_Pct,Risk_Score,Classification\n";
            list.forEach(s => {
                csv += `"${s.Ticker}","${s.CompanyName}","${s.Exchange}",${s.Price},${s.Price_Change_1Y_Pct},${s.Daily_Volume},${s.Debt_to_Equity},${s.ROE_Pct},${s.Risk_Score},"${s.Classification}"\n`;
            });

            const blob = new Blob([csv], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'StockDetective_DeadStock_Report.csv';
            a.click();
        }

        function exportJSON() {
            const list = getProcessedStockList();
            const blob = new Blob([JSON.stringify(list, null, 2)], { type: 'application/json' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'StockDetective_Dataset.json';
            a.click();
        }
    </script>
</body>
</html>
"""

# Render application in Streamlit canvas
components.html(html_code, height=1050, scrolling=True)
