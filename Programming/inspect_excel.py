import pandas as pd

file = "Copy of ADNI_group_ID_data.xlsx"

df = pd.read_excel(file)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 10 rows:")
print(df.head(10))