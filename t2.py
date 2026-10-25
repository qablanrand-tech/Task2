import json
import pandas as pd

print("=== 1. CSV DATA ANALYSIS ===")
csv_data = {
    "name": ["Ahmad", "Fatima", "Ali", "Sara", "Omar"],
    "age": [25, 30, 22, 28, 35],
    "score": [85, 90, 78, 92, 88],
}
df_csv = pd.DataFrame(csv_data)

print("Shape (Rows, Columns):", df_csv.shape)

print("\nColumn Types:\n", df_csv.dtypes)

print("\nMissing Values:\n", df_csv.isnull().sum())

print("\nSummary Statistics:\n", df_csv.describe())


print("\n" + "=" * 50 + "\n")


print("=== 2. JSON DATA ANALYSIS ===")
json_data = [
    {"product": "Laptop", "price": 1200, "stock": 15},
    {"product": "Phone", "price": 800, "stock": 30},
    {"product": "Tablet", "price": 500, "stock": 20},
]

with open("local_data.json", "w") as f:
    json.dump(json_data, f)

df_json = pd.read_json("local_data.json")

print("Shape (Rows, Columns):", df_json.shape)

print("\nColumn Types:\n", df_json.dtypes)

print("\nMissing Values:\n", df_json.isnull().sum())

print("\nSummary Statistics:\n", df_json.describe())