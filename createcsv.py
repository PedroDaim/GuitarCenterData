import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV file into a pandas DataFrame
file_path = r'C:\Users\Pedro\OneDrive\Documents\!!!!Data Analytics\GuitarCenterData\guitar_sales.csv'
guitar_store_sales = pd.read_csv(file_path)

# Display the first few rows
print("First 5 rows of the DataFrame:")
print(guitar_store_sales.head())
print("\n" + "="*50 + "\n")

# Display the last few rows
print("Last 5 rows of the DataFrame:")
print(guitar_store_sales.tail())
print("\n" + "="*50 + "\n")

# Get a summary of the DataFrame
print("Information about the DataFrame:")
print(guitar_store_sales.info())
print("\n" + "="*50 + "\n")

# Get descriptive statistics for numerical columns
print("Descriptive statistics of numerical columns.")
print(guitar_store_sales[['Price']].describe().round(2))
print(guitar_store_sales[['Quantity']].describe().round(0)) # Round to 0 decimal places for Quantity
print("\n" + "="*50 + "\n")
# Check the data types of columns
print("Data types of each column:")
print(guitar_store_sales.dtypes)


