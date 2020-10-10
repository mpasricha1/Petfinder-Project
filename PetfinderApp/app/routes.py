from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session
import config
import time
from OAuth2 import PetfinderAPI
from dataEncoder import encoder
from neuralNetwork import petfinderNeuralNetwork
from app import app 

clientID1 = config.API_KEY_1
clientSecret1 = config.SECRET_KEY_1

clientID2 = config.API_KEY_2
clientSecret2 = config.SECRET_KEY_2

clientID3 = config.API_KEY_3
clientSecret3 = config.SECRET_KEY_3
tokenURL = "https://api.petfinder.com/v2/oauth2/token"

engine = create_engine(f"postgresql+psycopg2://postgres:postgres@localhost/adoption_db")
Base = automap_base()
Base.prepare(engine,reflect=True)

Animal = Base.classes.animal
Breed = Base.classes.breed
Color = Base.classes.color
State = Base.classes.state 

@app.route('/')
@app.route('/index')
def index(): 
	return render_template("index.html")

@app.route('/getdata')
def getdata():
	session = Session(engine)
	moreData = True
	currentPage = 10

	# breeds = session.query(Breed.breed_id, Breed.breed_name).all()
	# colors = session.query(Color.color_id, Color.color_name)

	# authenticator = PetfinderAPI(clientID1, clientSecret1, tokenURL)
	# authenticator2 = PetfinderAPI(clientID2, clientSecret2, tokenURL)

	# token = authenticator.generateAccessToken()
	# data = authenticator.callAPI(token,currentPage, "dog")

	# dataEncoder = encoder(data)
	# dataEncoder.parseAnimal(breeds, colors)

	sel = [Animal.type, Animal.age, Animal.breed1, Animal.breed2, Animal.gender, Animal.color1,
		   Animal.color2, Animal.color3, Animal.maturity_size, Animal.furlength, Animal.vaccinated, 
		   Animal.dewormed, Animal.sterilized, Animal.health, Animal.fee, Animal.adoption_speed ]

	trainData = session.query(*sel).\
		   filter(Animal.test_train == 'train').all()

	testData = session.query(*sel).\
		filter(Animal.test_train == 'test').all()

	neuralNetwork = petfinderNeuralNetwork(trainData)
	neuralNetwork.trainNetwork()
	neuralNetwork.predict(testData)

	session.close()
	return "Hello"
	#jsonify(data)