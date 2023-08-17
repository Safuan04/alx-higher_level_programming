-- This is a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT t.title, g.genre_id
FROM tv_show_genres AS g
JOIN tv_shows AS t ON t.id = g.show_id
ORDER BY t.title, g.genre_id ASC;
