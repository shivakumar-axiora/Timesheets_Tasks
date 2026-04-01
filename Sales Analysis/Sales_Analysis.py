#Sales analysis on real CSV — groupby, pivot, merge.

import pandas as pd

#Loading The Data
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
# df1 = pd.DataFrame(sales)
# df2 = pd.DataFrame(customers)
# df3 = pd.DataFrame(products)

# print("Sales Data:\n", df1)
# print("Customers Data:\n", df2)
# print("Products Data:\n", df3)

#creating Total Sales column
sales['total'] = sales['quantity'] * sales['price']

#Merging the data
df = sales.merge(customers, on= "customer_id") \
        .merge(products, on="product_id")
print("Merged Data: \n", df)

#grouping the data based on total sales per region
region_sales = df.groupby("region")["total"].sum()
print("\n sales by region:\n", region_sales)

#grouping the data based on sales by catgory
category_sales = df.groupby("category")["total"].sum()
print("\n sales by Category:\n", category_sales)

#grouping the data based on the top customer spends
customer_sales = df.groupby("customer_name")["total"].sum().sort_values(ascending=False)
print("\n sales by customer spending:\n", customer_sales)


#pivoting
pivot_table = pd.pivot_table(
    df, 
    values="total", 
    index="region",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

print("\n Pivot Table (Region vs Category) :\n", pivot_table)