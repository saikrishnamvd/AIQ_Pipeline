import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Create a dedicated folder to save plots
plot_folder = 'plots'
if not os.path.exists(plot_folder):
    os.makedirs(plot_folder)

def perform_analysis(df4):
    
     
    # Create a count plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df4, x='customer_id')
    plt.title('Count of Customer IDs')
    plt.xlabel('Customer ID')
    plt.ylabel('Count')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    #plt.savefig('count_plot.png')
    plot_path = os.path.join(plot_folder, 'count_plot.png')
    plt.savefig(plot_path)

    # Analyze sales trends over time (e.g., monthly or quarterly sales).

    # Group by month and quarter, and sum sales amount
    monthly_sales = df4.groupby('Month')['price'].sum()
    quarterly_sales = df4.groupby('Quarter')['price'].sum()

    # Plot monthly sales trends
    plt.figure(figsize=(10, 5))
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales Amount')
    plt.xticks(range(1, 13))
    plt.grid(True)
    #plt.savefig('monthly_sales.png')
    plot_path = os.path.join(plot_folder, 'monthly_sales.png')
    plt.savefig(plot_path)

    # Plot quarterly sales trends
    plt.figure(figsize=(10, 5))
    quarterly_sales.plot(kind='bar', color='skyblue')
    plt.title('Quarterly Sales Trends')
    plt.xlabel('Quarter')
    plt.ylabel('Sales Amount')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    #plt.savefig('quarterly_sales.png')
    plot_path = os.path.join(plot_folder, 'quarterly_sales.png')
    plt.savefig(plot_path)


    # Total Sales Amount per Customer
    Total_Sales = df4.groupby('customer_id')['price'].sum().reset_index()

    # Average Order Quantity per product
    Avg_Order = df4.groupby('product_id')['quantity'].mean().reset_index()

    # Top Selling Products
    top_products = df4.groupby('product_id')['quantity'].sum().reset_index()
    top_products_df = top_products.sort_values(by='quantity', ascending=False)
    order_data_df = pd.merge(Avg_Order, top_products_df, on=['product_id'], how='inner')


    # Average Sales Amount per Weather Condition
    sales_weather1 = df4.groupby('Weather Description')['price'].mean().reset_index()
    sales_weather1 = sales_weather1.rename(columns={'price': 'Avg. Price'})

    sales_weather2 = df4.groupby('Weather Description')['price'].sum().reset_index()
    sales_weather2 = sales_weather2.rename(columns={'price': 'Total Price'})

    sales_weather3 = df4.groupby('Weather Description')['quantity'].sum().reset_index()
    sales_weather3 = sales_weather3.rename(columns={'quantity': 'Total Qty.'})

    sales_weather_df1 = pd.merge(sales_weather1, sales_weather2, on=['Weather Description'], how='inner')
    sales_weather_df = pd.merge(sales_weather_df1, sales_weather3, on=['Weather Description'], how='inner')

    print("data_manipulation.py is completed")
    
    return Total_Sales, order_data_df, sales_weather_df




