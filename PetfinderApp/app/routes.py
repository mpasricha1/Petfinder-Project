from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import requests
from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
import config
from OAuth2 import PetfinderAPI
from app import app 

clientID = config.API_KEY_MARK
clientSecret = config.SECRET_KEY_MARK
tokenURL = "https://api.petfinder.com/v2/oauth2/token"


@app.route('/')
@app.route('/index')
def index(): 
	return render_template("index.html")

@app.route('/getdata')
def getdata():
	authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)
	token = authenticator.generateAccessToken()
	data = authenticator.callAPI(token)

	return jsonify(data)