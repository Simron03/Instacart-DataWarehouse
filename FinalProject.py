
import numpy as np
import pandas as pd

aisle = pd.read_csv("aisles.csv")
departments = pd.read_csv("departments.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
order_products1= pd.read_csv("order_products__prior.csv")
order_products2= pd.read_csv("order_products__train.csv")

order_products2.shape


aisle.head()

#Checking Data Frame - Aisle
aisle.head()

#Checking Data Frame - Departments
departments.head()

#Checking Data Frame - Orders
del orders["eval_set"]
orders.head()

# Finding number of rows and column in the data frame
print("The product has : "+ Str(Product.shape[0]) + " rows and " + str(Product.shape[1]) + "columns.")



# Join Product, Departments and Aisle Data Frame to product_all data frame
product_aisle  = products.merge(aisle, left_on="aisle_id", right_on="aisle_id")
product_all = product_aisle.merge(departments, left_on="department_id", right_on="department_id")
product_all = product_all.drop(columns=["aisle_id","department_id"])
product_all = product_all[['product_id', 'product_name', 'department','aisle', ]]
product_all.head()

market_basket = order_products.merge(orders, left_on="order_id",right_on="order_id")
market_basket.sample(5)

market_basket = market_basket[['user_id','order_id', 'order_number',
       'order_dow', 'order_hour_of_day', 'days_since_prior_order','product_name', 'add_to_cart_order', 'reordered',
    'department', 'aisle' ]]

market_basket.head()

#converting number of day to name
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Sunday" if x==0 else x)
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Monday" if x==1 else x)
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Tuesday" if x==2 else x)
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Wednesday" if x==3 else x)
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Thursday" if x==4 else x)
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Friday" if x==5 else x)
market_basket["order_dow"] = market_basket["order_dow"].apply(lambda x:"Saturday" if x==6 else x)

#Saving result data frame as a Pickle File
market_basket.to_pickle("MarketBasketInitialPickle")

#Reading market basket initial from Pickle File as a data frame
market_basket = pd.read_pickle("MarketBasketInitialPickle")


