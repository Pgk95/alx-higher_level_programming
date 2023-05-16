-- Prints the full description of the table first_table
SELECT CONCAT('Table	', TABLE_NAME, '     ', CREATE_TABLE)
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
	AND TABLE_NAME = 'first_table';
