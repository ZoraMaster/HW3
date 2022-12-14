import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='hw3',
                            user=os.environ['postgres'],
                            password=os.environ['jan2001'])
    return conn

@app.route('/')    
def index():    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basket_a;')
    cur.execute('INSERT INTO Basket_a(a, fruit_a) VALUES (5, \'Cherry\');')
    cur.execute('SELECT * FROM Basket_b;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)