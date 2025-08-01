import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("dirty_cafe_sales.csv")
print(df.groupby('Total Spent')['Total Spent'])
# df["Transaction Date"] = df.to_datetime(df['Transaction Date'])
# daily_sales = df.groupby('Transaction Date')['Total Spent'].sum().reset_index()
# print(daily_sales)
