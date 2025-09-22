# CRUD OPERATION TEST

```sql
-- 1. Creating Users / Customers
INSERT INTO Customers (fullName, phoneNumber) VALUES
('Abdalazizi Twariki', '0784889737'),
('Flaviene Benihirwe', '0781234567'),
('Inocent Tito', '0787654321');

-- Results
-- INSERT INTO Customers (fullName, phoneNumber) VALUES
-- ('Abdalazizi Twariki', '0784889737'),
-- ('Flaviene Benihirwe', '0781234567'),
-- ('Inocent Tito', '0787654321');
-- AffectedRows : 3

-- 2. Select All Users
SELECT * FROM Customers;

-- Results
-- customer_id | fullName             | phoneNumber
-- 1           | Abdalazizi Twariki  | 0784889737
-- 2           | Flaviene Benihirwe  | 0781234567
-- 3           | Inocent Tito        | 0787654321

-- 3. Update User Name
UPDATE Customers
SET fullName = 'Abdalazizi T.'
WHERE phoneNumber = '0784889737';

-- Results
-- UPDATE Customers SET fullName = 'Abdalazizi T.' WHERE phoneNumber = '0784889737';
-- AffectedRows : 1

SELECT * FROM Customers WHERE phoneNumber = '0784889737';

-- Results
-- customer_id | fullName       | phoneNumber
-- 1           | Abdalazizi T. | 0784889737

-- 4. Delete a User
DELETE FROM Customers
WHERE phoneNumber = '0787654321';

-- Results
-- DELETE FROM Customers WHERE phoneNumber = '0787654321';
-- AffectedRows : 1

SELECT * FROM Customers;

-- Results
-- customer_id | fullName             | phoneNumber
-- 1           | Abdalazizi T.       | 0784889737
-- 2           | Flaviene Benihirwe  | 0781234567

-- 5. Insert Transactions
INSERT INTO Transactions (partyA, partyB, amount, category_id) VALUES
('0784889737', '0781234567', 150.00, 1),
('0781234567', '0784889737', 200.00, 2);

-- Results
-- INSERT INTO Transactions (partyA, partyB, amount, category_id) VALUES
-- ('0784889737', '0781234567', 150.00, 1),
-- ('0781234567', '0784889737', 200.00, 2);
-- AffectedRows : 2

SELECT * FROM Transactions;

-- Results
-- transaction_id | partyA      | partyB      | transaction_date       | amount  | category_id
-- 1              | 0784889737 | 0781234567 | (current timestamp)   | 150.00  | 1
-- 2              | 0781234567 | 0784889737 | (current timestamp)   | 200.00  | 2

-- 6. Update Transaction Amount
UPDATE Transactions
SET amount = 175.00
WHERE transaction_id = 1;

-- Results
-- UPDATE Transactions SET amount = 175.00 WHERE transaction_id = 1;
-- AffectedRows : 1

SELECT * FROM Transactions WHERE transaction_id = 1;

-- Results
-- transaction_id | partyA      | partyB      | transaction_date       | amount  | category_id
-- 1              | 0784889737 | 0781234567 | (current timestamp)   | 175.00  | 1

-- 7. Delete a Transaction
DELETE FROM Transactions
WHERE transaction_id = 2;

-- Results
-- DELETE FROM Transactions WHERE transaction_id = 2;
-- AffectedRows : 1

SELECT * FROM Transactions;

-- Results
-- transaction_id | partyA      | partyB      | transaction_date       | amount  | category_id
-- 1              | 0784889737 | 0781234567 | (current timestamp)   | 175.00  | 1
