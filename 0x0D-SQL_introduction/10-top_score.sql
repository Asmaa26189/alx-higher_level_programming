-- The script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- Records should be ordered by score (top first)
SELECT (name, score) FROM second_table WHERE score >= 10 ORDER BY score DESC;
