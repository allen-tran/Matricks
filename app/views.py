from re import L
from flask import Blueprint, render_template, request
import numpy as np

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("addition.html")

@views.route('/addition')
def addition():
    return render_template("addition.html")

@views.route('/multiplication')
def multiplication():
    return render_template("multiplication.html")

@views.route('/subtraction')
def subtraction():
    return render_template("subtraction.html")

@views.route('/determinant')
def determinant():
    return render_template("determinant.html")

@views.route('/inverse')
def inverse():
    return render_template("inverse.html")

@views.route("/add",methods = ['POST'])
def add():
    m = int(request.form['dim'])
    n = int(request.form['dim2'])

    a = np.zeros((m, n), dtype=int)
    u = len(a)

    for i in range(u):
        for j in range(len(a[i])):
            x = int(input("Enter element: "))
            a[i][j] = x
        
    j = int(request.form['dim3'])
    k = int(request.form['dim4'])
        
    b = np.zeros((j, k), dtype=int)
    v = len(b)

    for i in range(v):
        for j in range(len(b[i])):
            x = int(input("Enter element: "))
            b[i][j] = x
    return render_template("addtion.html", sum = np.add(a, b))

@views.route('/mult', methods=["POST"])
def mult():
    m = int(request.form['dim'])
    n = int(request.form['dim2'])

    a = np.zeros((m, n), dtype=int)
    u = len(a)

    for i in range(u):
        for j in range(len(a[i])):
            x = int(input("Enter element: "))
            a[i][j] = x
        
    j = int(request.form['dim3'])
    k = int(request.form['dim4'])
        
    b = np.zeros((j, k), dtype=int)
    v = len(b)

    for i in range(v):
        for j in range(len(b[i])):
            x = int(input("Enter element: "))
            b[i][j] = x
    return render_template("base.html", sum = np.add(a, b))
    
