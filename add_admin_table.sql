-- SQL script to add admin management table
-- Run this in MySQL Workbench or command line

USE predicting_employees_under_stress;

-- Create admin table with correct Django naming convention
CREATE TABLE IF NOT EXISTS service_provider_admin_model (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(254) NULL,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Insert default admin (optional - you can add more admins through the web interface)
INSERT INTO service_provider_admin_model (username, password, email, is_active) 
VALUES ('SuperAdmin', 'SuperAdmin123', 'admin@company.com', TRUE)
ON DUPLICATE KEY UPDATE username=username;

-- Show the table structure
DESCRIBE service_provider_admin_model;

-- Show current admins
SELECT * FROM service_provider_admin_model;