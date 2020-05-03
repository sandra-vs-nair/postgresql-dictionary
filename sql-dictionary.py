# -----------------------------------------------------------
# A dictionary application using python and postgreSQL.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import json
import sys
import difflib
import psycopg2

# @desc Returns the meaning of a word if found in postgreSQL table. Else, queries the user with similar words.
# If no similar words are found, displays a suitable message and exit the program.
# @param string $word - the word to which meaning is sought.
# @return void.


def definition(word):
    word=word.strip()      #Remove leading and trailing spaces.
    query = cursor.execute("SELECT definition FROM dict WHERE word = '"+word.lower()+ \   
                    "'or word = '"+word.title()+"' or word = '"+word.upper()+"'")   #Querying postgreSQL table.
    results = cursor.fetchall()
    if results:
        num,meanings= len(results),results
        i=1
        for result in results:
            print(i, result[0])
            i=i+1
    else:
        print("The word does not exist")
        query_words = cursor.execute("SELECT word FROM dict")
        out = cursor.fetchall()
        word_list = [element[0] for element in out] 
        similar_word=difflib.get_close_matches(word,word_list,1,0.7)        #Checking for similar words.
        if not similar_word:                                                #No similar words found.
            print("No similar words found. Please check and try again")
            con.close()
            sys.exit()
        response=input("Do you mean "+similar_word[0]+" ? Y or N ?")
        if response == 'Y' or response =='y':
            definition(similar_word[0])
        elif response == 'N' or response =='n':
            print("Please make sure of the spelling and type again")    
            con.close()
            sys.exit()
        else:
            print("Please type Y or N")
# connect to PostgreSQL. Enter your credentials here.
con = psycopg2.connect(user = 'postgres',password = 'password123',host="localhost",database="dictionary-database")
cursor = con.cursor()
word=input("Enter a word :")
definition(word)
con.close()                                                                #close connection.
