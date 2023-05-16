-- List all records with a name va;ue from second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER by score DESC;
