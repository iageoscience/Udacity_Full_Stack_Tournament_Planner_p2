# Tournament Planner

This program uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

###Install Vagrant###
https://www.vagrantup.com/downloads

Verify that Vagrant is installed and working by typing in the terminal:

	$ vagrant -v   # will print out the Vagrant version number

###Clone the Repository###
clone this repoitory

	$ git clone https://github.com/iageoscience/Udacity_Full_Stack_Tournament_Planner.git
	$ cd udacity-swiss-tournament
	$ cd vagrant

###Verify that these files exist in the newly cloned repository:###<br>

	--tournament             #folder containing tournament files
	----tournament.py        #file that contains the python functions which unit tests will run on
							  Each function has a docstring that says what it should do
	----tournament_test.py   #unit tests that will test the functions for tournament.py
	----tournament.sql       #postgresql database schema
	--Vagrantfile            #The primary function of the Vagrantfile is to describe the type 
							  of machine required for a project, and how to configure and provision these machines.
	--pg_config.sh           #shell script provisioner called by Vagrantfile that performs some configurations 

###Launch the Vagrant Box###

	$ vagrant up   #to launch and provision the vagrant environment
		is all you need to work on any project, to install every dependency that project needs, and to set up any networking or synced folders,
		if virtualbox is not installed on the system Vagrant will take care of it and install automatically.

	$ vagrant ssh  #to SSH login to your vagrant environment

###Enter the Tournament folder###

	$ cd /
	$ cd vagrant
	$ cd tournament

###Initialize the database###

	$ psql
	vagrant=> \i tournament.sql
	vagrant=> \q


###Run the unit tests###

	$ python tournament_test.py

You should see these results:

	1. Old matches can be deleted.
	2. Player records can be deleted.
	3. After deleting, countPlayers() returns zero.
	4. After registering a player, countPlayers() returns 1.
	5. Players can be registered and deleted.
	6. Newly registered players appear in the standings with no matches.
	7. After a match, players have updated standings.
	8. After one match, players with one win are paired.
	Success!  All tests pass!

###Shutdown Vagrant machine###

	$ vagrant halt


###Destroy the Vagrant machine###

	$ vagrant destroy


###Shoutouts & References###
* http://www.tutorialspoint.com/python/python_tuples.htm
* https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
* http://initd.org/psycopg/docs/
* www.postgresql.org
* http://www.postgresguide.com/utilities/psql.html
* https://www.vagrantup.com/docs/