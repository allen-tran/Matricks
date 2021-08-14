from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='../templates')

@app.route("/<name>")
def home(name):
    return render_template("index.html", content = name, r= 2)

if __name__ == "__main__":
    app.run(debug = True)