-- database/init.sql
-- Initialization script to set up the database schema using PostgreSQL

-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Create the expenses table
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL,
    description VARCHAR(200),
    date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO users (name, email, password) VALUES
('John Doe', 'john.doe@example.com', 'hashed_password_123'),
('Jane Smith', 'jane.smith@example.com', 'hashed_password_456');

INSERT INTO expenses (user_id, category, amount, description, date) VALUES
(1, 'Groceries', 150.50, 'Weekly groceries at Walmart', '2025-01-01'),
(1, 'Utilities', 80.75, 'Electricity bill', '2025-01-02'),
(2, 'Entertainment', 120.00, 'Movie and dinner', '2025-01-03');
