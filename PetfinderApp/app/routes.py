from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session
import config
import threading
import time

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

tokenURL = "https://api.petfinder.com/v2/oauth2/token"

engine = create_engine(f"postgresql+psycopg2://postgres:postgres@localhost/adoption_db")
Base = automap_base()
Base.prepare(engine,reflect=True)

Animal = Base.classes.animal
Breed = Base.classes.breed
Color = Base.classes.color
State = Base.classes.state 

# session = Session(engine)
# sel = [Animal.type, Animal.age, Animal.breed1, Animal.breed2, Animal.gender, Animal.color1,
# 		Animal.color2, Animal.color3, Animal.maturity_size, Animal.furlength, Animal.vaccinated, 
# 		Animal.dewormed, Animal.sterilized, Animal.health, Animal.fee, Animal.adoption_speed ]

# trainData = session.query(*sel).\
# 	filter(Animal.test_train == 'train').all()

# neuralNetwork = petfinderNeuralNetwork(trainData)
# neuralNetwork.trainNetwork()

# session.close()

@app.route('/')
@app.route('/index')
def index():
	# session = Session(engine)
	# testData = session.query(*sel).\
	# 					filter(Animal.test_train == 'test').all()
	# neuralNetwork.predict(testData)
	return render_template("index.html")

@app.route('/getdata')
def getdata():
	session = Session(engine)
	moreData = True
	currentPage = 10

	breeds = session.query(Breed.breed_id, Breed.breed_name).all()
	colors = session.query(Color.color_code, Color.color_name).all()
	states = session.query(State.state_id, State.state_name)

	x = threading.Thread(target=apiThread, args=(clientID1, clientSecret1, tokenURL, breeds, colors, states, "dog"))
	x.start()

	y = threading.Thread(target=apiThread, args=(clientID2, clientSecret2, tokenURL, breeds, colors, states, "cat"))
	y.start()

	session.close()
	return "TestS"