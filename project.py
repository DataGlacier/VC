import pandas as pd
import os

cab_data = pd.read_csv('Cab_Data.csv')

print("Cab_Data.csv:")
print("Total number of observations:", cab_data.shape[0])
print("Total number of features:", cab_data.shape[1])
print("Base format of the file: .csv")
print("Size of the data (MB):", round(os.path.getsize('Cab_Data.csv') / (1024 * 1024), 2))

customer_data = pd.read_csv('Customer_ID.csv')

print("Customer_ID.csv:")
print("Total number of observations:", customer_data.shape[0])
print("Total number of features:", customer_data.shape[1])
print("Base format of the file: .csv")
print("Size of the data (MB):", round(os.path.getsize('Customer_ID.csv') / (1024 * 1024), 2))

transaction_data = pd.read_csv('Transaction_ID.csv')

print("Transaction_ID.csv:")
print("Total number of observations:", transaction_data.shape[0])
print("Total number of features:", transaction_data.shape[1])
print("Base format of the file: .csv")
print("Size of the data (MB):", round(os.path.getsize('Transaction_ID.csv') / (1024 * 1024), 2))

city_data = pd.read_csv('City.csv')

print("City.csv:")
print("Total number of observations:", city_data.shape[0])
print("Total number of features:", city_data.shape[1])
print("Base format of the file: .csv")
print("Size of the data (MB):", round(os.path.getsize('City.csv') / (1024 * 1024), 2))

