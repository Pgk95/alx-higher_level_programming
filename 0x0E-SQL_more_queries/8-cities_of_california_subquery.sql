-- This script lists al componenets that can be found in a database.
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC;
