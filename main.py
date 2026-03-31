import pandas as pd
df = pd.read_csv("sales.csv")
print("Original Data:")
print(df)
df = df.dropna()
total_sales = df["sales"].sum()
print("\nTotal Sales:", total_sales)