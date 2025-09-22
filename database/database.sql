- Customers
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    fullName VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

-- Transaction Categories
CREATE TABLE Transaction_categories (
    category_id SERIAL PRIMARY KEY,
    categoryName VARCHAR(40) NOT NULL,
    description VARCHAR(30)
);

-- Transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,
    partyA INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    partyB INT NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    CONSTRAINT fk_partyA FOREIGN KEY (partyA) REFERENCES Customers(customer_id),
    CONSTRAINT fk_partyB FOREIGN KEY (partyB) REFERENCES Customers(customer_id)
);

-- System Logs
CREATE TABLE System_Logs (
    log_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    category_id INT NOT NULL,
    transaction_id INT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_log_customer FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT fk_log_transaction FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
    CONSTRAINT fk_log_category FOREIGN KEY (category_id) REFERENCES Transaction_categories(category_id)
);

INSERT INTO Customers (fullName, phoneNumber) VALUES
('Alice Johnson', '254700111111'),
('Bob Smith', '254700222222'),
('Charlie Brown', '254700333333'),
('Diana Prince', '254700444444'),
('Ethan Hunt', '254700555555');
INSERT INTO Transaction_categories (categoryName, description) VALUES
('Transfer', 'Money transfer between accounts'),
('Payment', 'Payment for goods or services'),
('Withdrawal', 'Cash withdrawal from account'),
('Deposit', 'Money deposit into account');

INSERT INTO Transactions (partyA, partyB, amount) VALUES
('254700111111', '254700222222', 1500.00),
('254700333333', '254700444444', 250.75),
('254700555555', '254700111111', 3000.00),
('254700222222', '254700333333', 450.50),
('254700444444', '254700555555', 120.00);

-- Sample System Logs
INSERT INTO System_Logs (customer_id, category, transaction_id) VALUES
(1, 'Transfer', 1),
(2, 'Payment', 2),
(3, 'Withdrawal', 3),
(3, 'Withdrawal', 3),
(4, 'Deposit', 4),
(5, 'Transfer', 5);