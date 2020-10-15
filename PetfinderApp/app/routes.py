from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
import config
import threading
import time
import numpy as np
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

trainData = db.getTrainData(True)
neuralNetwork = petfinderNeuralNetwork(trainData)
neuralNetwork.trainNetwork(True)

@app.route('/')
@app.route('/index')
def index():
	data = db.getHomeAnimalData()
	return render_template("index.html", data=data)

@app.route('/getdata')
def getdata():
	# t1 = threading.Thread(target=apiThread, args=(clientID1, clientSecret3, tokenURL, db, "dog", "adopted"), daemon = True)
	# t1.start()
	# t2 = threading.Thread(target=apiThread, args=(clientID2, clientSecret4, tokenURL, db, "cat", "adopted"), daemon = True)
	# t2.start()
	t3 = threading.Thread(target=apiThread, args=(clientID3, clientSecret3, tokenURL, db, "dog", "adoptable"), daemon = True)
	t3.start()
	t4 = threading.Thread(target=apiThread, args=(clientID4, clientSecret4, tokenURL, db, "cat", "adoptable"), daemon = True)
	t4.start()

	return "Test"

@app.route('/updatepredictions')
def updatepredictions():
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
	db.updateNewPredictions(updateList)
	return "Test"

@app.route('/tool', methods=["GET","POST"])
def tool():
	animal = {}
	breeds = db.breedsList()
	colors = db.colorsList()

	if request.method == "POST":
		animal["empId"] = request.form.get("inputEmpID")
		animal["shelterId"] = request.form.get("inputShelter")
		animal["acqDate"] = request.form.get("inputDate")
		animal["zipcode"] = request.form.get("inputZip")
		if request.form.get("sex") == "Male":
			animal["gender"] = 1
		elif request.form.get("sex") == "Female":
			animal["gender"] = 2
		else:
			animal["gender"] = 3
		if request.form.get("petType") == "Dog":
			animal["type"] = 1
		else:
			animal["type"] = 2
		animal["petName"] = request.form.get("petName")
		animal["age"]= request.form.get("petAge")
		animal["breed1"] = request.form.get("breed1")
		animal["breed2"] = request.form.get("breed2")
		animal["color1"] = request.form.get("color1")
		animal["color2"] = request.form.get("color2")
		animal["color3"] = 49
		animal["furlength"] = request.form.get("furlenghth")
		animal["maturity_size"] = request.form.get("breedsize")
		if request.form.get("breedsize") == "Small":
			animal["maturity_size"] = 1
		elif request.form.get("breedsize") == "Medium":
			animal["maturity_size"] = 2
		elif request.form.get("breedsize") == "Large":
			animal["maturity_size"] = 3
		elif request.form.get("breedsize") == "Extra Large":
			animal["maturity_size"] = 4
		else:
			animal["health"] = 5

		if request.form.get("goodKids") != None:
			animal["good_with_kids"] = 1
		else: 
			animal["good_with_kids"] = 0
		if request.form.get("goodCats") != None:
			animal["good_with_cats"] = 1 
		else: 
			animal["good_with_cats"] = 0 
		if request.form.get("goodDogs") != None:
			animal["good_with_dogs"] = 1
		else:
			animal["good_with_dogs"] = 0 
		if request.form.get("vaccinated") != None: 
			animal["vaccinated"] = 1 
		else:
			animal["vaccinated"] = 0
		if request.form.get("dewormed") != None: 
			animal["dewormed"] = 1
		else:
			animal["dewormed"] = 0
		if request.form.get("sterilized") != None:
			animal["sterilized"] = 1
		else:
			animal["sterilized"] = 0
		animal["photo_amt"] = request.form.get("photoCount")
		animal["video_amt"] = request.form.get("videoCount")
		animal["fee"] = request.form.get("fee")
		if request.form.get("health") == "Healthy":
			animal["health"] = 1
		elif request.form.get("health") == "Minor Injury":
			animal["health"] = 2
		elif request.form.get("health") == "Serious Injury":
			animal["health"] = 3
		else:
			animal["health"] = 4

	print(animal)
	# proccessedData = neuralNetwork.predict(animal,True,True)
	# data = prepDataForProfile(testData,db,proccessedData)
	return render_template("tool2.html", breeds=breeds, colors=colors, data="")

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
	breeds = db.breedsList()
	colors = db.colorsList()
	if request.method == "POST": 
		petId = request.form.get("inputPetID")
		testData = apiSearchAnimal(clientID5,clientSecret5,tokenURL,db,petId)
		proccessedData = neuralNetwork.predict(testData,True,True)
		testData = prepDataForProfile(testData,db,proccessedData)

		return render_template("tool2.html", data=testData, breeds=breeds, colors=colors)
		

	return redirect('/tool')