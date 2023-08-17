-- This is a script that lists all cities contained in the database hbtn_0d_usa

SELECT c.id, c.name, s.name
FROM states AS s
JOIN cities AS c ON c.state_id = s.id;
