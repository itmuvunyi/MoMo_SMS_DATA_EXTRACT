def categorize_transaction(transaction):
    """
    Categorizes a transaction based on simple rules.

    Args:
        transaction (dict): A dictionary representing a transaction.

    Returns:
        str: The category of the transaction.
    """
    amount = transaction.get('amount', 0)
    description = transaction.get('description', '').lower()

    if 'grocery' in description:
        return 'Grocery'
    elif 'dining' in description or 'restaurant' in description:
        return 'Dining'
    elif 'transport' in description or 'taxi' in description:
        return 'Transport'
    elif amount < 0:
        return 'Refund'
    else:
        return 'Other'


def categorize_transactions(transactions):
    """
    Applies categorization to a list of transactions.

    Args:
        transactions (list): A list of transaction dictionaries.

    Returns:
        list: A list of transactions with their categories.
    """
    for transaction in transactions:
        transaction['category'] = categorize_transaction(transaction)
    return transactions