# Larry To
# Created on: 5/6/2020
# A web app for True or Drink game which display questions on a card and users can click through it 

from flask import Flask, render_template, url_for, request, redirect, g
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from random import randint 
import json


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	return render_template("home.html")

@app.route("/adult", methods = ["GET", "POST"])
def adult():
	

	if request.method == "POST":
		question = OptainQuestion("adult")
		str = 'How would you rate your oral sex skills out of 10?'
		return render_template("adult.html", content=question)

def normal():

	if request.method == "POST":
		question = OptainQuestion("normal")
		str = 'How would you rate your oral sex skills out of 10?'
		return render_template("adult.html", content=question)


def OptainQuestion(gameName):
	with open("Questions.json") as file:
		questions = json.load(file)

	if gameName == "adult": 
		numQuestion = len(questions["Adult"]) - 1
		questionNo = randint(0, numQuestion)
		
		return questions["Adult"][questionNo]

	elif gameName == "normal":
		questionNo = randint(0, len(questions["Normal"]))
		return question["Normal"][questionNo]

if __name__ == "__main__":
	app.run(debug=True)