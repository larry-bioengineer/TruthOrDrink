# Larry To
# Created on: 5/6/2020
# A web app for True or Drink game which display questions on a card and users can click through it 

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	return render_template("home.html")

@app.route("/adult", methods = ["GET", "POST"])
def adult():
	if request.method == "POST":
		str = 'How would you rate your oral sex skills out of 10?'
		return render_template("adult.html", content=str)

if __name__ == "__main__":
	app.run(debug=True)