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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
