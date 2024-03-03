import unittest
import pandas as pd
import matplotlib.pyplot as plt
from data_manipulation import perform_analysis

class TestDataManipulation(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        data = {
            'customer_id': [1, 2, 3, 1, 2, 3],
            'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-02-01', '2024-02-02', '2024-02-03'],
            'Month': [1, 1, 1, 2, 2, 2],
            'Quarter': [1, 1, 1, 1, 1, 1],
            'price': [100, 200, 300, 150, 250, 350],
            'product_id': ['A', 'B', 'C', 'A', 'B', 'C'],
            'quantity': [5, 10, 15, 5, 10, 15],
            'Weather Description': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy', 'Rainy']
        }
        self.df4 = pd.DataFrame(data)

    def test_perform_analysis(self):
        # Call the function and get the returned dataframes and plots
        Total_Sales, order_data_df, sales_weather_df = perform_analysis(self.df4)

        # Assert that returned objects are dataframes
        self.assertIsInstance(Total_Sales, pd.DataFrame)
        self.assertIsInstance(order_data_df, pd.DataFrame)
        self.assertIsInstance(sales_weather_df, pd.DataFrame)

        # Assert that plots are generated
        self.assertTrue(plt.fignum_exists(1))  # Check if count plot figure exists
        self.assertTrue(plt.fignum_exists(2))  # Check if monthly sales trend figure exists
        self.assertTrue(plt.fignum_exists(3))  # Check if quarterly sales trend figure exists

        # Optionally, you can also check the content of the returned dataframes
        # Assert expected columns are present
        self.assertCountEqual(Total_Sales.columns, ['customer_id', 'price'])

if __name__ == '__main__':
    unittest.main()
