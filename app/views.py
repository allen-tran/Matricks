from re import L
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("base.html")

@views.route('/addition')
def addition():
    return render_template("addition.html")

@views.route('/multiplication')
def multiplication():
    return render_template("multiplication.html")
    
@views.route('/inverse')
def inverse():
    return render_template("inverse.html")