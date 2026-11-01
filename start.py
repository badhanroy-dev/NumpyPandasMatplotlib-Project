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
#Converting order value column into numpy array
values = df["Order_Value"].to_numpy()
print("Order value mean:",np.mean(values))
print("Order value minimum:",np.min(values))
print("Order value maximum:",np.max(values))
print("Order value standard Deviation:",np.std(values))
#order values above 100
result = np.where(values > 100)
print(df.iloc[result[0]]["Order_ID"])
print("rating is between 1 and 5")
ratings = df["Customer_Rating"].to_numpy()
print(np.all(ratings>=1)&(ratings<=5))
#number of orders where delivery time 4 days or less
fast_deliveries = np.sum(df["Delivery_Days"].to_numpy() <=4)
percentage = (fast_deliveries/len(df)) * 100
print("Fast deliveries", fast_deliveries)
print("Percentage",percentage)

#Average order value by each category
category_avg = df.groupby("Category")["Order_Value"].mean()
plt.bar(category_avg.index, category_avg.values)
plt.title("Average Order value by Category")
plt.xlabel("Category")
plt.ylabel("Average Order value")
plt.show()
#Distribution of delivery time
plt.hist(df["Delivery_Days"], bins=8,edgecolor = "black")
plt.title("Distribution of Delivery time")
plt.xlabel("Delivery Days")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()
#Delivery time against customer rating
plt.scatter(df["Delivery_Days"],df["Customer_Rating"])
plt.title("Delivery time vs Customer Rating")
plt.xlabel("Delivery Days")
plt.ylabel("Customer Rating")
plt.tight_layout()
plt.show()