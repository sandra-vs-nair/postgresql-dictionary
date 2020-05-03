# -----------------------------------------------------------
# Converting a json file to postgresql table.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import psycopg2
import os
import json

# loading a json file.
data=json.load(open("data/dictionary.json"))   

# connect to PostgreSQL. Enter your credentials here.
con = psycopg2.connect(user = 'postgres',password = 'password123',host="localhost", \
      database="dictionary-database")
cursor = con.cursor()

# parse json data and insert it into postgreSQL table.
# for each word there can be a number of meanings.
for term in data.keys():                  
    meanings = data[term]
    for meaning in meanings:                                 
        word = term
        definition = meaning
        cursor.execute("INSERT INTO dict (word, definition) VALUES (%s,%s)", (word,definition))
con.commit()
con.close()