# createtables.py
# author: jared arroyo ruiz

# a program that executes two SQL statements, 
# which should create tables to hold the data 
# in the two data files (cities and statements).

import psycopg2

def create_tables():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    cities_tab = """DROP TABLE IF EXISTS cities_df;
                    CREATE TABLE cities_df (
                    city TEXT,
                    state TEXT,
                    population NUMERIC(8,0),
                    latitude NUMERIC(5, 2),
                    longitude NUMERIC(5, 2));"""""
    
    states_tab = """DROP TABLE IF EXISTS states_df;
                    CREATE TABLE states_df (
                    code TEXT,
                    state TEXT,
                    pop NUMERIC(8,0));"""
    
    cur.execute(cities_tab)
    cur.execute(states_tab)

    conn.commit()

create_tables()