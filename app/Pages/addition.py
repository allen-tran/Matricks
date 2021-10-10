from flask import Flask, redirect, url_for, render_template, request
import numpy as np
from get_matrix import instantiate_matrix

app = Flask(__name__, template_folder='../templates')

@app.route("/addition")
def home():
    return render_template("home.html")

@app.route("/add",methods = ['POST'])
def add():
    if request == 'POST':
        m = request.form['dim']
        n = request.form['dim2']

        a = np.zeros((m, n), dtype=int)
        u = len(a)

        for i in range(u):
            for j in range(len(a[i])):
                x = int(input("Enter element: "))
                a[i][j] = x
        
        j = request.form['dim3']
        k = request.form['dim4']
        
        b = np.zeros((j, k), dtype=int)
        v = len(b)

        for i in range(v):
            for j in range(len(b[i])):
                x = int(input("Enter element: "))
                b[i][j] = x
        return render_template("base.html", sum = np.add(a, b))
    return

if __name__ == "__main__":
    app.run(debug = True)