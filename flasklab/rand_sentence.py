from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("starter.html")

if __name__ == '__main__':
    my_port = 5112
    app.run(host='0.0.0.0', port = my_port) 