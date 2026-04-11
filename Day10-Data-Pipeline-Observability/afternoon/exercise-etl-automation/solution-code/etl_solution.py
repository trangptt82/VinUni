import json
import pandas as pd
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'

def extract(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def validate(data):
    valid_records = []
    dropped_records = []
    
    for record in data:
        # Check Price
        if record.get('price', 0) <= 0:
            dropped_records.append({"id": record.get('id'), "reason": "Price <= 0"})
            continue
            
        # Check Category
        if not record.get('category'):
            dropped_records.append({"id": record.get('id'), "reason": "Missing Category"})
            continue
            
        valid_records.append(record)
        
    print(f"Validation summary: {len(valid_records)} kept, {len(dropped_records)} dropped.")
    if dropped_records:
        print(f"Errors found: {dropped_records}")
    return valid_records

def transform(data):
    df = pd.DataFrame(data)
    
    # Logic 1: Discount
    df['discounted_price'] = df['price'] * 0.9
    
    # Logic 2: Formatting
    df['category'] = df['category'].str.title()
    
    # Logic 3: Metadata (Observability)
    df['processed_at'] = datetime.datetime.now().isoformat()
    
    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Successfully loaded {len(df)} records to {output_path}")

if __name__ == "__main__":
    raw_data = extract(SOURCE_FILE)
    if raw_data:
        clean_data = validate(raw_data)
        final_df = transform(clean_data)
        load(final_df, OUTPUT_FILE)
    else:
        print("Pipeline aborted: No data extracted.")
