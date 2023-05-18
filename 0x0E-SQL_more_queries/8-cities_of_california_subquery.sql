-- This script lists al componenets that can be found in a database.
USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC;
