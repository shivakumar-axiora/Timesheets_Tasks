#Sales analysis on real CSV — groupby, pivot, merge using method chaining. Profile with .info() + .describe().
import pandas as pd

#Method Chaining
#load datasets
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv") 
products = pd.read_csv("products.csv") 

#creating a total column 
df = (
    sales.assign(total = lambda x: x['quantity'] * x['price'])
    .merge(customers, on="customer_id")
    .merge(products, on="product_id"))

print("Merged Data:\n", df)

#Data Profiling
print("\n Info:")
print(df.info())

print("\n Describe:")
print(df.describe(include="all"))

#group by (chained format)
region_sales = (
    df
    .groupby("region", as_index=False)
    .agg(total_sales=("total", "sum"))
)

print("\n Sales by Region:\n", region_sales)

customer_sales = (
    df
    .groupby("customer_name", as_index=False)
    .agg(total_spent=("total", "sum"))
    .sort_values(by="total_spent", ascending=False)
)

print("\n Customer Spending:\n", customer_sales)

category_sales = (
    df
    .groupby("category", as_index=False)
    .agg(total_sales=("total", "sum"))
)

print("\n Category Sales:\n", category_sales)

#pivot table

pivot_table = (
    df.pivot_table(
        values="total",
        index="region",
        columns="category",
        aggfunc="sum",
        fill_value=0
    )
    .reset_index()
)

print("\n Pivot Table:\n", pivot_table)