from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
import config
import threading
import time
from dbConnector import dbConnector
from neuralNetwork import petfinderNeuralNetwork
from tasks import apiThread
from app import app 

clientID1 = config.API_KEY_1
clientSecret1 = config.SECRET_KEY_1

clientID2 = config.API_KEY_2
clientSecret2 = config.SECRET_KEY_2

clientID3 = config.API_KEY_3
clientSecret3 = config.SECRET_KEY_3

clientID4 = config.API_KEY_4
clientSecret4 = config.SECRET_KEY_4

clientID5 = config.API_KEY_5
clientSecret5 = config.SECRET_KEY_5

clientID6 = config.API_KEY_6
clientSecret6 = config.SECRET_KEY_6

tokenURL = "https://api.petfinder.com/v2/oauth2/token"

db = dbConnector()
db.establishConnection()

# trainData = db.getNeuralNetworkData()
# neuralNetwork = petfinderNeuralNetwork(trainData)
# neuralNetwork.trainNetwork()

@app.route('/')
@app.route('/index')
def index():
	
	# testData = db.getTestData()
	# neuralNetwork.predict(testData)
	
	return render_template("index.html")

@app.route('/getdata')
def getdata():
	x1 = threading.Thread(target=apiThread, args=(clientID1, clientSecret1, tokenURL, db, "dog"))
	x1.start()

	x2 = threading.Thread(target=apiThread, args=(clientID2, clientSecret2, tokenURL, db, "dog"))
	x2.start()

	x3 = threading.Thread(target=apiThread, args=(clientID3, clientSecret3, tokenURL, db, "dog"))
	x3.start()

	y1 = threading.Thread(target=apiThread, args=(clientID4, clientSecret4, tokenURL, db, "cat"))
	y1.start()

	y2 = threading.Thread(target=apiThread, args=(clientID5, clientSecret5, tokenURL, db, "cat"))
	y2.start()

	y3 = threading.Thread(target=apiThread, args=(clientID6, clientSecret6, tokenURL, db, "cat"))
	y3.start()

	return "Test"

@app.route('/tool')
def tool(methods=["GET","POST"]):
	return render_template("tool.html")

@app.route("/analytics")
def analytics():
	return render_template("analytics.html")

@app.route("/howitworks")
def howitworks(): 
	return render_template("howitworks.html")