-- creates the database hbtn_0d_2 and the user user_0d_2.
-- DDL query to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- DDL query to create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- query privilegs for user_0d_2
GRANT USAGE ON * . * TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2` . * TO 'user_0d_2'@'localhost';
