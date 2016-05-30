-- pair each player with an opponent who has won the same number of matches, or as close as possible.
-- Your code and database only needs to support a single tournament at a time.
-- all players who are in the database will participate in the tournament,
-- when you want to run a new tournament, all the game records from the previous tournament will need to be deleted.




--Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Drop view and Table if exists
DROP VIEW IF EXISTS winview;
DROP VIEW IF EXISTS winview;
DROP VIEW IF EXISTS standings;
DROP DATABASE IF EXISTS tournament;


-- Create Database
CREATE DATABASE tournament;

--Connect to tournament database
\c tournament;

--Players table
CREATE TABLE IF NOT EXISTS players 
	(player_ID serial primary key,player_name text,score integer);

--Matches table
CREATE TABLE IF NOT EXISTS matches 
	(match_ID serial primary key,winner integer,loser integer);


--Matchview to list number of matches for each player
CREATE VIEW  matchview AS 
	SELECT players.player_ID , players.player_name ,COUNT(matches.match_ID) AS matches 
	FROM players left join matches  on players.player_ID = matches.winner OR players.player_ID = matches.loser 
 	GROUp BY players.player_ID;


--Winview to list number of Wins for each player
CREATE VIEW  winview AS 
	SELECT players.player_ID , players.player_name ,COUNT(matches.winner) AS wins 
	FROM players left join matches ON players.player_ID = matches.winner 
    GROUP BY players.player_ID;

--Standings to list player standings

CREATE VIEW  standings AS 
	SELECT winview.player_ID , winview.player_name ,winview.wins ,matchview.matches 
	FROM winview,matchview WHERE winview.player_id = matchview.player_id;
