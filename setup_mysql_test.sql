-- Create a test database for HBNB (Holberton Airbnb) project
-- Safe creation pattern prevents errors on repeated execution
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a test user for the HBNB project
-- User can only connect from localhost with the specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the test database to the test user
-- This gives full control over the test database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT (read-only) privileges on performance_schema for monitoring
-- This allows limited access to MySQL performance monitoring data
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply privilege changes immediately without requiring server restart
FLUSH PRIVILEGES;
