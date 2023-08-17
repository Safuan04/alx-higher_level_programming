-- This is a script that  lists all shows contained in the database hbtn_0d_tvshows

SELECT t.title, g.genre_id
FROM tv_show_genres AS g
RIGHT JOIN tv_shows AS t ON t.id = g.show_id
ORDER BY t.title, g.genre_id ASC;ql -hlocalhost -uroot -p hbtn_0d_tvshows;
