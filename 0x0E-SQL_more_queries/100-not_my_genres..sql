-- The script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT DISTINCT name
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS s
       ON g.id = s.genre_id

       INNER JOIN tv_shows AS t
       ON s.show_id = t.id
       WHERE g.name NOT IN
             (SELECT name
                FROM tv_genres AS g
	             INNER JOIN tv_show_genres AS s
		     ON g.id = s.genre_id

		     INNER JOIN tv_shows AS t
		     ON s.show_id = t.id
		     WHERE t.title = "Dexter")
 ORDER BY g.name;
 