-- Retrieve records with score >= 10, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score
ORDER BY score DESC;
