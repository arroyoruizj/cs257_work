# cityquery.py
# author: jared arroyo ruiz

# the follwing code was created in order to determine
# the following questions from the 'us-cities-top-1k.csv'
# datset

import psycopg2

def test_query_one():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    sql = "SELECT state, city FROM cities WHERE city = 'Northfield' "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:

        print("Northfield is not in the dateset!")

    else: 

          print(row)

    conn.commit()

def test_query_two():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    max_finder = "SELECT city FROM cities WHERE population = (SELECT MAX(population) FROM cities);"
    
    cur.execute( max_finder )

    row = cur.fetchone()[0]
    print(str(row) + " is the largest city in our datset!")

    conn.commit()

def test_query_three():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    max_finder = "SELECT city FROM cities WHERE state = 'Minnesota' AND population = (SELECT MIN(population) FROM cities);"
    
    cur.execute( max_finder )

    row = cur.fetchone()[0]
    print(str(row) + " is the largest city in our datset!")

    conn.commit()

test_query_one()
test_query_two()
test_query_three()