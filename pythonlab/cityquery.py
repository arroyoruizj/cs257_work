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

        print("Northfield is not in the dataset!" + "\n")

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
    print(str(row) + " is the largest city in our daaset!" + "\n")

    conn.commit()

def test_query_three():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    max_finder = "SELECT city FROM cities WHERE population = (SELECT MIN(population) FROM cities WHERE state = 'Minnesota');"
    
    cur.execute( max_finder )

    row = cur.fetchone()[0]
    print(str(row) + " has the smallest population in Minnesota!" + "\n")

    conn.commit()

def test_query_four():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    north_finder = "SELECT city FROM cities WHERE latitude = (SELECT MAX(latitude) FROM cities)"
    cur.execute(north_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most northern city!")

    south_finder = "SELECT city FROM cities WHERE latitude = (SELECT MIN(latitude) FROM cities)"
    cur.execute(south_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most southern city!")

    east_finder = "SELECT city FROM cities WHERE longitude = (SELECT MAX(longitude) FROM cities)"
    cur.execute(east_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most eastern city!")

    west_finder = "SELECT city FROM cities WHERE longitude = (SELECT MIN(longitude) FROM cities)"
    cur.execute(west_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most western city!")

    conn.commit()

def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    chosen_state = input(print("Please choose a state: "))

test_query_one()
test_query_two()
test_query_three()
test_query_four()