-- The script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM hbtn_0d_usa.cities AS c 
WHERE c.state_id == 
(SELECT id FROM hbtn_0d_usa.states AS s WHERE name = 'California');