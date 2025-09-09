import os
import logging
from etl.parse_xml import parse_xml
from etl.clean_normalize import clean_normalize
from etl.categorize import categorize
from etl.load_db import load_db
import json

# Configure logging
logging.basicConfig(filename='data/logs/etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_etl(xml_file, json_output):
    try:
        logging.info("Starting ETL process")
        
        # Step 1: Parse XML
        logging.info("Parsing XML file")
        transactions = parse_xml(xml_file)
        
        # Step 2: Clean and normalize data
        logging.info("Cleaning and normalizing data")
        cleaned_data = clean_normalize(transactions)
        
        # Step 3: Categorize transactions
        logging.info("Categorizing transactions")
        categorized_data = categorize(cleaned_data)
        
        # Step 4: Load data into the database
        logging.info("Loading data into the database")
        load_db(categorized_data)
        
        # Step 5: Export cleaned data to JSON
        logging.info("Exporting cleaned data to JSON")
        with open(json_output, 'w') as json_file:
            json.dump(categorized_data, json_file)
        
        logging.info("ETL process completed successfully")
    
    except Exception as e:
        logging.error(f"Error during ETL process: {e}")

if __name__ == "__main__":
    xml_input_file = os.path.join('data', 'raw', 'momo.xml')
    json_output_file = os.path.join('data', 'processed', 'dashboard.json')
    run_etl(xml_input_file, json_output_file)