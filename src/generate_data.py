"""
Generates realistic synthetic expense data for 1 year.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# Configuration
CATEGORIES = {
    'Food':      {'min': 50,    'max': 800,   'weight': 0.30},
    'Transport': {'min': 30,    'max': 500,   'weight': 0.15},
    'Rent':      {'min': 8000,  'max': 15000, 'weight': 0.05},
    'Bills':     {'min': 500,   'max': 3000,  'weight': 0.10},
    'Shopping':  {'min': 200,   'max': 5000,  'weight': 0.15},
    'Entertainment': {'min': 100, 'max': 2000,'weight': 0.10},
    'Health':    {'min': 200,   'max': 4000,  'weight': 0.05},
    'Education': {'min': 500,   'max': 6000,  'weight': 0.05},
    'Others':    {'min': 50,    'max': 1500,  'weight': 0.05},
}

PAYMENT_METHODS = ['UPI', 'Credit Card', 'Debit Card', 'Cash', 'Net Banking']

def generate_expenses(start_date='2024-01-01', days=365, transactions_per_day=(1, 5)):
    rows = []
    start = datetime.strptime(start_date, '%Y-%m-%d')

    cat_names = list(CATEGORIES.keys())
    cat_weights = [CATEGORIES[c]['weight'] for c in cat_names]

    for d in range(days):
        current_date = start + timedelta(days=d)
        n_txn = random.randint(*transactions_per_day)

        for _ in range(n_txn):
            category = np.random.choice(cat_names, p=cat_weights)
            cfg = CATEGORIES[category]
            amount = round(np.random.uniform(cfg['min'], cfg['max']), 2)

            rows.append({
                'Date': current_date.strftime('%Y-%m-%d'),
                'Category': category,
                'Description': f"{category} expense",
                'Amount': amount,
                'Payment_Method': random.choice(PAYMENT_METHODS),
                'Type': 'Expense'
            })

        # Monthly salary injection (1st of each month)
        if current_date.day == 1:
            rows.append({
                'Date': current_date.strftime('%Y-%m-%d'),
                'Category': 'Salary',
                'Description': 'Monthly Salary',
                'Amount': 50000 + np.random.randint(-2000, 5000),
                'Payment_Method': 'Net Banking',
                'Type': 'Income'
            })

    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    df = generate_expenses()
    df.to_csv('data/expenses.csv', index=False)
    print(f"✅ Generated {len(df)} transactions → data/expenses.csv")
    print(df.head())