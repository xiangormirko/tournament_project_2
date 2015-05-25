-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;
DROP VIEW IF EXISTS wins;
DROP VIEW IF EXISTS count;
DROP VIEW IF EXISTS standings;
DROP VIEW IF EXISTS pairings;


CREATE TABLE players ( name TEXT,
                     id SERIAL PRIMARY KEY );


CREATE TABLE matches ( winner INT references players (id),
                     loser INT references players (id),
                     match_id SERIAL PRIMARY KEY);

--A view named wins to display wins grouped by player and ordered by wins
CREATE VIEW wins AS 
SELECT p.id, p.name, COUNT(m.winner) 
AS winnings FROM players p 
LEFT JOIN matches m  
ON p.id = m.winner 
GROUP BY p.id 
ORDER BY winnings DESC;

--A view named count to display total number of matches played by player
CREATE VIEW count AS 
SELECT players.id, players.name, COUNT(matches) 
AS total_matches FROM players 
LEFT JOIN matches 
ON players.id = winner OR players.id = loser 
GROUP BY players.id ORDER BY players.id;  

--A view named standings to display current standings of players
CREATE VIEW standings 
AS SELECT players.id, players.name, wins.winnings, count.total_matches 
FROM players, wins, count 
WHERE players.id = wins.id AND wins.id = count.id 
ORDER BY wins.winnings DESC;

--A simple view to facilitate the pairing of players
CREATE VIEW pairings AS 
SELECT standings.id, standings.name 
FROM standings;



