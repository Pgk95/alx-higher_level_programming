-- Connect to the MySQL server
USE mysql;

-- Retrieve the list of databases
SELECT SCHEMA_NAME AS "Database"
FROM INFORMATION_SCHEMA.SCHEMATA;
