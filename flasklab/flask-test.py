import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def addition(num1, num2):
    sum = str(int(num1) + int(num2))
    return "The sum of your numbers is: " + sum

@app.route('/pop/<abbrev>')
def pop(abbrev):

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="arroyoruizj",
        user="arroyoruizj",
        password="sunshine987chip")

    cur = conn.cursor()

    sql = "SELECT pop, code FROM states WHERE code = %s"
    
    cur.execute(sql, [abbrev])
    
    row = cur.fetchone()[0]

    return str(row)

if __name__ == '__main__':
    my_port = 5112
    app.run(host='0.0.0.0', port = my_port) 