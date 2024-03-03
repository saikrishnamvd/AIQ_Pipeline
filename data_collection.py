import pandas as pd
import requests

def perform_data_collection():
    # Read the sales data CSV file
    df = pd.read_csv("Sales_data.csv")

    # URL of the JSONPlaceholder API endpoint for users
    url = 'https://jsonplaceholder.typicode.com/users'

    # Sending a GET request to fetch user data
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the JSON response into a Python list of dictionaries
        users = response.json()
    else:
        print(f"Failed to fetch user data. Status code: {response.status_code}")
        users = []

    # Convert user data into a DataFrame
    df2 = pd.DataFrame(users)

    # Data Transformation - 1
    normalized_df = pd.json_normalize(df2['address'])
    df2 = pd.concat([df2, normalized_df], axis=1)
    df2 = df2.drop('address', axis=1)
    df2 = df2.rename(columns={'id': 'customer_id'})
    df3 = pd.merge(df, df2, on='customer_id', how='inner')
    df3 = df3.rename(columns={'geo.lat': 'Latitude', 'geo.lng': 'Longitude'})

    # Data Transformation - 2
    unique_coordinates = df3[['Latitude', 'Longitude']].drop_duplicates()
    api_key = '351588d54e524e74fda97f2731f4d096'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Create an empty list to store weather data
    weather_data = []

    # Iterate over unique latitude and longitude pairs and make API calls
    for index, row in unique_coordinates.iterrows():
        # Extract latitude and longitude from the current row
        latitude = row['Latitude']
        longitude = row['Longitude']

        # Construct the complete URL with parameters
        complete_url = base_url + f'lat={latitude}&lon={longitude}&appid=' + api_key

        # Make the API call
        response = requests.get(complete_url)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()

            # Extract relevant information
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Append the weather data to the list
            weather_data.append((latitude, longitude, weather_description, temperature, humidity, wind_speed))
        else:
            print(f'Failed to retrieve data for Latitude: {latitude}, Longitude: {longitude} from the API.')

    # Convert weather data into a DataFrame
    weather_df = pd.DataFrame(weather_data, columns=['Latitude', 'Longitude', 'Weather Description', 'Temperature (K)', 'Humidity (%)', 'Wind Speed (m/s)'])

    # Merge weather data with sales data
    df4 = pd.merge(df3, weather_df, on=['Latitude', 'Longitude'], how='inner')
    df4['order_date'] = pd.to_datetime(df4['order_date'])
    df4['Month'] = df4['order_date'].dt.month
    df4['Quarter'] = df4['order_date'].dt.quarter

    print('data_collection.py is completed')
    
    return df4


