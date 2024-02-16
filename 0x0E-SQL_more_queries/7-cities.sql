-- creates the database hbtn_0d_usa and the table cities
-- DDL query to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- to start the database
USE hbtn_0d_0;
-- creates the table
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL, name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states(id));
