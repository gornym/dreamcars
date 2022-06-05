from flask import Flask, render_template
from flask import request
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/motorcycle')
def motorcycle():
    return render_template('motorcycle.html')

@app.route('/yacht')
def yacht():
    return render_template('yacht.html')


if __name__ == '__main__':
    app.run(debug=True)
