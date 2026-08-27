import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
os.makedirs('images', exist_ok=True)

def plot_category_bar(df):
    exp = df[df['Type'] == 'Expense']
    data = exp.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=data.index, y=data.values, palette='Set2')
    plt.title("Total Expense by Category", fontsize=14, fontweight='bold')
    plt.ylabel("Amount (₹)"); plt.xticks(rotation=45)
    plt.tight_layout(); plt.savefig('images/category_bar.png', dpi=120); plt.close()

def plot_pie(df):
    exp = df[df['Type'] == 'Expense']
    data = exp.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution", fontsize=14, fontweight='bold')
    plt.tight_layout(); plt.savefig('images/pie_chart.png', dpi=120); plt.close()

def plot_monthly_trend(df):
    exp = df[df['Type'] == 'Expense'].groupby('Month_Num')['Amount'].sum()
    inc = df[df['Type'] == 'Income'].groupby('Month_Num')['Amount'].sum()
    plt.figure(figsize=(10, 5))
    exp.plot(marker='o', label='Expense', color='red')
    inc.plot(marker='o', label='Income', color='green')
    plt.title("Monthly Income vs Expense", fontsize=14, fontweight='bold')
    plt.xlabel("Month"); plt.ylabel("Amount (₹)"); plt.legend()
    plt.tight_layout(); plt.savefig('images/monthly_trend.png', dpi=120); plt.close()

def plot_weekday_pattern(df):
    exp = df[df['Type'] == 'Expense']
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Weekday', y='Amount', data=exp, order=order, estimator=sum, palette='coolwarm')
    plt.title("Total Spending by Weekday", fontsize=14, fontweight='bold')
    plt.tight_layout(); plt.savefig('images/weekday_pattern.png', dpi=120); plt.close()