from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
import config
import time
from OAuth2 import PetfinderAPI
#from dataEncoder import encoder
from app import app 

clientID1 = config.API_KEY_MARK
clientSecret1 = config.SECRET_KEY_MARK

clientID2 = config.API_KEY_KRISTIN
clientSecret2 = config.SECRET_KEY_KRISTIN

clientID3 = config.API_KEY_MELISSA
clientSecret3 = config.SECRET_KEY_MELISSA
tokenURL = "https://api.petfinder.com/v2/oauth2/token"


@app.route('/')
@app.route('/index')
def index(): 
	return render_template("index.html")

@app.route('/getdata')
def getdata():
	moreData = True
	currentPage = 10

	authenticator = PetfinderAPI(clientID1, clientSecret1, tokenURL)
	token = authenticator.generateAccessToken()
	data = authenticator.callAPI(token,currentPage)

	# dataEncoder = encoder(data)
	# dataEncoder.encodeData()

	return jsonify(data)