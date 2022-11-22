#!/usr/bin/env python
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent.parent)+'\\O+00+00+03+ICICIBREEZE\\')
import breeze_connect
import mysql.connector
import mysql.connector.errorcode
import breezeValues

# Retrieve Session Token from mySQL Database
def getToken():
    try:
        cnx = mysql.connector.connect(**breezeValues.breezeConfig)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(err)
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = cnx.cursor()
        query = ("SELECT SQL_NO_CACHE TokenNumber, TimeStamp from icicitoken ORDER BY TimeStamp DESC LIMIT 1;")
        cursor.execute(query)
        for row in cursor:
            return row[0]

# Generate Session
def getSession():
    breeze = breeze_connect.BreezeConnect(api_key=breezeValues.breezeKey)
    breezeSession = getToken()
    breeze.generate_session(api_secret=breezeValues.breezeSecret, session_token=breezeSession)
    return breeze