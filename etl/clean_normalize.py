import re
from datetime import datetime

def clean_amount(amount_str):
    """Clean and normalize the amount string."""
    try:
        # Remove any currency symbols and commas
        amount = re.sub(r'[^\d.]', '', amount_str)
        return float(amount)
    except ValueError:
        return None

def clean_date(date_str):
    """Clean and normalize the date string."""
    try:
        # Parse the date string into a standard format
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None

def clean_phone(phone_str):
    """Clean and normalize the phone number string."""
    # Remove non-numeric characters
    return re.sub(r'\D', '', phone_str)

def normalize_data(transaction):
    """Normalize the transaction data."""
    transaction['amount'] = clean_amount(transaction.get('amount', ''))
    transaction['date'] = clean_date(transaction.get('date', ''))
    transaction['phone'] = clean_phone(transaction.get('phone', ''))
    return transaction