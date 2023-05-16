-- Retrieve records with score >= 10, ordered by score (top first)
SELECT score,name
FROM hbtn_0c_0.second_table
WHERE score
ORDER BY score DESC;
