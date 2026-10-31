import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("online_shopping.csv")
print("The first five rows-")
print(df.head())
print("The last five rows-")
print(df.tail())
print("The number of rows and columns")
print(df.shape)
print("The number of columns-")
print(df.columns)
print("The dataTypes-")
print(df.info())
print("Summary statistics for numerical columns")
print(df.describe())
print("Missing values")
print(df.isnull().sum())
print("Duplicate rows")
print(df.duplicated().sum())
df.replace("Missing",np.nan,inplace=True) #inplace modifies the original dataframe directly instead of creating a new dataframe
df.drop_duplicates(inplace=True)
df["Category"] = df["Category"].replace("Clothes","Clothing")
df["Order_Value"] = pd.to_numeric(df["Order_Value"])
df["Delivery_Days"] = pd.to_numeric(df["Delivery_Days"])
df.loc[~df["Customer_Rating"].between(1,5), "Customer_Rating"] = np.nan
#~ reverses the Boolean condition. It selects ratings that are not between 1 and 5
df["Order_Value"] = df["Order_Value"].fillna(df["Order_Value"].median())
df["Delivery_Days"] = df["Delivery_Days"].fillna(df["Delivery_Days"].median())
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].median())
print("RemainingNull")
print(df.isnull().sum()) #gives per column count of nulls in them
print("Duplicated")
print(df.duplicated().sum())
print(df.shape)
#Creating delivery type
df["Delivery_Type"] = np.where(
    df["Delivery_Days"] <=4, "Fast","Slow"
)
print(df[["Order_ID","Delivery_Days","Delivery_Type"]])
print("Average order value:", df["Order_Value"].mean())
print("Average delivery days:",df["Delivery_Days"].mean())
print("Median order value:",df["Order_Value"].median())
print("Maximum delivery days:",df["Delivery_Days"].max())
print("Orders more than value 100: ",df[df["Order_Value"]>100])
print("Orders rated 5:",df[df["Customer_Rating"]==5])
category_summary = df.groupby("Category").agg(
    order_Count = ("Order_ID","count"),
    Average_Order_Value = ("Order_Value","mean"),
    Average_Delivery_Days = ("Delivery_Days","mean")
)
print("Category Summary: ",category_summary)
print("Total orders by status: ")
print(df["Status"].value_counts())
print("Sorted by delivery time")
print(df.sort_values("Delivery_Days",ascending=False))
print("3 most expensive orders")
print(df.nlargest(3,"Order_Value"))
