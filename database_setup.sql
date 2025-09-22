-- ==========================================
-- DATABASE SETUP SCRIPT: database_setup.sql
-- ==========================================

-- -----------------------------
-- 1. Drop existing tables (if any)
-- -----------------------------
DROP TABLE IF EXISTS System_Logs;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Transaction_categories;
DROP TABLE IF EXISTS Customers;

-- -----------------------------
-- 2. Customers Table
-- -----------------------------
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    fullName VARCHAR(50) NOT NULL,
    phoneNumber VARCHAR(12) NOT NULL UNIQUE
);

-- Index for faster lookups by phoneNumber
CREATE INDEX idx_customers_phone ON Customers(phoneNumber);

-- -----------------------------
-- 3. Transaction Categories Table
-- -----------------------------
CREATE TABLE Transaction_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    categoryName VARCHAR(40) NOT NULL,
    description VARCHAR(30)
);

-- Index for faster lookups by categoryName
CREATE INDEX idx_category_name ON Transaction_categories(categoryName);

-- -----------------------------
-- 4. Transactions Table
-- -----------------------------
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    partyA VARCHAR(12) NOT NULL,
    partyB VARCHAR(12) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount NUMERIC(12,2) NOT NULL,
    category_id INT,
    CONSTRAINT fk_partyA FOREIGN KEY (partyA)
        REFERENCES Customers(phoneNumber)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_partyB FOREIGN KEY (partyB)
        REFERENCES Customers(phoneNumber)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_category FOREIGN KEY (category_id)
        REFERENCES Transaction_categories(category_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Indexes for common queries
CREATE INDEX idx_transactions_partyA ON Transactions(partyA);
CREATE INDEX idx_transactions_partyB ON Transactions(partyB);
CREATE INDEX idx_transactions_category ON Transactions(category_id);

-- -----------------------------
-- 5. System Logs Table
-- -----------------------------
CREATE TABLE System_Logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    category VARCHAR(40) NOT NULL,
    transaction_id INT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_log_customer FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_log_transaction FOREIGN KEY (transaction_id)
        REFERENCES Transactions(transaction_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Index for faster log retrieval
CREATE INDEX idx_logs_customer ON System_Logs(customer_id);
CREATE INDEX idx_logs_transaction ON System_Logs(transaction_id);

-- -----------------------------
-- 6. Insert Sample Data
-- -----------------------------

-- Customers
INSERT INTO Customers (fullName, phoneNumber) VALUES
('Alice Johnson', '0700000001'),
('Bob Smith', '0700000002'),
('Charlie Brown', '0700000003'),
('Diana Prince', '0700000004'),
('Ethan Hunt', '0700000005');

-- Transaction Categories
INSERT INTO Transaction_categories (categoryName, description) VALUES
('Deposit', 'Money deposited'),
('Withdrawal', 'Money withdrawn'),
('Transfer', 'Money transferred'),
('Payment', 'Payment made'),
('Refund', 'Money refunded');

-- Transactions
INSERT INTO Transactions (partyA, partyB, amount, category_id) VALUES
('0700000001', '0700000002', 100.00, 1),
('0700000003', '0700000004', 250.50, 3),
('0700000002', '0700000005', 75.25, 2),
('0700000004', '0700000001', 300.00, 4),
('0700000005', '0700000003', 150.00, 5);

-- System Logs
INSERT INTO System_Logs (customer_id, category, transaction_id) VALUES
(1, 'Deposit', 1),
(2, 'Transfer', 1),
(3, 'Transfer', 2),
(4, 'Transfer', 2),
(5, 'Withdrawal', 3);

