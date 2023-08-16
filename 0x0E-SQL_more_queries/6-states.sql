-- A script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;
-- Create the table states
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id)
);
