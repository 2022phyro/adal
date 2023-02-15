-- THis prints all the genres of the movie Dexter
SELECT name FROM tv_genres
WHERE id IN 
	(SELECT genre_id FROM tv_show_genres
	 WHERE tv_show_genres.show_id = 
		(SELECT id FROM tv_shows
		  WHERE title = 'Dexter'
		)
	)
ORDER BY name ASC;
