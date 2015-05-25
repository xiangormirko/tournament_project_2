#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        conn = psycopg2.connect("dbname=tournament")
        return conn
    except psycopg2.Error as e:
        print("There was an error stablishing conneciton\
             with the database")


def deleteMatches():
    """Remove all the match records from the database."""
    # standard database action
    # connection, cursor, execute query, commit, close
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()
    print("Match records have been erased")


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()
    print("Player records have been erased")


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    players = c.fetchall()[0][0]
    DB.close()
    return players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # takes in a name and registers a player
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()
    print("A new player named {} joined the tournament".format(name))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # fetches from a view called standings

    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM standings;")
    standing = []

    for row in c.fetchall():
        if row[3] == None:
            standing.append((row[0], row[1], 0, 0))
        else:
            standing.append(row)
    DB.close()

    return standing


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # registers a match result with winner and loser

    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches VALUES (%s, %s)", (winner, loser))
    DB.commit()
    DB.close()
    print("A match data has been recorded")


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # the view in the database is organized with id, name
    # ordered by amount of winnings
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM pairings;")
    standings = c.fetchall()
    pairings = []
    i = 0
    # the code goes through ever 2 pair and appends them
    if len(standings) % 2 != 0:
        print("Odd number of players! please recruite another player")
    else:
        while i < len(standings):
            player1 = standings[i]
            player2 = standings[i+1]
            pair = player1+player2
            pairings.append(pair)
            i += 2
    DB.close()

    return pairings
