

import psycopg2
from psycopg2.extras import execute_values

def insert_data_to_database(df4, Total_Sales, order_data_df, sales_weather_df):
    dbname = "newdb100"
    user = "postgres"
    password = "admin"
    host = "192.168.29.26"
    port = "5432"  # default PostgreSQL port is 5432

    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        # Convert DataFrame to a list of tuples
        required_columns = ['Latitude','Longitude','city','Weather Description','Temperature (K)','Humidity (%)', 'Wind Speed (m/s)']
        WeatherData_df = df4[required_columns].copy()
        data_tuples1 = [tuple(row) for row in WeatherData_df.to_numpy()]

        insert_query1 = """
            INSERT INTO Weather_Data (Latitude, Longitude, city, weather_description, Temperature, Humidity, WindSpeed)
            VALUES %s
        """
        execute_values(cur, insert_query1, data_tuples1)

        required_columns = ['customer_id','street','suite','city','zipcode','Latitude', 'Longitude']
        useraddress_df = df4[required_columns].copy()
        data_tuples2 = [tuple(row) for row in useraddress_df.to_numpy()]

        insert_query2 = """
            INSERT INTO User_Address (customer_id, street, suite, city, zipcode, latitude, longitude)
            VALUES %s
        """
        execute_values(cur, insert_query2, data_tuples2)

        required_columns = ['customer_id','name','username','email','phone']
        userdata_df = df4[required_columns].copy()
        data_tuples3 = [tuple(row) for row in userdata_df.to_numpy()]

        insert_query3 = """
            INSERT INTO User_Data (customer_id, name, username, email, phone)
            VALUES %s
        """
        execute_values(cur, insert_query3, data_tuples3)

        required_columns = ['order_id','customer_id','product_id','quantity','price','order_date']
        sales_table_df = df4[required_columns].copy()
        data_tuples4 = [tuple(row) for row in sales_table_df.to_numpy()]

        insert_query4 = """
            INSERT INTO Sales_Data (order_id, customer_id, product_id, quantity, price, order_date)
            VALUES %s
        """
        execute_values(cur, insert_query4, data_tuples4)

        data_tuples5 = [tuple(row) for row in Total_Sales.to_numpy()]
        insert_query5 = """
            INSERT INTO Total_Sales (customer_id, Total_Sales)
            VALUES %s
        """
        execute_values(cur, insert_query5, data_tuples5)

        data_tuples6 = [tuple(row) for row in order_data_df.to_numpy()]
        insert_query6 = """
            INSERT INTO product_data (product_id, avg_quantity, total_quantity)
            VALUES %s
        """
        execute_values(cur, insert_query6, data_tuples6)

        data_tuples7 = [tuple(row) for row in sales_weather_df.to_numpy()]
        insert_query7 = """
            INSERT INTO weather_metrics (weather, average_price, total_sales, total_qty)
            VALUES %s
        """
        execute_values(cur, insert_query7, data_tuples7)

        required_columns = ['customer_id','name','username','email','phone','order_id','product_id','quantity','price','order_date','street','suite','city','zipcode','Latitude', 'Longitude','Weather Description','Temperature (K)','Humidity (%)', 'Wind Speed (m/s)']
        sales_table_df = df4[required_columns].copy()
        data_tuples8 = [tuple(row) for row in sales_table_df.to_numpy()]

        insert_query8 = """
            INSERT INTO merged_data (customer_id, name, username, email, phone, order_id, product_id, quantity, price, order_date, street, suite, city, zipcode, latitude, longitude, weather, Temperature, Humidity, WindSpeed)
            VALUES %s
        """
        execute_values(cur, insert_query8, data_tuples8)

        # Commit the transaction
        conn.commit()
        print("Data Stored in the DB")
        
    except Exception as e:
        print(f"Error inserting data into database: {e}")
    finally:
        # Close the cursor and connection
        if conn:
            cur.close()
            conn.close()


# You can call this function by passing the required DataFrames as arguments
#insert_data_to_database(df4, Total_Sales, order_data_df, sales_weather_df)
