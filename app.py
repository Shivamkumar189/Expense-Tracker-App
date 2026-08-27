"""
💰 EXPENSE TRACKER PRO — AI-Powered Personal Finance Dashboard
Built with Streamlit | Plotly | Pandas
Author: Your Name
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import io

# ═══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="💰 Expense Tracker Pro",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════
# CUSTOM CSS — The secret sauce for that WOW factor
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main content area */
    .main .block-container {
        background: rgba(255, 255, 255, 0.97);
        border-radius: 20px;
        padding: 2rem 3rem;
        margin-top: 1rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    /* Hero title */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
    }
    .kpi-card-green {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        box-shadow: 0 10px 30px rgba(17, 153, 142, 0.3);
    }
    .kpi-card-red {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        box-shadow: 0 10px 30px rgba(235, 51, 73, 0.3);
    }
    .kpi-card-orange {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
    }
    .kpi-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .kpi-label {
        font-size: 0.9rem;
        opacity: 0.9;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        margin: 0.3rem 0;
    }
    .kpi-delta {
        font-size: 0.85rem;
        opacity: 0.9;
    }
    
    /* Insight card */
    .insight-card {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        color: #5c3c00;
        font-weight: 500;
        box-shadow: 0 5px 15px rgba(253, 160, 133, 0.3);
        border-left: 5px solid #e67e22;
    }
    
    /* Budget health */
    .health-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .health-excellent { background: #d4edda; color: #155724; }
    .health-good { background: #fff3cd; color: #856404; }
    .health-poor { background: #f8d7da; color: #721c24; }
    
    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d3748;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c3e50 0%, #1a1a2e 100%);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stDateInput label {
        color: #f0f0f0 !important;
        font-weight: 600;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; }
    ::-webkit-scrollbar-thumb { 
        background: linear-gradient(#667eea, #764ba2); 
        border-radius: 5px; 
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #f0f2f6;
        padding: 6px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
    }
    
    /* Metric animation */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .kpi-card { animation: fadeInUp 0.6s ease; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# DATA LOADING
# ═══════════════════════════════════════════════════════════════
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/cleaned_expenses.csv')
    except FileNotFoundError:
        # Fallback: generate on the fly
        st.warning("⚠️ cleaned_expenses.csv not found. Run `python main.py` first.")
        st.stop()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month_name()
    df['Month_Num'] = df['Date'].dt.month
    df['Weekday'] = df['Date'].dt.day_name()
    df['Year'] = df['Date'].dt.year
    return df

df = load_data()

# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown('<h1 class="hero-title">💰 Expense Tracker Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">AI-Powered Personal Finance Analytics · Track · Analyze · Save Smarter</p>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SIDEBAR FILTERS
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### 🎛️ Control Panel")
    st.markdown("---")
    
    # Date range
    min_date, max_date = df['Date'].min(), df['Date'].max()
    date_range = st.date_input(
        "📅 Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Category filter
    categories = st.multiselect(
        "🏷️ Categories",
        options=sorted(df['Category'].unique()),
        default=sorted(df['Category'].unique())
    )
    
    # Payment method
    if 'Payment_Method' in df.columns:
        payment_methods = st.multiselect(
            "💳 Payment Methods",
            options=sorted(df['Payment_Method'].unique()),
            default=sorted(df['Payment_Method'].unique())
        )
    else:
        payment_methods = None
    
    # Monthly budget input
    st.markdown("---")
    st.markdown("### 🎯 Set Your Budget")
    monthly_budget = st.number_input(
        "Monthly Budget (₹)",
        min_value=1000,
        max_value=500000,
        value=40000,
        step=1000
    )
    
    st.markdown("---")
    st.markdown("### 👤 About")
    st.info("Built with ❤️ using Python & Streamlit\n\n**Data Science Project**")

# ═══════════════════════════════════════════════════════════════
# APPLY FILTERS
# ═══════════════════════════════════════════════════════════════
if len(date_range) == 2:
    fdf = df[(df['Date'] >= pd.Timestamp(date_range[0])) & (df['Date'] <= pd.Timestamp(date_range[1]))]
else:
    fdf = df.copy()

fdf = fdf[fdf['Category'].isin(categories)]
if payment_methods is not None:
    fdf = fdf[fdf['Payment_Method'].isin(payment_methods)]

exp_df = fdf[fdf['Type'] == 'Expense']
inc_df = fdf[fdf['Type'] == 'Income']

# ═══════════════════════════════════════════════════════════════
# KPI CARDS ROW
# ═══════════════════════════════════════════════════════════════
total_income = inc_df['Amount'].sum()
total_expense = exp_df['Amount'].sum()
net_savings = total_income - total_expense
savings_rate = (net_savings / total_income * 100) if total_income > 0 else 0
avg_daily = exp_df.groupby('Date')['Amount'].sum().mean() if len(exp_df) > 0 else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card kpi-card-green">
        <div class="kpi-icon">💵</div>
        <div class="kpi-label">Total Income</div>
        <div class="kpi-value">₹{total_income:,.0f}</div>
        <div class="kpi-delta">↑ {len(inc_df)} transactions</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card kpi-card-red">
        <div class="kpi-icon">💸</div>
        <div class="kpi-label">Total Expense</div>
        <div class="kpi-value">₹{total_expense:,.0f}</div>
        <div class="kpi-delta">↓ {len(exp_df)} transactions</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    card_style = "kpi-card" if net_savings >= 0 else "kpi-card kpi-card-red"
    st.markdown(f"""
    <div class="{card_style}">
        <div class="kpi-icon">🏦</div>
        <div class="kpi-label">Net Savings</div>
        <div class="kpi-value">₹{net_savings:,.0f}</div>
        <div class="kpi-delta">{savings_rate:.1f}% savings rate</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card kpi-card-orange">
        <div class="kpi-icon">📊</div>
        <div class="kpi-label">Avg Daily Spend</div>
        <div class="kpi-value">₹{avg_daily:,.0f}</div>
        <div class="kpi-delta">{len(fdf)} total txns</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# BUDGET HEALTH SCORE
# ═══════════════════════════════════════════════════════════════
monthly_avg_expense = exp_df.groupby('Month_Num')['Amount'].sum().mean() if len(exp_df) > 0 else 0
budget_usage = (monthly_avg_expense / monthly_budget * 100) if monthly_budget > 0 else 0

if budget_usage < 70:
    health_status = "EXCELLENT 🌟"
    health_class = "health-excellent"
    health_msg = "You're managing your budget brilliantly!"
elif budget_usage < 100:
    health_status = "GOOD 👍"
    health_class = "health-good"
    health_msg = "You're on track but watch out for overspending."
else:
    health_status = "NEEDS ATTENTION ⚠️"
    health_class = "health-poor"
    health_msg = "You're exceeding your budget. Time to cut back!"

col_a, col_b = st.columns([1, 2])
with col_a:
    st.markdown('<div class="section-header">💚 Budget Health</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="health-badge {health_class}">{health_status}</div>', unsafe_allow_html=True)
    st.markdown(f"**{health_msg}**")
    st.progress(min(budget_usage / 100, 1.0))
    st.caption(f"Monthly avg: ₹{monthly_avg_expense:,.0f} of ₹{monthly_budget:,.0f} budget ({budget_usage:.1f}% used)")

with col_b:
    # Gauge chart for budget usage
    gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=budget_usage,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Budget Usage %", 'font': {'size': 18}},
        delta={'reference': 100, 'decreasing': {'color': "green"}, 'increasing': {'color': "red"}},
        gauge={
            'axis': {'range': [None, 150], 'tickwidth': 1},
            'bar': {'color': "#667eea"},
            'steps': [
                {'range': [0, 70], 'color': "#d4edda"},
                {'range': [70, 100], 'color': "#fff3cd"},
                {'range': [100, 150], 'color': "#f8d7da"}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 100}
        }
    ))
    gauge.update_layout(height=250, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(gauge, use_container_width=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# TABS FOR ORGANIZED CONTENT
# ═══════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview", 
    "📈 Trends", 
    "🏷️ Categories", 
    "💡 AI Insights",
    "📋 Data"
])

# ═══════════════════════════════════════════════════════════════
# TAB 1: OVERVIEW
# ═══════════════════════════════════════════════════════════════
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">🍩 Expense Distribution</div>', unsafe_allow_html=True)
        cat_data = exp_df.groupby('Category')['Amount'].sum().reset_index()
        fig_donut = px.pie(
            cat_data, values='Amount', names='Category', hole=0.5,
            color_discrete_sequence=px.colors.sequential.Plasma_r
        )
        fig_donut.update_traces(textposition='outside', textinfo='percent+label', pull=[0.05]*len(cat_data))
        fig_donut.update_layout(showlegend=False, height=400, margin=dict(t=20, b=20))
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col2:
        st.markdown('<div class="section-header">💳 Payment Method Split</div>', unsafe_allow_html=True)
        if 'Payment_Method' in exp_df.columns:
            pay_data = exp_df.groupby('Payment_Method')['Amount'].sum().reset_index()
            fig_pay = px.bar(
                pay_data.sort_values('Amount'), x='Amount', y='Payment_Method',
                orientation='h', color='Amount', color_continuous_scale='Viridis',
                text='Amount'
            )
            fig_pay.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
            fig_pay.update_layout(height=400, showlegend=False, coloraxis_showscale=False,
                                  margin=dict(t=20, b=20), xaxis_title="Amount (₹)", yaxis_title="")
            st.plotly_chart(fig_pay, use_container_width=True)

    # Top 10 expenses
    st.markdown('<div class="section-header">🔥 Top 10 Biggest Expenses</div>', unsafe_allow_html=True)
    top10 = exp_df.nlargest(10, 'Amount')[['Date', 'Category', 'Description', 'Amount', 'Payment_Method']] \
        if 'Payment_Method' in exp_df.columns else exp_df.nlargest(10, 'Amount')
    st.dataframe(top10, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════
# TAB 2: TRENDS
# ═══════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-header">📈 Income vs Expense Trend</div>', unsafe_allow_html=True)
    
    monthly_exp = exp_df.groupby('Month_Num')['Amount'].sum().reset_index()
    monthly_inc = inc_df.groupby('Month_Num')['Amount'].sum().reset_index()
    
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=monthly_inc['Month_Num'], y=monthly_inc['Amount'],
        mode='lines+markers', name='Income', line=dict(color='#11998e', width=4),
        marker=dict(size=12), fill='tozeroy', fillcolor='rgba(17,153,142,0.1)'
    ))
    fig_trend.add_trace(go.Scatter(
        x=monthly_exp['Month_Num'], y=monthly_exp['Amount'],
        mode='lines+markers', name='Expense', line=dict(color='#eb3349', width=4),
        marker=dict(size=12), fill='tozeroy', fillcolor='rgba(235,51,73,0.1)'
    ))
    fig_trend.update_layout(
        height=450, hovermode='x unified',
        xaxis_title="Month", yaxis_title="Amount (₹)",
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # Weekday heatmap
    st.markdown('<div class="section-header">🗓️ Spending Heatmap (Day × Month)</div>', unsafe_allow_html=True)
    heatmap_data = exp_df.pivot_table(
        index='Weekday', columns='Month', values='Amount', aggfunc='sum', fill_value=0
    )
    weekday_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
    heatmap_data = heatmap_data.reindex(weekday_order)
    heatmap_data = heatmap_data[[m for m in month_order if m in heatmap_data.columns]]
    
    fig_heat = px.imshow(
        heatmap_data, color_continuous_scale='RdYlGn_r', aspect='auto',
        labels=dict(color="₹ Spent")
    )
    fig_heat.update_layout(height=400, margin=dict(t=20, b=20))
    st.plotly_chart(fig_heat, use_container_width=True)

    # Cumulative spending
    st.markdown('<div class="section-header">📊 Cumulative Spending Over Time</div>', unsafe_allow_html=True)
    cum_df = exp_df.sort_values('Date').copy()
    cum_df['Cumulative'] = cum_df['Amount'].cumsum()
    fig_cum = px.area(cum_df, x='Date', y='Cumulative', color_discrete_sequence=['#764ba2'])
    fig_cum.update_layout(height=350, plot_bgcolor='white', margin=dict(t=20, b=20))
    st.plotly_chart(fig_cum, use_container_width=True)

# ═══════════════════════════════════════════════════════════════
# TAB 3: CATEGORIES
# ═══════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="section-header">🏷️ Category Deep-Dive</div>', unsafe_allow_html=True)
    
    cat_summary = exp_df.groupby('Category').agg(
        Total=('Amount', 'sum'),
        Average=('Amount', 'mean'),
        Count=('Amount', 'count'),
        Max=('Amount', 'max')
    ).round(2).sort_values('Total', ascending=False).reset_index()
    
    # Horizontal bar with gradient
    fig_cat = px.bar(
        cat_summary, x='Total', y='Category', orientation='h',
        color='Total', color_continuous_scale='Sunset',
        text='Total', hover_data=['Average', 'Count', 'Max']
    )
    fig_cat.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
    fig_cat.update_layout(
        height=500, yaxis={'categoryorder': 'total ascending'},
        coloraxis_showscale=False, plot_bgcolor='white', margin=dict(t=20, b=20)
    )
    st.plotly_chart(fig_cat, use_container_width=True)
    
    st.markdown("### 📋 Category Statistics Table")
    st.dataframe(
        cat_summary.style.background_gradient(subset=['Total'], cmap='Oranges') \
                         .format({'Total': '₹{:,.0f}', 'Average': '₹{:,.0f}', 'Max': '₹{:,.0f}'}),
        use_container_width=True, hide_index=True
    )

# ═══════════════════════════════════════════════════════════════
# TAB 4: AI INSIGHTS
# ═══════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="section-header">🤖 AI-Powered Insights</div>', unsafe_allow_html=True)
    
    insights = []
    
    # Top category insight
    if len(cat_summary) > 0:
        top_cat = cat_summary.iloc[0]
        pct = (top_cat['Total'] / total_expense * 100) if total_expense > 0 else 0
        insights.append(f"🏆 **{top_cat['Category']}** is your biggest expense category, accounting for **{pct:.1f}%** (₹{top_cat['Total']:,.0f}) of your total spending.")
    
    # Weekend vs weekday
    if 'IsWeekend' in exp_df.columns:
        wknd = exp_df[exp_df['IsWeekend']]['Amount'].sum()
        wkdy = exp_df[~exp_df['IsWeekend']]['Amount'].sum()
        if wkdy > 0:
            ratio = wknd / wkdy * 100
            insights.append(f"📅 You spend **₹{wknd:,.0f}** on weekends vs **₹{wkdy:,.0f}** on weekdays — weekend spending is **{ratio:.1f}%** of weekday.")
    
    # Savings rate insight
    if savings_rate > 30:
        insights.append(f"🌟 Amazing! You're saving **{savings_rate:.1f}%** of your income — financial experts recommend 20%+.")
    elif savings_rate > 0:
        insights.append(f"💪 You're saving **{savings_rate:.1f}%** of your income. Aim for 20%+ to build a strong emergency fund.")
    else:
        insights.append(f"⚠️ You're spending more than you earn! Consider cutting down on **{cat_summary.iloc[0]['Category'] if len(cat_summary)>0 else 'discretionary'}** expenses.")
    
    # Highest spending month
    if len(monthly_exp) > 0:
        peak_month_num = monthly_exp.loc[monthly_exp['Amount'].idxmax(), 'Month_Num']
        peak_amount = monthly_exp['Amount'].max()
        month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        insights.append(f"📊 Your highest spending month was **{month_names[int(peak_month_num)-1]}** with **₹{peak_amount:,.0f}** in expenses.")
    
    # Most frequent category
    freq_cat = exp_df['Category'].value_counts().idxmax() if len(exp_df) > 0 else None
    if freq_cat:
        freq_count = exp_df['Category'].value_counts().max()
        insights.append(f"🔁 You make the most transactions in **{freq_cat}** — **{freq_count}** times in the selected period.")
    
    # Payment method insight
    if 'Payment_Method' in exp_df.columns and len(exp_df) > 0:
        top_pay = exp_df['Payment_Method'].value_counts().idxmax()
        insights.append(f"💳 Your preferred payment method is **{top_pay}** — used in {exp_df['Payment_Method'].value_counts().max()} transactions.")
    
    # Avg transaction
    avg_txn = exp_df['Amount'].mean() if len(exp_df) > 0 else 0
    insights.append(f"💰 Your average transaction size is **₹{avg_txn:,.0f}**.")
    
    # Display insights
    for insight in insights:
        st.markdown(f'<div class="insight-card">{insight}</div>', unsafe_allow_html=True)
    
    # Recommendations
    st.markdown('<div class="section-header">🎯 Smart Recommendations</div>', unsafe_allow_html=True)
    recs = [
        "💡 Set category-wise budgets to control overspending in your top category.",
        "📱 Review your subscriptions monthly — small recurring charges add up!",
        "🍳 Cooking at home 2 extra days/week could save ~₹3,000/month.",
        "🚴 Use public transport or carpool to reduce transport costs by 30%.",
        "💳 Pay credit card bills in full to avoid 30-40% interest charges."
    ]
    for r in recs:
        st.markdown(f"- {r}")

# ═══════════════════════════════════════════════════════════════
# TAB 5: DATA EXPLORER
# ═══════════════════════════════════════════════════════════════
with tab5:
    st.markdown('<div class="section-header">📋 Raw Data Explorer</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", f"{len(fdf):,}")
    col2.metric("Columns", f"{len(fdf.columns)}")
    col3.metric("Date Range", f"{(fdf['Date'].max() - fdf['Date'].min()).days} days")
    
    search = st.text_input("🔍 Search transactions", "")
    display_df = fdf.copy()
    if search:
        mask = display_df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
        display_df = display_df[mask]
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Download button
    csv = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name=f'expense_report_{datetime.now().strftime("%Y%m%d")}.csv',
        mime='text/csv',
        use_container_width=True
    )

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; color: #666;'>
    <p>Built with 💜 using <b>Python</b> · <b>Pandas</b> · <b>Plotly</b> · <b>Streamlit</b></p>
    <p style='font-size: 0.9rem;'>⭐ Star this project on GitHub · 🔗 Connect on LinkedIn</p>
</div>
""", unsafe_allow_html=True)