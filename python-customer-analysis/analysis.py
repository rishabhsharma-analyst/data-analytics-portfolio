import pandas as pd

# Load data
# df = pd.read_csv("customers.csv") # Original line causing FileNotFoundError

# --- FIX: Create a sample DataFrame for demonstration if 'customers.csv' is not available ---
data = {
    'customer_id': range(1, 11),
    'annual_income': [50000, 75000, 30000, 120000, 60000, 80000, 45000, 90000, 35000, 110000],
    'spending_score': [70, 85, 40, 95, 55, 78, 30, 88, 50, 92],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Chicago', 'Los Angeles', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Basic info
print("Dataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Average income
avg_income = df["annual_income"].mean()
print("\nAverage Income:", avg_income)

# Top spending customers
top_customers = df.sort_values(by="spending_score", ascending=False).head(5)
print("\nTop Customers:")
print(top_customers)

# Group by city
city_analysis = df.groupby("city")["annual_income"].mean()
print("\nAverage Income by City:")
print(city_analysis)

# Customer segmentation
def segment(score):
    if score > 75:
        return "High Value"
    elif score > 50:
        return "Medium Value"
    else:
        return "Low Value"

df["segment"] = df["spending_score"].apply(segment)

print("\nCustomer Segments:")
print(df[["customer_id", "segment"]])

import matplotlib.pyplot as plt

# Spending score distribution
plt.hist(df["spending_score"])
plt.title("Spending Score Distribution")
plt.xlabel("Score")
plt.ylabel("Customers")
plt.show()

# Income vs Spending
plt.scatter(df["annual_income"], df["spending_score"])
plt.title("Income vs Spending")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()
