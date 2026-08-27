from src.generate_data import generate_expenses
from src.clean_data import clean_data
from src.analyze import monthly_summary, category_summary, detect_overspending
from src.visualize import plot_category_bar, plot_pie, plot_monthly_trend, plot_weekday_pattern
import os

os.makedirs('data', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

print("Step 1: Generating synthetic data...")
df_raw = generate_expenses()
df_raw.to_csv('data/expenses.csv', index=False)

print("Step 2: Cleaning data...")
df = clean_data()

print("Step 3: Analysis...")
monthly = monthly_summary(df)
cat = category_summary(df)
overspend = detect_overspending(df)

monthly.to_csv('outputs/monthly_report.csv')
cat.to_csv('outputs/category_report.csv')

print("\n📊 Monthly Summary:\n", monthly)
print("\n📊 Category Summary:\n", cat)
print("\n⚠️ Overspending months:\n", overspend)

print("\nStep 4: Generating charts...")
plot_category_bar(df); plot_pie(df); plot_monthly_trend(df); plot_weekday_pattern(df)
print("✅ All charts saved in images/")

# Generate insights
with open('outputs/insights.md', 'w') as f:
    f.write("# 💡 Key Insights\n\n")
    f.write(f"- Total transactions analyzed: **{len(df)}**\n")
    f.write(f"- Highest spending category: **{cat.index[0]}** (₹{cat['sum'].iloc[0]:,.0f})\n")
    f.write(f"- Average monthly savings rate: **{monthly['Savings_Rate_%'].mean():.2f}%**\n")
    f.write(f"- Months with overspending: **{list(overspend.index)}**\n")
print("✅ Insights saved → outputs/insights.md")