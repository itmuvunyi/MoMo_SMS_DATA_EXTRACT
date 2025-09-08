#!/bin/bash

# This script rebuilds the processed dashboard JSON file from the SQLite database.

# Define the path to the SQLite database and the output JSON file
DB_PATH="../data/db.sqlite3"
OUTPUT_JSON="../data/processed/dashboard.json"

# Run the Python script to export data from the database to JSON
python -c "
import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('$DB_PATH')
cursor = conn.cursor()

# Query to fetch the necessary data for the dashboard
cursor.execute('SELECT * FROM transactions')  # Adjust the query as needed
rows = cursor.fetchall()

# Convert the fetched data into a list of dictionaries
columns = [column[0] for column in cursor.description]
data = [dict(zip(columns, row)) for row in rows]

# Write the data to the JSON file
with open('$OUTPUT_JSON', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Close the database connection
conn.close()
"