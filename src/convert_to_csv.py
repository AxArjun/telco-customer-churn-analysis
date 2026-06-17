import pandas as pd

df = pd.read_excel(
    r"C:\Users\arjun\telco-customer-churn-analysis\data\raw\Telco_customer_churn.xlsx"
)

print("Shape:", df.shape)
print(df.columns.tolist())

df.to_csv(
    r"C:\Users\arjun\telco-customer-churn-analysis\data\raw\telco_customer_churn.csv",
    index=False
)

print("CSV created successfully")