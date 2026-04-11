import json
import pandas as pd
import os

# --- CONGFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'

def extract(file_path):
    """
    Task 1: Load the JSON data from the file.
    """
    print(f"Extracting data from {file_path}...")
    # TODO: Load JSON 
    pass

def validate(data):
    """
    Task 2: Check for data quality issues.
    - No negative prices.
    - No missing IDs.
    """
    valid_records = []
    error_count = 0
    
    # TODO: Loop through data and keep only valid records
    
    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records

def transform(data):
    """
    Task 3: Apply business logic.
    - Discount 10%.
    - Title case categories.
    """
    # TODO: Transform data
    pass

def load(df, output_path):
    """
    Task 4: Save to CSV.
    """
    # TODO: Save using pandas
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # 1. Extract
    # 2. Validate
    # 3. Transform
    # 4. Load
    print("ETL Pipeline Started...")
