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
			animal["petType"] = 1
		else:
			animal["petType"] = 2
		animal["petName"] = request.form.get("petName")
		animal["age"]= request.form.get("petAge")
		animal["primaryBreed"] = request.form.get("breed1")
		animal["secondaryBreed"] = request.form.get("breed2")
		animal["primaryColor"] = request.form.get("color1")
		animal["secondaryColor"] = request.form.get("color2")
		animal["thirdColor"] = 49
		animal["furLenghth"] = request.form.get("furlenghth")
		animal["breedSize"] == request.form.get("breedSize")
		if request.form.get("goodKids") != None:
			animal["goodKids"] = 1
		else: 
			animal["goodKids"] = 0
		if request.form.get("goodCats") != None:
			animal["goodCats"] = 1 
		else: 
			animal["goodCats"] = 0 
		if request.form.get("goodDogs") != None:
			animal["goodDogs"] = 1
		else:
			animal["goodDogs"] = 0 
		if request.form.get("vaccinated") != None: 
			animal["vac"] = 1 
		else:
			animal["vac"] = 0
		if request.form.get("dewormed") != None: 
			animal["worm"] = 1
		else:
			animal["worm"] = 0
		if request.form.get("sterilized") != None:
			animal["ster"] = 1
		else:
			animal["ster"] = 0
		animal["photoCount"] = request.form.get("photoCount")
		animal["vidCount"] = request.form.get("videoCount")

	print(animal)
	
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
		proccessedData = neuralNetwork.predict(testData,True,True)
		testData = prepDataForProfile(testData,db,proccessedData)

		print(testData)
		return render_template("tool2.html", data=testData)
		

	return redirect('/tool')