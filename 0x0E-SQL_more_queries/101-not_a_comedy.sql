sts all shows without the comedy genre in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.name = "Comedy" AND tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;
