-- TO create a user an grant all privileges
-- DDL query
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
-- DML query to grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
