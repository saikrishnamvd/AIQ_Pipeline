import subprocess

from data_collection import perform_data_collection
from data_manipulation import perform_analysis
from data_storage import insert_data_to_database

df4 = perform_data_collection()

Total_Sales, order_data_df, sales_weather_df = perform_analysis(df4)

subprocess.run(["python", "db_creation.py"])

insert_data_to_database(df4, Total_Sales, order_data_df, sales_weather_df)


