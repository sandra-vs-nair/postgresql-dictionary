## Dictionary application using Python and PostgreSQL.

This project demonstrates a dictinary application using python and postgreSQL. The user is prompted for an input which is expected to be the word to which the meaning is sought for. It deals with two scenarios.
1. Word is found: Here, the meaning of the word is displayed.
2. Word is not found: Here, the dictionary is checked for similar words.
	(a) If similar words are found, the user is queried whether it is the word he actually meant. If yes, meaning of the word is returned, else a suitable message is displayed and program is exited.
	(b) If similar words are not found, a suitable message is displayed and program is exited.

# Prerequisites

The dictionary data should be saved as a table in postgreSQL. The data is provided as a json file dictionary.json. For connecting with postgeSQL, a python module psycopg2 should be installed. Inorder to install that, use the command

````
pip install psycopg2

````
If it doesn't work, use

````
pip3 install psycopg2

````

# Usage

To create the postgreSQL database:
1. Login to postgreSQL and create a database named dictionary-database. 
2. Within the database, create a table named dict.
3. The table dict should have two columns
    (a) word 
    (b) definition
Both columns should be of character varying datatype.
4. After creating the database, enter your username and password in appropriate places inside the json-to-postgresql.py and sql-dictionary.py

Run the python file json-to-postgresql.py. Use the commands below in any terminal.
```
python json-to-postgresql.py

```
or if the python version is 3, use command.

```
python3 json-to-postgresql.py

```
or you can also use any python IDE.

5. Now you can see that the postgreSQL table is populated with words and their meanings. After this run sql-dictionary.py.

Run the python file json-to-postgresql.py. Use the commands below in any terminal.
```
python sql-dictionary.py

```
or if the python version is 3, use command.

```
python3 sql-dictionary.py

```
When prompted, enter the word to know its meaning.
