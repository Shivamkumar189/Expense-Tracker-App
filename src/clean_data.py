import pandas as pd

def clean_data(input_path='data/expenses.csv', output_path='data/cleaned_expenses.csv'):
    df = pd.read_csv(input_path)
    df = df.drop_duplicates()
    df = df.dropna(subset=['Date', 'Amount', 'Category', 'Type'])

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Category'] = df['Category'].astype(str).str.strip().str.title()
    df['Type'] = df['Type'].astype(str).str.strip().str.title()

    # Feature engineering
    df['Month'] = df['Date'].dt.month_name()
    df['Month_Num'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.day_name()
    df['IsWeekend'] = df['Weekday'].isin(['Saturday', 'Sunday'])

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved → {output_path}")
    return df

if __name__ == "__main__":
    clean_data()