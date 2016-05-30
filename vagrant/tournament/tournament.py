#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        
        return db, cursor
    except:
        print("<error message>")

def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()

    query = "DELETE FROM matches;"
    cursor.execute(query)

    db.commit()
    db.close()
    
    

def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM players;")
  
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor.execute("SELECT * FROM players;")
    count = cursor.rowcount
    db.commit()
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    cursor.execute("INSERT INTO players (player_name) VALUES (%s)",(name,))
 
    db.commit()
    db.close()


def playerStandings():
   
    db, cursor = connect()
   
    cursor.execute("SELECT * FROM standings")
    fetch = cursor.fetchall()

    db.close()
    return fetch

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db, cursor = connect()
    cursor.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser,))

    db.commit()
    db.close()

def swissPairings():
	


    pairs=[]
    standings = playerStandings()
    db, cursor = connect()
    cursor.execute("SELECT player_ID , player_name FROM standings ORDER BY wins DESC;")
    db.commit()
    standings_count = cursor.rowcount
    standngs_ordered = cursor.fetchall()

    for i in range(0 , (len(standings)) ,2):
		pairs.append((standngs_ordered[i][0],standngs_ordered[i][1],standngs_ordered[i+1][0],standngs_ordered[i+1][1]))
	

    db.close()

    return pairs
