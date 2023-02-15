-- This lists all shows which are not listed as comedy
SELECT title FROM tv_shows
WHERE id NOT IN (
	SELECT show_id FROM tv_show_genres
	WHERE genre_id = (
		SELECT id FROM tv_genres
		WHERE name = 'Comedy'
	)
)
ORDER BY title ASC;
