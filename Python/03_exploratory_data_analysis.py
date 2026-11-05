
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------
# 1. LOAD CLEANED DATA
# --------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR, "Dataset", "cleaned_superstore.csv"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "Dashboard-Screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH, parse_dates=["Order Date", "Ship Date"])

sns.set_theme(style="whitegrid")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# --------------------------------
# 2. BUSINESS KPIs
# --------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()
profit_margin = (total_profit / total_sales) * 100

print("\n========== BUSINESS KPIs ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Total Quantity: {total_quantity:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

# --------------------------------
# 3. MONTHLY SALES ANALYSIS
# --------------------------------

df["Order Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Order Month")["Sales"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "monthly_sales.png"))
plt.show()

# --------------------------------
# 4. CATEGORY-WISE SALES
# --------------------------------

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Sales:")
print(category_sales)

plt.figure(figsize=(9, 5))
sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "category_sales.png"))
plt.show()

# --------------------------------
# 5. REGIONAL SALES ANALYSIS
# --------------------------------

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRegional Sales:")
print(region_sales)

plt.figure(figsize=(9, 5))
sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)
plt.title("Regional Sales Performance")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "regional_sales.png"))
plt.show()

# --------------------------------
# 6. PROFIT BY CATEGORY
# --------------------------------

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Profit:")
print(category_profit)

plt.figure(figsize=(9, 5))
sns.barplot(
    x=category_profit.index,
    y=category_profit.values
)
plt.title("Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "category_profit.png"))
plt.show()

# --------------------------------
# 7. TOP 10 PRODUCTS BY SALES
# --------------------------------

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .nlargest(10)
)

print("\nTop 10 Products:")
print(top_products)

plt.figure(figsize=(11, 7))
sns.barplot(
    x=top_products.values,
    y=top_products.index
)
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_products.png"))
plt.show()

# --------------------------------
# 8. DISCOUNT VS PROFIT
# --------------------------------

plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.5
)
plt.title("Discount vs Profit Analysis")
plt.xlabel("Discount")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "discount_profit.png"))
plt.show()

# --------------------------------
# 9. CORRELATION ANALYSIS
# --------------------------------

numeric_df = df[
    ["Sales", "Quantity", "Discount", "Profit"]
]

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Sales Data Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.show()

print("\nEDA completed successfully!")
print("Charts saved in:", OUTPUT_DIR)
