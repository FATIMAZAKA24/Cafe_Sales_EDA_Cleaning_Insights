# EDA & Cleaning with Python - Dirty Cafe Sales Dataset

# importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# saving data in dataframe
df = pd.read_csv("dirty_cafe_sales.csv")
# checking shape of data
print(df.shape)
# viewing few rows of data
print(df.head())
# checking for duplicates
print(df.duplicated().sum())
# checking datatype of each column
print(df.dtypes)
# peforming datatype conversion
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").astype("Int64")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce").astype(
    "float64"
)
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce").astype("float64")
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")

# ensuring the datatypes are now accurate
print(df.dtypes)

# checking null values
print(df.isnull().sum())

# dealing with null values in item Column
print(df["Item"].unique())
# Replace 'UNKNOWN' and 'ERROR' values with NaN
df["Item"] = df["Item"].replace({"UNKNOWN": np.nan, "ERROR": np.nan})
print(df["Item"].unique())
# Replace NaN with mode
mode_item = df["Item"].mode()[0]
df["Item"] = df["Item"].fillna(mode_item)
print(df["Item"].unique())


# dealing with null values in Payment Method Column
print(df["Payment Method"].unique())
df["Payment Method"] = df["Payment Method"].replace(
    {"UNKNOWN": np.nan, "ERROR": np.nan}
)
mode_payment = df["Payment Method"].mode()[0]
df["Payment Method"] = df["Payment Method"].fillna(mode_payment)
mode_item = df["Item"].mode()[0]
df["Item"] = df["Item"].fillna(mode_item)
print(df.isnull().sum())

# dealing with null values in Location Column
print(df["Location"].unique())
df["Location"] = df["Location"].replace({"UNKNOWN": np.nan, "ERROR": np.nan})
mode_location = df["Location"].mode()[0]
df["Location"] = df["Location"].fillna(mode_location)
mode_payment = df["Location"].mode()[0]
df["Location"] = df["Location"].fillna(mode_payment)
mode_item = df["Location"].mode()[0]
df["Location"] = df["Location"].fillna(mode_item)
print(df.isnull().sum())

# dealing with null values in Transaction Date Column
# Show how many times the values 'UNKNOWN' and 'ERROR' appear in the 'Transaction Date' column
print(df["Transaction Date"].value_counts().get("UNKNOWN", 0))
print(df["Transaction Date"].value_counts().get("ERROR", 0))
df["Transaction Date"] = df["Transaction Date"].replace(
    {"UNKNOWN": np.nan, "ERROR": np.nan}
)
# Replace null values in 'Transaction Date' with the nearest value (forward fill)
df["Transaction Date"] = df["Transaction Date"].ffill()
print(df.isnull().sum())


# dealing with null values in 'Quantity', 'Price Per Unit', and 'Total Spent' Columns
print(df.isnull().sum())
print(df["Quantity"].describe())
print(df[df["Quantity"] < 0])  # check for negative / huge values
# Check for zeros or negative values
bad_rows = df[
    (df["Quantity"] <= 0) | (df["Price Per Unit"] <= 0) | (df["Total Spent"] <= 0)
]
print(bad_rows)
print(len(bad_rows))
df = df[(df["Quantity"] > 0) | df["Quantity"].isna()]
df = df[(df["Price Per Unit"] > 0) | df["Price Per Unit"].isna()]
df = df[(df["Total Spent"] > 0) | df["Total Spent"].isna()]


def safe_infer(row):
    # Infer missing values only if exactly one is missing
    q, p, t = row["Quantity"], row["Price Per Unit"], row["Total Spent"]

    if pd.isna(q) and pd.notna(p) and pd.notna(t):
        row["Quantity"] = t / p
    elif pd.isna(p) and pd.notna(q) and pd.notna(t):
        row["Price Per Unit"] = t / q
    elif pd.isna(t) and pd.notna(q) and pd.notna(p):
        row["Total Spent"] = q * p

    return row


df = df.apply(safe_infer, axis=1)
# Ensure no negative or huge values
df["Quantity"] = df["Quantity"].clip(lower=0)
df["Price Per Unit"] = df["Price Per Unit"].clip(lower=0)
df["Total Spent"] = df["Total Spent"].clip(lower=0)
df = df.dropna(subset=["Quantity", "Price Per Unit", "Total Spent"])

# Finally checking if there are any null values left
print(df.isnull().sum())


# Using clean data for answering/visualizing some business questions a cafe manager might care about
# 1. Which items sell the most?
# print(df.head(5))
items_sale = (
    df.groupby("Item")["Quantity"]
    .sum()
    .reset_index()
    .sort_values(by="Quantity", ascending=False)
)
plt.figure(figsize=(10, 6))
sns.barplot(x="Item", y="Quantity", data=items_sale)
plt.title("Items Sold by Quantity")
plt.show()


# 2. Which locations generate the most revenue?
revenue_location = (
    df.groupby("Location")["Total Spent"]
    .sum()
    .reset_index()
    .sort_values(by="Total Spent", ascending=False)
)
plt.figure(figsize=(10, 6))
sns.barplot(x="Location", y="Total Spent", data=revenue_location)
plt.title("Revenue by Location")
plt.show()

# 3. Are there seasonal trends in sales? (e.g., weekends vs weekdays, months)
# extract month from transaction date
df["Month"] = df["Transaction Date"].dt.month
monthly_sales = (
    df.groupby("Month")["Total Spent"].sum().reset_index().sort_values(by="Month")
)
plt.figure(figsize=(10, 6))
sns.lineplot(x="Month", y="Total Spent", data=monthly_sales, marker="o")
plt.title("Monthly Sales Trend")
plt.show()

# --------------------------------------------------------------------------------------------------------------#
