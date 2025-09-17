from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, 'views')

# Define variable
@views.route('/')
def home():
    return render_template('index.html', name="Matrix")

# Define variable from URL parameter
@views.route('/profile')
def profile():
    args = request.args
    name = args.get('name')
    return render_template('index.html', name=name)

# Return JSON response
@views.route('/json')
def get_json():
    return {
        "name": "Matrix",
        "year": 1999 ,
        "city": "Zion"
    }

# Return Data
@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

# Redirect
@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))