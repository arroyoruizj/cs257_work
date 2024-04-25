from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("starter.html")

@app.route('/random/sentence/')
def rand_sent_gen():

    adjectives = ['aggressive', 'boring', 'clueless', 'dazzling', 'eager',
                  'fantastic', 'gorgeous', 'heavenly', 'impressionable', 'jumpy',
                  'kind', 'lawful', 'majestic', 'naive', 'optimistic',
                  'playful', 'quiet', 'radiant', 'sarcastic', 'talkative',
                  'unpleasant', 'vigilant', 'weird', 'xanthic', 'young', 'zesty']
    
    names = ['Asher', 'Blake', 'Charlie', 'Daniel', 'Emery',
             'Florence', 'Grayson', 'Hayden', 'Indigo', 'Jamie',
             'Keagan', 'Lark', 'Miles', 'Nolan', 'Olive',
             'Peyton', 'Quinn', 'Riley', 'Spencer', 'Tate',
             'Ulysse', 'Valentine', 'Wren', 'Xennon', 'Yale', 'Zuri']
    
    random_adj = random.choice(adjectives)
    random_name = random.choice(names)

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    sql = "SELECT city FROM cities"
    
    cur.execute(sql)
    
    all_cities = list(cur.fetchall())

    random_city = random.choice(all_cities)

    random_year = random.randint(0, 2024)

    return render_template("random_sent.html", 
                           randAdj = random_adj, 
                           randName = random_name, 
                           randCity = random_city, 
                           randYear = random_year)

if __name__ == '__main__':
    my_port = 5112
    app.run(host='0.0.0.0', port = my_port) 