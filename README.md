# AIQ_Pipeline

# Comprehensive Sales Data Pipeline
This project aims to build a comprehensive sales data pipeline for a retail company. The pipeline combines generated sales data with data from external sources, performs data transformations and aggregations, and stores the final dataset in a PostgreSQL database. The goal is to enable analysis and derive insights into customer behavior and sales performance.

# Setup Instructions
1. Ensure you have Python installed on your machine. You can download it from python.org.
2. Install the required Python packages using pip. You can install them by running the following command:
![image](https://github.com/saikrishnamvd/AIQ_Pipeline/assets/81354542/1a011436-2fad-49f3-b03e-b76fc9b4d67b)
3. Make sure you have PostgreSQL installed on your machine. You can download it from postgresql.org.
4. Create a new PostgreSQL database with the name postgres and provide the necessary permissions to access it.
5. The details of the PostgreSQL database like dbname, user, password, host and port needs to be updated in db_creation.py anddata_storage.py
6. The host ip shall be same as the ip of the local machine in which the PostgreSQL is running.
7. Make sure connections are allowed at the host ip from docker to connect with PostgreSQL database. If no, make changes in the pg_hba.conf file as below:
![image](https://github.com/saikrishnamvd/AIQ_Pipeline/assets/81354542/c3d650fd-43f6-4e61-b75e-192840073849)

# Usage
1. Clone this repository to your local machine in VSCode:

![image](https://github.com/saikrishnamvd/AIQ_Pipeline/assets/81354542/76200f9b-d80a-491b-ae11-8d07506846fd)

3. Run the Python script main.py to execute the data pipeline:

![image](https://github.com/saikrishnamvd/AIQ_Project/assets/81354542/1a9631f8-77d8-4b7e-a8c5-94d62437a50d)

4. Alternatively, the entire code is dockerized. You can directly pull the docker and run the container as below:
![image](https://github.com/saikrishnamvd/AIQ_Pipeline/assets/81354542/c382180e-378f-4451-9d55-27e19e206a88)
![image](https://github.com/saikrishnamvd/AIQ_Pipeline/assets/81354542/ae977e14-6bb5-453b-8e63-d52b80c5f8b5)
    *Replace 'container_name', 'host_port', 'container_port', 'username/repository' with respective details.
   
5. The script will perform the following tasks:
    Fetch user data from the JSONPlaceholder API endpoint.
    Merge the user data with the sales data based on the customer_id field.
    Fetch weather data for each sale using the OpenWeatherMap API.
    Perform data transformations and aggregations.
    Stores the data visualization plots in a separate folder.
    Store the transformed data in the PostgreSQL database.

7. After running the script, you can access the final dataset and analysis results in the PostgreSQL database.

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
