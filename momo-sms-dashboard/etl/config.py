# Configuration settings for ETL process

# File paths
RAW_DATA_PATH = 'data/raw/momo.xml'
PROCESSED_DATA_PATH = 'data/processed/dashboard.json'
DATABASE_PATH = 'data/db.sqlite3'
LOG_FILE_PATH = 'data/logs/etl.log'
DEAD_LETTER_PATH = 'data/logs/dead_letter/'

# Thresholds and categories for processing
TRANSACTION_TYPE_THRESHOLDS = {
    'low': 10,
    'medium': 100,
    'high': 1000
}

TRANSACTION_CATEGORIES = [
    'food',
    'transport',
    'entertainment',
    'utilities',
    'other'
]