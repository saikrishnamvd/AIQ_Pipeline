# AIQ_Pipeline

# Comprehensive Sales Data Pipeline
This project aims to build a comprehensive sales data pipeline for a retail company. The pipeline combines generated sales data with data from external sources, performs data transformations and aggregations, and stores the final dataset in a PostgreSQL database. The goal is to enable analysis and derive insights into customer behavior and sales performance.

# Setup Instructions
1. Ensure you have Python installed on your machine. You can download it from python.org.
2. Install the required Python packages using pip. You can install them by running the following command:

![image](https://github.com/saikrishnamvd/AIQ_Project/assets/81354542/c9e7faba-c02f-46e7-adb5-8391eac4b81e)

3. Make sure you have PostgreSQL installed on your machine. You can download it from postgresql.org.
4. Create a new PostgreSQL database with the name postgres and provide the necessary permissions to access it.

# Usage
1. Clone this repository to your local machine:

![image](https://github.com/saikrishnamvd/AIQ_Project/assets/81354542/7bb8385b-ba38-4538-9806-8df57313baf7)

2. Navigate to the project directory:

![image](https://github.com/saikrishnamvd/AIQ_Project/assets/81354542/e99219ff-0489-43ac-add7-154d1b909330)

3. Run the Python script main.py to execute the data pipeline:

![image](https://github.com/saikrishnamvd/AIQ_Project/assets/81354542/1a9631f8-77d8-4b7e-a8c5-94d62437a50d)

4. The script will perform the following tasks:
    Fetch user data from the JSONPlaceholder API endpoint.
    Merge the user data with the sales data based on the customer_id field.
    Fetch weather data for each sale using the OpenWeatherMap API.
    Perform data transformations and aggregations.
    Store the transformed data in the PostgreSQL database.

5. After running the script, you can access the final dataset and analysis results in the PostgreSQL database.

# Components and Functionality
1. Data Fetching: The script fetches user data from the JSONPlaceholder API and weather data from the OpenWeatherMap API.
2. Data Transformation: It performs various data transformations such as merging datasets, normalizing JSON data, and extracting relevant information.
3. Data Aggregation: The script aggregates sales data based on customer, product, and weather metrics.
4. Data Storage: The final dataset is stored in a PostgreSQL database with appropriate tables and schemas.

# Dependencies
    Python
    pandas
    requests
    psycopg2
    sqlalchemy
    matplotlib
    seaborn

# Data Manipulation and Aggregations
1. Total sales amount per customer.
2. Average order quantity per product.
3. Top-selling products.
4. Sales trends over time (monthly and quarterly).
5. Analysis of sales data based on weather conditions.
