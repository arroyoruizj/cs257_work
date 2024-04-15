# createtables.py
# author: jared arroyo ruiz

# a program that executes two SQL statements, 
# which should create tables to hold the data 
# in the two data files (cities and statements).

def create_tables():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    cities_tab = "psql -f create_cities.sql"
    states_tab = "psql -f create_states.sql"
    
    cur.execute(cities_tab)
    cur.execute(states_tab)

    conn.commit()

create_tables()