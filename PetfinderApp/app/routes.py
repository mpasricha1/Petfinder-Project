from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
import config
import threading
import time
from dbConnector import dbConnector
from neuralNetwork import petfinderNeuralNetwork
from tasks import apiThread, apiSearchAnimal, prepDataForProfile
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

trainData = db.getTrainData()
neuralNetwork = petfinderNeuralNetwork(trainData)
neuralNetwork.trainNetwork()

@app.route('/')
@app.route('/index')
def index():
	updateList = []

	testData = db.getTestData()
	proccessedData = neuralNetwork.predict(testData,0)


	for i,j in zip(proccessedData, testData):
		record = {}
		id = j[0]
		score = np.argmax(i, axis=0)

		record["id"] = id 
		record["score"] = score
		updateList.append(record)
	print(updateList)
	return render_template("index.html")

@app.route('/getdata')
def getdata():
	# t1 = threading.Thread(target=apiThread, args=(clientID3, clientSecret3, tokenURL, db, "dog", "adopted"), daemon = True)
	# t1.start()
	# t2 = threading.Thread(target=apiThread, args=(clientID4, clientSecret4, tokenURL, db, "cat", "adopted"), daemon = True)
	# t2.start()
	t3 = threading.Thread(target=apiThread, args=(clientID3, clientSecret3, tokenURL, db, "dog", "adoptable"), daemon = True)
	t3.start()
	t4 = threading.Thread(target=apiThread, args=(clientID4, clientSecret4, tokenURL, db, "cat", "adoptable"), daemon = True)
	t4.start()

	return "Test"

@app.route('/tool', methods=["GET","POST"])
def tool():
	if request.method == "POST":
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")
		empid = request.form.get("inputEmpID")


	return render_template("tool2.html", data=None)

@app.route("/analytics", methods=["GET"])
def analytics():
	return render_template("analytics.html")

@app.route("/howitworks")
def howitworks(): 
	return render_template("howitworks.html")

@app.route("/getanalysisdata")
def getanalysisdata(): 
	data = db.getAnalysisData()
	return jsonify(data)

@app.route("/searchanimal", methods=["POST"])
def searchanimal():
	returnAnimal = {}
	if request.method == "POST": 
		petId = request.form.get("inputPetID")
		testData = apiSearchAnimal(clientID5,clientSecret5,tokenURL,db,petId)
		proccessedData = neuralNetwork.predict(testData,1)
		testData = prepDataForProfile(testData,db,proccessedData)

		print(testData)
		return render_template("tool2.html", data=testData)
		

	return redirect('/tool')