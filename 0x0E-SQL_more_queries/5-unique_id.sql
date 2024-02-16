-- creates the table unique_id on your MySQL server.
-- DDL query to create the table
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
