import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV file into a pandas DataFrame
file_path = r'C:\Users\Pedro\OneDrive\Documents\!!!!Data Analytics\GuitarCenterData\guitar_sales.csv'
guitar_store_sales = pd.read_csv(file_path)

# Check the data types of columns
print("Data types of each column:")
print(guitar_store_sales.dtypes)

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


# Calculate the revenue for each sale
guitar_store_sales['Revenue'] = guitar_store_sales['Price'] * guitar_store_sales['Quantity']

# Group by 'Product Category' and 'Brand' and sum the 'Revenue'
best_selling_by_revenue = guitar_store_sales.groupby(['Product Category', 'Brand'])['Revenue'].sum()

# Sort the results in descending order of revenue
best_selling_by_revenue_sorted = best_selling_by_revenue.sort_values(ascending=False)

# Print the top products by revenue
print("Best-selling products by Category and Brand (Total Revenue):\n")
print(best_selling_by_revenue_sorted)

# Bar Chart Visualization with Matplotlib

plt.figure(figsize=(12, 6))
best_selling_by_revenue_sorted.plot(kind='bar')
plt.title('Best-Selling Products by Category and Brand (Total Revenue)')
plt.xlabel('(Product Category, Brand)')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


