-- uses the specified data base and lists all genres of the show Dexter.
USE hbtn_0d_tvshows;

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE title = 'Dexter'
ORDER BY tv_genres.name ASC;
