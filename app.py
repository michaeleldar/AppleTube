from crypt import methods
from fileinput import filename
from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
def index():
    url_for('static', filename="style.css")
    url_for('static', filename="script.js")
    return render_template('index.html')

@app.route('/games', methods = ['GET', 'POST'])
def games():
    url_for('static', filename="style.css")
    url_for('static', filename="script.js")
    return render_template('games.html')

@app.route('/scratchtube')
def scratchtube():
    url_for('static', filename="style.css")
    url_for('static', filename="script.js")
    return render_template('scratchtube.html')

@app.route('/tutorials')
def tutorials():
    url_for('static', filename="style.css")
    url_for('static', filename="script.js")
    return render_template('tutorials.html')








@app.route('/games/Escape_From_Syria_1.4')
def games_Escape_From_Syria_1_4(): 
    url_for('static', filename='style.css')
    url_for('static', filename='script.js')
    return render_template('games/Escape_From_Syria_1.4.html')
