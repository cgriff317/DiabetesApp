import unittest
import os
import pandas as pd
from app import load_and_process_data  # Adjust import according to your actual file structure and function names

class TestLoadAndProcessData(unittest.TestCase):
    def setUp(self):
        # This method will be run before each test
        self.base_directory = r"C:\Users\crgriffin\PycharmProjects\Diabetes"
        self.filename = "Diabetes.csv"
        self.filepath = os.path.join(self.base_directory, self.filename)

    def test_data_loading(self):
        """Test that data is loaded correctly."""
        df = load_and_process_data(self.filepath)
        self.assertIsInstance(df, pd.DataFrame)  # Check if it returns a DataFrame
        self.assertFalse(df.empty)  # Check if DataFrame is not empty

    def test_column_presence(self):
        """Test that the expected columns are present in the DataFrame."""
        df = load_and_process_data(self.filepath)
        expected_columns = {'Glucose', 'BloodPressure', 'Insulin'}  # Adjust these columns as per your dataset
        self.assertTrue(set(df.columns).issuperset(expected_columns))

    def test_data_types(self):
        """Test data types are as expected."""
        df = load_and_process_data(self.filepath)
        self.assertTrue(pd.api.types.is_numeric_dtype(df['Glucose']))
        self.assertTrue(pd.api.types.is_numeric_dtype(df['BloodPressure']))
        # Add more type checks as necessary

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
