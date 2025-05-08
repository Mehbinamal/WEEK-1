import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Load The CSV
df = pd.read_csv('May-8/sales_data.csv')
print("\n\nData Set\n\n",df.to_string(index=False))

#Adding A revenue column
df['Revenue'] = df['Units_Sold']*df['Price']
print("\n\nData Set After Adding Revenue\n\n",df.to_string(index=False))

df.to_csv('May-8/sales_data.csv',index=False)

#group By
product_sales = df.groupby('Product').agg({'Units_Sold': 'sum', 'Revenue': 'sum'}).reset_index()
print("\n\nGroup By Products \n\n",product_sales)

# Bar Chart 
plt.figure(figsize=(8, 5))
plt.bar(product_sales['Product'], product_sales['Revenue'])
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('May-8/Output/plotOfRevenue')
plt.show()


#nmpy mean,meadian,sd
units_array = df['Units_Sold'].to_numpy()
mean_units = np.mean(units_array)
median_units = np.median(units_array)
std_units = np.std(units_array)

print("\n NumPy Statistics on Units Sold:")
print(f"Mean: {mean_units}")
print(f"Median: {median_units}")
print(f"Standard Deviation: {std_units}")