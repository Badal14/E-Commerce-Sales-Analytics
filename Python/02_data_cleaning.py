
import pandas as pd
import numpy as np
import os

# ----------------------------------
# 1. PROJECT PATHS
# ----------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "Dataset", "superstore.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "Dataset", "cleaned_superstore.csv")

# ----------------------------------
# 2. LOAD ORIGINAL DATASET
# ----------------------------------

df = pd.read_csv(
    DATA_PATH,
    encoding="latin1",
    dtype={"Postal Code": "string"}
)

print("Original dataset loaded:", df.shape)

# Keep original data unchanged
original_rows = len(df)

# ----------------------------------
# 3. CLEAN COLUMN WHITESPACE
# ----------------------------------

df.columns = df.columns.str.strip()

text_columns = df.select_dtypes(include=["object", "string"]).columns

for col in text_columns:
    df[col] = df[col].str.strip()

# ----------------------------------
# 4. CONVERT DATE COLUMNS
# ----------------------------------

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%m/%d/%Y",
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%m/%d/%Y",
    errors="coerce"
)

# ----------------------------------
# 5. CHECK INVALID DATES
# ----------------------------------

print("\nInvalid Order Dates:", df["Order Date"].isna().sum())
print("Invalid Ship Dates:", df["Ship Date"].isna().sum())

# ----------------------------------
# 6. CHECK BUSINESS RULES
# ----------------------------------

print("\nNegative Sales:", (df["Sales"] < 0).sum())
print("Negative Profit:", (df["Profit"] < 0).sum())
print("Zero or Negative Quantity:", (df["Quantity"] <= 0).sum())
print("Invalid Discount:", ((df["Discount"] < 0) | (df["Discount"] > 1)).sum())

# Check shipping date before order date
print(
    "Ship date before order date:",
    (df["Ship Date"] < df["Order Date"]).sum()
)

# ----------------------------------
# 7. FINAL DATA QUALITY CHECK
# ----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ----------------------------------
# 8. SAVE CLEANED DATASET
# ----------------------------------

assert len(df) == original_rows, "Unexpected row count change!"

df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned dataset saved successfully!")
print("Output:", OUTPUT_PATH)
print("Final dataset shape:", df.shape)
