import csv
import sys
import os
import pandas as pd

'''
class functions():
    def __init__(self,file_path) :
        self.file_path = file_path'''

def save_insurance_data_to_csv(text_file_path, csv_file_name='insurance_text_data.csv'):
    """Load insurance data from a text file and save it as a CSV."""
    # Read the text file into a DataFrame
    df = pd.read_csv(text_file_path, delimiter='|')
    
    # Create the path for the 'data' folder one level up
    data_folder = os.path.abspath(os.path.join(os.getcwd(), '..', 'data'))
    os.makedirs(data_folder, exist_ok=True)  # Create 'data' folder if it doesn't exist

    # Define the full path for the CSV file
    csv_file_path = os.path.join(data_folder, csv_file_name)
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"Data saved to {csv_file_path}")

# Example usage
#txt_to_csv('data.txt', 'data.csv', delimiter='\t', new_delimiter=',')  # For tab-separated text file

