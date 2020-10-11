from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import requests

class PetfinderAPI:
	def __init__(self, clientID, clientSecret, tokenURL):
		self.clientID = clientID
		self.clientSecret = clientSecret
		self.tokenURL = tokenURL

	def generateAccessToken(self):
		client = BackendApplicationClient(client_id=self.clientID)
		oauth = OAuth2Session(client=client)
		token = oauth.fetch_token(token_url=self.tokenURL, client_id=self.clientID,client_secret=self.clientSecret)
		return token

	def callAPIAdopted(self,token, page, type):
		headers = {
	    	'Authorization': f'Bearer {token["access_token"]}',
		}
		params = {
	    	"page": f"{page}",
	    	"status": "adopted", 
	    	"type" : f"{type}"

		}

		# r = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
		# print(r.url)

		return requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params).json()

	def callAPIAdoptable(self,token, page, type):
		headers = {
	    	'Authorization': f'Bearer {token["access_token"]}',
		}
		params = {
	    	"page": f"{page}",
	    	"status": "adoptable", 
	    	"type" : f"{type}", 
	    	"special_needs": True

		}
		# r = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
		# print(r.url)

		return requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params).json()