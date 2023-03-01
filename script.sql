-- Create a new database 
CREATE DATABASE ecomstore CHARACTER SET utf8;
-- Create a new MySQL user with a password.
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
-- Grant the new MySQL user permissions to manipulate the database.
GRANT ALL ON ecomstore.* TO 'username'@'localhost';