import pandas as pd

def monthly_summary(df):
    exp = df[df['Type'] == 'Expense']
    inc = df[df['Type'] == 'Income']
    summary = pd.DataFrame({
        'Total_Expense': exp.groupby('Month_Num')['Amount'].sum(),
        'Total_Income':  inc.groupby('Month_Num')['Amount'].sum(),
    }).fillna(0)
    summary['Savings'] = summary['Total_Income'] - summary['Total_Expense']
    summary['Savings_Rate_%'] = (summary['Savings'] / summary['Total_Income'] * 100).round(2)
    return summary

def category_summary(df):
    exp = df[df['Type'] == 'Expense']
    return exp.groupby('Category')['Amount'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False)

def detect_overspending(df, threshold_multiplier=1.5):
    """Flags months where spending exceeds 1.5x the yearly average."""
    exp = df[df['Type'] == 'Expense']
    monthly = exp.groupby('Month_Num')['Amount'].sum()
    threshold = monthly.mean() * threshold_multiplier
    return monthly[monthly > threshold]