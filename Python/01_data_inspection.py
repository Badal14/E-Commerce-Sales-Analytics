
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
DATA_PATH = os.path.join(BASE_DIR, "Dataset", "superstore.csv")

# Load dataset
df = pd.read_csv(DATA_PATH, encoding="latin1")

print("Dataset loaded successfully!")

# Display first 5 records
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 records
print("\nLast 5 Rows:")
print(df.tail())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Data types
print("\nData Types:")
print(df.dtypes)

# Unique values per column
print("\nUnique Values:")
print(df.nunique())