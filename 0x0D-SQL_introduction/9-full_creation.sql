-- This is a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

CREATE TABLE IF EXISTS second_table(
        id int,
        name varchar(256),
        score int
        );
INSERT INTO second_table (id, name, score) VALUES(1, "John", 10),(2, "Alex", 3),(2, "Bob", 14),(4, "George", 8);
