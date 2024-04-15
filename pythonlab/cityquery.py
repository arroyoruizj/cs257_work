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

    sql = "SELECT city, population FROM population WHERE MAX(population) "
    
    cur.execute( sql )

    row = cur.fetchone()

    print(row[0])

    conn.commit()

test_query_one()
test_query_two()