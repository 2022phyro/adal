-- THis prints all the genres which the show Dexter is not classified under
SELECT name FROM tv_genres
WHERE id NOT IN (
	SELECT genre_id FROM tv_show_genres
	WHERE tv_show_genres.show_id = (
		SELECT id FROM tv_shows
		  WHERE title = 'Dexter'
	)
)
ORDER BY name ASC;
