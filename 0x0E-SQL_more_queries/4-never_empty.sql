-- creates the table id_not_null on your MySQL server.
-- DDL query
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name
 VARCHAR(200) NOT NULL);
