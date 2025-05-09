import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

class SalesDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.product_summary = None

    def load_data(self):
        #Load the CSV file into a DataFrame
        try:
            self.df = pd.read_csv(self.file_path)
            print("\nData Loaded Successfully:\n")
            print(self.df.to_string(index=False))
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            raise

    def save_processed_data(self, output_path=None):
        # Save the updated DataFrame back to CSV
        output_path = output_path if output_path else self.file_path
        self.df.to_csv(output_path, index=False)
        print(f"\nProcessed data saved to {output_path}")

    def analyze_by_product(self):
        # Group data by Product and calculate total Units_Sold and Revenue
        self.product_summary = self.df.groupby('Product').agg({
            'Units_Sold': 'sum',
            'Revenue': 'sum'
        }).reset_index()
        print("\nGrouped Data (Total Units Sold and Revenue by Product):\n")
        print(self.product_summary)

    def plot_revenue(self, output_dir='Output', filename='revenue_plot.png'):
        # Create and save a bar plot of Revenue by Product
        if self.product_summary is None:
            raise ValueError("Run analyze_by_product() before plotting.")

        os.makedirs(output_dir, exist_ok=True)
        plt.figure(figsize=(8, 5))
        plt.bar(self.product_summary['Product'], self.product_summary['Revenue'], color='teal')
        plt.title('Total Revenue by Product')
        plt.xlabel('Product')
        plt.ylabel('Revenue')
        plt.tight_layout()
        plot_path = os.path.join(output_dir, filename)
        plt.savefig(plot_path)
        plt.show()
        print(f"\nRevenue plot saved to {plot_path}")

    def compute_statistics(self):
        #print mean, median
        units = self.df['Units_Sold'].to_numpy()
        mean_val = np.mean(units)
        median_val = np.median(units)
        std_dev = np.std(units)

        print("\nStatistics for Units Sold:")
        print(f"Mean: {mean_val}")
        print(f"Median: {median_val}")
        print(f"Standard Deviation: {std_dev}")

        return mean_val, median_val, std_dev

    def top_selling_products(self, top_n=3):
        # Display top N products by total units sold
        if self.product_summary is None:
            self.analyze_by_product()
        top_products = self.product_summary.sort_values(by='Units_Sold', ascending=False).head(top_n)
        print(f"\nTop {top_n} Best-Selling Products (by Units Sold):\n")
        print(top_products)
        return top_products

    def top_revenue_products(self, top_n=3):
        # Display top N products by total revenue.
        if self.product_summary is None:
            self.analyze_by_product()
        top_revenue = self.product_summary.sort_values(by='Revenue', ascending=False).head(top_n)
        print(f"\nTop {top_n} Products by Revenue:\n")
        print(top_revenue)
        return top_revenue

    def low_performance_products(self, threshold_units=10):
        # List products with units sold below a certain threshold.
        if self.product_summary is None:
            self.analyze_by_product()
        low_perf = self.product_summary[self.product_summary['Units_Sold'] < threshold_units]
        print(f"\nProducts with Units Sold < {threshold_units}:\n")
        print(low_perf)
        return low_perf

    def price_units_correlation(self):
        # Compute correlation between Price and Units Sold.
        correlation = self.df['Price'].corr(self.df['Units_Sold'])
        print(f"\nCorrelation between Price and Units Sold: {correlation:.2f}")
        return correlation

    def plot_units_vs_price(self, output_dir='Output', filename='price_units_scatter.png'):
        # Scatter plot of Units Sold vs. Price.
        os.makedirs(output_dir, exist_ok=True)
        plt.figure(figsize=(6, 5))
        plt.scatter(self.df['Price'], self.df['Units_Sold'], color='darkorange')
        plt.title('Units Sold vs. Price')
        plt.xlabel('Price')
        plt.ylabel('Units Sold')
        plt.grid(True)
        plt.tight_layout()
        path = os.path.join(output_dir, filename)
        plt.savefig(path)
        plt.show()
        print(f"\nScatter plot saved to {path}")


#creating Object
analyzer = SalesDataAnalyzer('May-8/sales_data.csv')

analyzer.load_data()
analyzer.save_processed_data()
analyzer.analyze_by_product()
analyzer.plot_revenue(output_dir='May-8/Output')
analyzer.compute_statistics()
analyzer.top_selling_products(top_n=5)
analyzer.top_revenue_products()
analyzer.low_performance_products(threshold_units=20)
analyzer.price_units_correlation()
analyzer.plot_units_vs_price(output_dir='May-8/Output')
