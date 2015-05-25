# tournament_project_2
udacity full stack nanodegree project 2 completed by Xiang Zhao Mirko
05/23/2015

GENERAL DESCRIPTION
-------------------
This is a project including sql schema in a virtual box instance using vagrant. Also include a script to create players, record matches, retrieve informations, and erase data. A unit test file is provided courtesy of Udacity

MODULES
-------------------
tournament.py: contains methods to interact with database such as create players, retrieve standings, and create swiss pairings
test_tournament.py: a unit test file to ensure that all methods behave as needed
tournament.sql: contains sql commands to create tables and views necessary

python libraries used: psycopg2

INSTALLATION
-------------------
Install Git, Vagrant, and Virtual Box
-Git: If you do not have a version of git installed, please visit http://git-scm.com/downloads
-Vagrant: in order to install Vagrant, plese visit https://www.vagrantup.com/downloads
-VirtualBox: in order to install Virtual Box, please visit https://www.virtualbox.org/wiki/Downloads

CONFIGURATION
-------------------
-git clone https://github.com/xiangormirko/tournament_project_2.git 
-using terminal navigate to the fouder in '/vagrant'
-type 'vagrant up'
-after the inizial setting up, type 'vagrant ssh' to log into the instance
-navigate to 'cd /vagrant' to access the share files

DATABASE & TABLES
-------------------
-After you are logged into vagrant type psql  
-Here type the commands to create the database tournament ('CREATE DATABASE tournament;')  
-You may check the the databases with the command '/d'  
-Connect to the database using the command ('\c tournament')  
-Import using command '/i tournament.sql' or paste sql schema to create tables and views from tournament.sql  
-Run 'python test_tournament.py' to check if the script passes all unit tests  
-Use and edit methods in tournament.py as needed  
-Thanks!  




