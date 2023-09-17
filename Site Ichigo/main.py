from flask import Flask
from flask import render_template, request

app = Flask(__name__)




@app.route("/")
def index():
    return render_template('Index.html')

@app.route("/Hollow.html")
def hollow():
    return render_template('Hollow.html')

