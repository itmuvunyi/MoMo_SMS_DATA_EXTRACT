import xml.etree.ElementTree as ET
import os

def parse_xml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    tree = ET.parse(file_path)
    root = tree.getroot()

    transactions = []
    
    for transaction in root.findall('transaction'):
        data = {
            'id': transaction.find('id').text,
            'amount': float(transaction.find('amount').text),
            'date': transaction.find('date').text,
            'phone': transaction.find('phone').text,
            'type': transaction.find('type').text,
        }
        transactions.append(data)

    return transactions

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parse_xml.py <path_to_xml>")
        sys.exit(1)

    file_path = sys.argv[1]
    transactions = parse_xml(file_path)
    print(transactions)