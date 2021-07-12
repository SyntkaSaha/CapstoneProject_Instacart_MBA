# importing required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# downloading and unzipping files
import zipfile

orders_data = "orders.csv"
products_data = 'products.csv'
departments_data = 'departments.csv'
aisles_data = 'aisles.csv'
order_products__prior_data = "order_products__prior.csv"
order_products__train_data = "order_products__train.csv"

directory = "C:/Users/sayan/Downloads/instacart-market-basket-analysis/"
unzip_orders = zipfile.ZipFile(directory+orders_data+".zip","r")
unzip_products = zipfile.ZipFile(directory+products_data+".zip","r")
unzip_departments = zipfile.ZipFile(directory+departments_data+".zip","r")
unzip_aisles = zipfile.ZipFile(directory+aisles_data+".zip","r")
unzip_order_products__prior = zipfile.ZipFile(directory+order_products__prior_data+".zip","r")
unzip_order_products__train = zipfile.ZipFile(directory+order_products__train_data+".zip","r")

# reading the files
df_orders = pd.read_csv(unzip_orders.open('orders.csv'))
df_products = pd.read_csv(unzip_products.open('products.csv'))
df_departments = pd.read_csv(unzip_departments.open('departments.csv'))
df_aisles = pd.read_csv(unzip_aisles.open('aisles.csv'))
df_order_products__prior = pd.read_csv(unzip_order_products__prior.open('order_products__prior.csv'))
df_order_products__train = pd.read_csv(unzip_order_products__train.open('order_products__train.csv'))

# checking dataframe details
df_orders.info()
df_products.info()
df_departments.info()
df_aisles.info()
df_order_products__prior.info()
df_order_products__train.info()

# check for missing values
df_orders.isnull().sum()
df_products.isnull().sum()
df_departments.isnull().sum()
df_aisles.isnull().sum()
df_order_products__prior.isnull().sum()
df_order_products__train.isnull().sum()

# sample overview of the dataframes
df_orders.head()
df_products.head()
df_departments.head()
df_aisles.head()
df_order_products__prior.head()
df_order_products__train.head()

# duplicate check of key dataframes
df_orders.order_id.count()
df_orders.order_id.nunique()
df_products.product_id.count()
df_products.product_id.nunique()
df_departments.department_id.count()
df_departments.department_id.nunique()
df_aisles.aisle_id.count()
df_aisles.aisle_id.nunique()

# merge two dataframes to check what products belong to what aisle

product_aisle_info = pd.merge(df_aisles, df_products, on="aisle_id")
product_aisle_info.head(10)

# to check what product belongs to which department

product_department_info = pd.merge(df_departments, df_products, on="department_id")
product_department_info.head(10)

# merge order products prior with products to check what product maps to what order
product_prior_order_info = pd.merge(df_order_products__prior, df_products, on="product_id")
product_prior_order_info.head(10)

# merge product_per_order_info and orders dataframes to check products for each order
product_per_order_info = pd.merge(product_prior_order_info, df_orders, on="order_id")
product_per_order_info.head(10)

# validating the claim that 4 to 100 orders of a customer are given
order_per_customer_info = df_orders.groupby("user_id")["order_number"].count().reset_index()
order_per_customer_info.head(10)

order_per_customer_info["order_number"].value_counts()

# validate claim through graphical representation
plt.figure(figsize=(25, 20))
sns.countplot(order_per_customer_info["order_number"])
plt.xlabel('Total number of orders')
plt.ylabel('Number of Customers')
plt.title('Validation Chart')

# send to json files
df_aisles.to_json(r'C:/Users/sayan/Desktop/Masters_MSBA/MIS-690/json files/aisles.json' , orient='records')
df_orders.to_json(r'C:/Users/sayan/Desktop/Masters_MSBA/MIS-690/json files/orders.json', orient='records')
df_products.to_json(r'C:/Users/sayan/Desktop/Masters_MSBA/MIS-690/json files/products.json', orient='records')
df_departments.to_json(r'C:/Users/sayan/Desktop/Masters_MSBA/MIS-690/json files/departments.json', orient='records')
df_order_products__prior.to_json(r'C:/Users/sayan/Desktop/Masters_MSBA/MIS-690/json files/order_products__prior.json', orient='records')
df_order_products__train.to_json(r'C:/Users/sayan/Desktop/Masters_MSBA/MIS-690/json files/order_products__train.json', orient='records')