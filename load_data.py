import sqlite3
import pandas as pd

conn = sqlite3.connect("olist.db")

df_orders = pd.read_csv("data_raw/olist_orders_dataset.csv")
df_order_items = pd.read_csv("data_raw/olist_order_items_dataset.csv")
df_products = pd.read_csv("data_raw/olist_products_dataset.csv")

df_orders.to_sql(
    name="orders",
    con=conn,
    if_exists="replace",
    index=False,
)

df_order_items.to_sql(
    name="order_items",
    con=conn,
    if_exists="replace",
    index=False,
)

df_products.to_sql(
    name="products",
    con=conn,
    if_exists="replace",
    index=False,
)

conn.close()

print("Importation des tables terminée avec succès !")

