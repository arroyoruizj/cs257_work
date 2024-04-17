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

    northfield_finder = "SELECT state, city FROM cities WHERE city = 'Northfield' "
    
    cur.execute(northfield_finder)

    row = cur.fetchone()

    if row == None:

        print("Northfield is not in the dataset!" + "\n")

    else: 

          print(row)
          print()

    #fajklfdjklafjkldlkklajfdjlajlfda
    max_finder = "SELECT city FROM cities WHERE population = (SELECT MAX(population) FROM cities);"
    
    cur.execute( max_finder )

    row = cur.fetchone()[0]
    print(str(row) + " is the largest city in our daaset!" + "\n")

    #jfalkdfjakljfdklajfljdkakfldjl
    mn_max_finder = "SELECT city FROM cities WHERE population = (SELECT MIN(population) FROM cities WHERE state = 'Minnesota');"
    
    cur.execute(mn_max_finder)

    row = cur.fetchone()[0]
    print(str(row) + " has the smallest population in Minnesota!" + "\n")

    #ajkldfjalfjdsalfjklajlkfdjlalfajdlkfjkla
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
    print(str(row) + " is the most western city!" + "\n")

    #jfkldjfkdajklfdjklajkldf
    chosen_state = input(str("Please choose a state: "))
    
    if len(chosen_state) == 2:

        abb_finder = "SELECT state FROM states WHERE code = %s"
        
        cur.execute(abb_finder, [chosen_state])

        chosen_state = cur.fetchone()[0]

    all_cits_and_pops = "SELECT city, population FROM cities WHERE state = %s"

    cur.execute(all_cits_and_pops, [chosen_state])

    row_list = cur.fetchall()

    total_pop = 0

    for row in row_list:
        
        total_pop = total_pop + row[1]

    print(str(chosen_state) + " has a population of: " + str(total_pop))

    conn.commit()


test_query_one()