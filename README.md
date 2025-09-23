# MoMo SMS Dashboard

## Project Overview
The MoMo SMS Dashboard is an enterprise-level full-stack application designed to process MoMo SMS data in XML format. The application cleans and categorizes the data, stores it in a relational database, and provides a frontend interface for analysis and visualization. This project demonstrates backend data processing, database management, and frontend development.

## Database Design

The database is structured to efficiently store and relate customer information, transaction details, transaction categories, and system logs. Below is a summary of the schema:

### Tables & Relationships

#### 1. Customers
- **customer_id** (PK): Unique identifier for each customer.
- **fullName**: Customer's full name.
- **phoneNumber**: Customer's phone number (unique).

#### 2. Transactions
- **transaction_id** (PK): Unique identifier for each transaction (auto-increment).
- **partyA**: Phone number of the sender (references Customers).
- **partyB**: Phone number of the receiver (references Customers).
- **transaction_date**: Date and time of the transaction.
- **amount**: Transaction amount.
- **transactionType**: Type/category of transaction.

#### 3. Transaction_categories
- **category_id** (PK): Unique identifier for each category.
- **categoryName**: Name of the transaction category.
- **description**: Description of the category.

#### 4. System_Logs
- **log_id** (PK): Unique identifier for each log entry.
- **customer_id** (FK): References Customers.
- **transactionType**: Type/category of transaction.
- **transaction_id**: References Transactions.
- **transaction_date**: Date and time of the log entry.

### Relationships
- **Customers** are linked to **Transactions** via phone numbers.
- **Transactions** reference **Transaction_categories** for classification.
- **System_Logs** track actions/events, referencing both **Customers** and **Transactions**.

### Example Data Structure

See [`examples/jsomodal.json`](examples/jsomodal.json) for sample data reflecting this schema.

### ERD DOCS

See [`docs/MoMo_SMS_DATA_EXTRACT_Database_implementation.pdf`](docs/MoMo_SMS_DATA_EXTRACT_Database_implementation.pdf) for more information about database.

---

## Team Name
### Third Dimension

## Scrumboard Link
```bash
https://momosmsdataextract.atlassian.net/jira/software/projects/MSDE/list?atlOrigin=eyJpIjoiNDUwMDUwZGViMWFiNDcxZGE0MzYxMjk0ZTU5YTFkMTQiLCJwIjoiaiJ9
```

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd momo-sms-dashboard
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Copy the `.env.example` to `.env` and set the necessary environment variables, including `DATABASE_URL` or the path to the SQLite database.

5. **Run the ETL Process**
   Execute the ETL process to parse, clean, categorize, and load the data into the database:
   ```bash
   ./scripts/run_etl.sh
   ```

6. **Serve the Frontend**
   To serve the frontend dashboard, run:
   ```bash
   ./scripts/serve_frontend.sh
   ```

## Team Members
- Innocent Tito Muvunyi
- Twariki Abdalazizi
- Flavienne BENIHIRWE
