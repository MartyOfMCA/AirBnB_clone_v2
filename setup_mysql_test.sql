-- Set up a test database for the system

-- Create a new test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant user hbnb_test permissions to hbnb_test_db
GRANT ALL
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- Grant user hbtn_test read-only permissions to performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';

-- Enforce new permissions
FLUSH PRIVILEGES;
