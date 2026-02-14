import pandas as pd

products = {
    "ProductID": [1, 2, 3, 4, 5],
    "ProductName": ["Rice", "Milk", "Bread", "Oil", "Sugar"],
    "Category": ["Grocery", "Dairy", "Bakery", "Grocery", "Grocery"],
    "CostPrice": [40, 20, 25, 120, 35]
}

df_products = pd.DataFrame(products)

sales = {
    "ProductID": [1, 2, 3, 4, 5],
    "QuantitySold": [50, 120, 80, 40, 60],
    "SellingPrice": [55, 30, 40, 150, 50]
}

df_sales = pd.DataFrame(sales)

df = pd.merge(df_products, df_sales, on="ProductID")

print("\nDATA INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

df["Revenue"] = df["SellingPrice"] * df["QuantitySold"]
df["Profit"] = (df["SellingPrice"] - df["CostPrice"]) * df["QuantitySold"]

print("\nSORTED BY PROFIT (DESCENDING)")
print(df.sort_values(by="Profit", ascending=False))

print("\nPRODUCTS WITH REVENUE GREATER THAN 4000")
print(df[df["Revenue"] > 4000])

print("\nGROCERY CATEGORY PRODUCTS")
print(df[df["Category"] == "Grocery"])

# Grouping
print("\nCATEGORY WISE TOTAL REVENUE")
print(df.groupby("Category")["Revenue"].sum())

print("\nCATEGORY WISE TOTAL PROFIT")
print(df.groupby("Category")["Profit"].sum())

# Best and Worst Products
print("\nBEST SELLING PRODUCT")
print(df.loc[df["Revenue"].idxmax()])

print("\nLEAST PROFIT PRODUCT")
print(df.loc[df["Profit"].idxmin()])

# Final Output
print("\nFINAL SUPERMARKET SALES REPORT")
print(df)
