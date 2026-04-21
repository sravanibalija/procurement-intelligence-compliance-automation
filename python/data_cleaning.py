import pandas as pd

df = pd.read_csv("data/raw_procurement_data.csv")
df = df.drop_duplicates()
df["Invoice_Date"] = pd.to_datetime(df["Invoice_Date"], errors="coerce")
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

df.to_csv("data/cleaned_procurement_data.csv", index=False)

print("Data cleaned successfully.")
