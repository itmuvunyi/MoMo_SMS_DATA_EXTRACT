# Project Documentation

## Table of Contents

1. [Transaction Categories CRUD](#transaction-categories-crud)
2. [Customers CRUD](#customers-crud)
3. [Transactions CRUD](#transactions-crud)
4. [System Logs CRUD](#system-logs-crud)
5. [JSON Data Modeling](#json-data-modeling)

---

## Transaction Categories CRUD

```sql
-- Insert Transaction Categories
INSERT INTO Transaction_categories (categoryName, description) VALUES
('Deposit', 'Money deposited into account'),
('Withdrawal', 'Money withdrawn from account'),
('Loan', 'Loan issued to customer'),
('Penalty', 'Late payment penalty'),
('Transfer', 'Money transferred between users');

-- Results
-- AffectedRows: 5

-- Select All Transaction Categories
SELECT * FROM Transaction_categories;

-- Update a Category Name
UPDATE Transaction_categories
SET categoryName = 'Bank Deposit'
WHERE category_id = 1;
-- Results: AffectedRows: 1

-- Delete a Transaction Category
DELETE FROM Transaction_categories
WHERE category_id = 5;
-- Results: AffectedRows: 1
```

## Customers CRUD

```sql
-- Create Users / Customers
INSERT INTO Customers (fullName, phoneNumber) VALUES
('Abdalazizi Twariki', '0784889737'),
('Flaviene Benihirwe', '0781234567'),
('Inocent Tito', '0787654321');
-- Results: AffectedRows: 3

-- Select All Users
SELECT * FROM Customers;

-- Update a Customer Name
UPDATE Customers
SET fullName = 'Abdalazizi T.'
WHERE phoneNumber = '0784889737';
-- Results: AffectedRows: 1

-- Delete a Customer
DELETE FROM Customers
WHERE phoneNumber = '0787654321';
-- Results: AffectedRows: 1
```

## Transactions CRUD

```sql
-- Insert Transactions
INSERT INTO Transactions (partyA, partyB, amount, category_id) VALUES
('0784889737', '0781234567', 150.00, 1),
('0781234567', '0784889737', 200.00, 2);
-- Results: AffectedRows: 2

-- Update Transaction Amount
UPDATE Transactions
SET amount = 175.00
WHERE transaction_id = 1;
-- Results: AffectedRows: 1

-- Delete a Transaction
DELETE FROM Transactions
WHERE transaction_id = 2;
-- Results: AffectedRows: 1
```

## System Logs CRUD

```sql
-- Insert a Log Entry
INSERT INTO System_Logs (customer_id, category, transaction_id) VALUES
(1, 'Deposit', 1);
-- Results: AffectedRows: 1

-- Select All Logs
SELECT * FROM System_Logs;
```

## JSON Data Modeling

### Customers

```json
{
  "customer_id": 1,
  "fullName": "Abdalazizi T.",
  "phoneNumber": "0784889737"
}
```

### Transaction Categories

```json
{
  "category_id": 1,
  "categoryName": "Bank Deposit",
  "description": "Money deposited into account"
}
```

### Transactions

```json
{
  "transaction_id": 1,
  "partyA": "0784889737",
  "partyB": "0781234567",
  "transaction_date": "2025-09-22T14:30:00Z",
  "amount": 175.00,
  "category_id": 1
}
```

### System Logs

```json
{
  "log_id": 1,
  "customer_id": 1,
  "category": "Deposit",
  "transaction_id": 1,
  "transaction_date": "2025-09-22T14:30:05Z"
}
```

### Complex Transaction Object (Nested)

```json
{
  "transaction_id": 1,
  "transaction_date": "2025-09-22T14:30:00Z",
  "amount": 175.00,
  "category": {
    "category_id": 1,
    "categoryName": "Bank Deposit",
    "description": "Money deposited into account"
  },
  "partyA": {
    "customer_id": 1,
    "fullName": "Abdalazizi T.",
    "phoneNumber": "0784889737"
  },
  "partyB": {
    "customer_id": 2,
    "fullName": "Flaviene Benihirwe",
    "phoneNumber": "0781234567"
  }
}
```

---

*This Markdown file provides a structured, professional presentation of the database CRUD operations, system logs, and JSON modeling for API serialization.*
