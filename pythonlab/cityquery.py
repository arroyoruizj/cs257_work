# cityquery.py
# author: jared arroyo ruiz

# the follwing code was created in order to do
# the following tasks given the 'us-cities-top-1k.csv' dataset:

# - Determine if Northfield is present in the database. 
#   If it is, print its location (Latitude and Longitude). 
#   If it is not, print an appropriate message for the user.

# - Print out the name of the city with the largest population.

# - Print out the name of the city in Minnesota with the smallest population.

# - Print out the names of the cities that is furthest North, furthest 
#   East, furthest South, and furthest West

# - Have the user enter a State from the keyboard. Print the Total 
#   population of all the cities in that state. The user should be 
#   able to enter either an abbreviation or the full name of the sate. 
#   If the user enters an abbreviation, then you should look up the abbreviation 
#   in the second table to learn the full name of the state.

import psycopg2

def test_query_one():
    
    # Environment
    # Establishing connection to server

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    # Q1
    northfield_finder = "SELECT state, city FROM cities WHERE city = 'Northfield' "
    
    cur.execute(northfield_finder)

    row = cur.fetchone()

    # If Northfield is present in dataset
    if row == None:

        print("Northfield is not in the dataset!" + "\n")

     # If Northfield is not present in dataset
    else: 

          print(row)
          print()

    # Q2
    max_finder = "SELECT city FROM cities WHERE population = (SELECT MAX(population) FROM cities);"
    
    cur.execute( max_finder )

    row = cur.fetchone()[0]
    print(str(row) + " is the largest city in our dataset!" + "\n")

    # Q3
    mn_max_finder = "SELECT city FROM cities WHERE population = (SELECT MIN(population) FROM cities WHERE state = 'Minnesota');"
    
    cur.execute(mn_max_finder)

    row = cur.fetchone()[0]
    print(str(row) + " has the smallest population in Minnesota!" + "\n")

    # Q4

    # Identifies most northern city
    north_finder = "SELECT city FROM cities WHERE latitude = (SELECT MAX(latitude) FROM cities)"
    cur.execute(north_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most northern city!")

    # Identifies most southern city
    south_finder = "SELECT city FROM cities WHERE latitude = (SELECT MIN(latitude) FROM cities)"
    cur.execute(south_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most southern city!")

    # Identifies most eastern city
    east_finder = "SELECT city FROM cities WHERE longitude = (SELECT MAX(longitude) FROM cities)"
    cur.execute(east_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most eastern city!")


    # Identifies most western city
    west_finder = "SELECT city FROM cities WHERE longitude = (SELECT MIN(longitude) FROM cities)"
    cur.execute(west_finder)
    row = cur.fetchone()[0]
    print(str(row) + " is the most western city!" + "\n")

    # Q5
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
    
    #Checks to see if user has provided an appropiate state
    if total_pop == 0:

        print("ERROR: Please choose a valid state name or abbreviation!")

    else:

        print(str(chosen_state) + " has a total population of: " + str(total_pop))

    conn.commit()


test_query_one()