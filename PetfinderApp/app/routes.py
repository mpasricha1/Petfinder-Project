from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import requests
from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
import config
from app import app 

clientID = config.API_KEY_MARK
clientSecret = config.SECRET_KEY_MARK
tokenURL = "https://api.petfinder.com/v2/oauth2/token"


@app.route('/')
@app.route('/index')
def index(): 
	return render_template("index.html")

@app.route('/callback')
def callback():
	client = BackendApplicationClient(client_id=clientID)
	oauth = OAuth2Session(client=client)
	token = oauth.fetch_token(token_url=tokenURL, client_id=clientID,
        client_secret=clientSecret)

	headers = {
	    'Authorization': f'Bearer {token["access_token"]}',
	}
	params = (
	    ('type', 'dog'),
	    ('page', '10000'),
	    ('status', 'adopted')
	)

	return jsonify(requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params).json())