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

