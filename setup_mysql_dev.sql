-- Create a development database for HBNB (Holberton Airbnb) project
-- Safe creation pattern prevents errors on repeated execution
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a development user for the HBNB project
-- User can only connect from localhost with the specified password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the development database to the dev user
-- This gives full control over the application database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges on performance_schema database for monitoring
-- This allows the user to access MySQL performance monitoring data
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply privilege changes immediately without requiring server restart
FLUSH PRIVILEGES;
