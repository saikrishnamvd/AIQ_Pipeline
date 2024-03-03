import psycopg2
from psycopg2 import OperationalError

def setup_database():
    dbname = "newdb100"
    user = "postgres"
    password = "admin"
    host = "192.168.29.26"
    port = "5432"  # default PostgreSQL port is 5432
    
    try:
        # Connect to PostgreSQL server
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='admin',
            host='192.168.29.26'
        )
        
        conn.autocommit = True
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute SQL command to create a new database
        cursor.execute(f'CREATE DATABASE {dbname}')
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Establish a connection to the newly created database
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        
        # SQL statements to create tables
        create_table_queries = [
            """CREATE TABLE Sales_Data (
                id SERIAL PRIMARY KEY,
                Order_id Integer,
                Customer_id Integer,
                Product_id Integer,
                Quantity Integer,
                Price Float,
                Order_date Date);""",
            """CREATE TABLE Weather_Data (
                id SERIAL PRIMARY KEY,
                Latitude Float,
                Longitude Float,
                City TEXT,
                weather_description TEXT,
                Temperature Float,
                Humidity Integer,
                WindSpeed Float);""",
            """CREATE TABLE User_Address (
                id SERIAL PRIMARY KEY,
                customer_id Integer,
                street TEXT,
                suite TEXT,
                city TEXT,
                zipcode TEXT,
                latitude Float,
                longitude Float);""",
            """CREATE TABLE User_Data (
                id SERIAL PRIMARY KEY,
                customer_id Integer,
                name TEXT,
                username TEXT,
                email TEXT,
                phone TEXT);""",
            """CREATE TABLE product_data (
                id SERIAL PRIMARY KEY,
                product_id Integer,
                avg_quantity Float,
                total_quantity Float);""",
            """CREATE TABLE weather_metrics (
                id SERIAL PRIMARY KEY,
                weather TEXT,
                average_price FLOAT,
                total_sales FLOAT,
                total_qty FLOAT);""",
            """CREATE TABLE Total_Sales (
                id SERIAL PRIMARY KEY,
                Customer_id Integer,
                Total_Sales Integer);""",
            """CREATE TABLE merged_data (
                id SERIAL PRIMARY KEY,
                customer_id Integer,
                name TEXT,
                username TEXT,
                email TEXT,
                phone TEXT,
                Order_id Integer,
                Product_id Integer,
                Quantity Integer,
                Price Float,
                Order_date Date,
                street TEXT,
                suite TEXT,
                city TEXT,
                zipcode TEXT,
                latitude Float,
                longitude Float,
                weather TEXT,
                Temperature Float,
                Humidity Integer,
                WindSpeed Float);"""
        ]
        
        # Execute SQL statements to create tables
        for query in create_table_queries:
            cursor.execute(query)
        
        # Commit the transaction
        conn.commit()
        print('Tables Created in the DB')
        
    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if conn:
            cursor.close()
            conn.close()

# Call the function to set up the database and create tables
setup_database()
