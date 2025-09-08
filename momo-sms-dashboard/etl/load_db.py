import sqlite3
import os

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create tables in the SQLite database."""
    try:
        sql_create_transactions_table = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            phone TEXT NOT NULL,
            category TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_transactions_table)
    except sqlite3.Error as e:
        print(e)

def upsert_transaction(conn, transaction):
    """Insert or update a transaction in the database."""
    sql = """
    INSERT INTO transactions (amount, date, phone, category)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        amount = excluded.amount,
        date = excluded.date,
        phone = excluded.phone,
        category = excluded.category;
    """
    cursor = conn.cursor()
    cursor.execute(sql, transaction)
    conn.commit()

def load_data_to_db(db_file, transactions):
    """Load cleaned transaction data into the SQLite database."""
    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn)
        for transaction in transactions:
            upsert_transaction(conn, transaction)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), '../data/db.sqlite3')
    # Example transaction data to load
    example_transactions = [
        (100.0, '2023-01-01', '1234567890', 'Food'),
        (50.5, '2023-01-02', '0987654321', 'Transport'),
    ]
    load_data_to_db(db_path, example_transactions)