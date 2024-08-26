# app.py
from flask import Flask, render_template, request
import requests
import random
from models import db, Intention, create_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intentions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

create_db(app)  # Inicjalizacja bazy danych

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Błąd: Dzielenie przez zero"

    return render_template('calculator.html', result=result)

@app.route('/brain_trainer')
def brain_trainer():
    return render_template('brain_trainer.html')

@app.route('/intentions')
def intentions():
    intentions_list = Intention.query.all()
    random_intention = random.choice(intentions_list).text if intentions_list else "Brak dostępnych intencji."
    return render_template('intentions.html', intention=random_intention)

@app.route('/gps')
def gps():
    # Zapytanie o informacje o IP
    ip_info = requests.get('https://ipapi.co/json/').json()
    return render_template('gps.html', ip_info=ip_info)


if __name__ == '__main__':
    app.run(debug=True)

