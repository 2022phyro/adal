-- This lists all shows which are listed as comedy
SELECT title FROM tv_shows
WHERE id IN (
	SELECT show_id FROM tv_show_genres
	WHERE genre_id = (
		SELECT id FROM tv_genres
		WHERE name = 'Comedy'
	)
)
ORDER BY title ASC;
