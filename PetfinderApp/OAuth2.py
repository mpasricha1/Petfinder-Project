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

	def callAPI(self,token, page, type, status):
		headers = {
	    	'Authorization': f'Bearer {token["access_token"]}',
		}
		params = {
	    	"page": f"{page}",
	    	"status": f"{status}", 
	    	"type" : f"{type}"

		}
		return requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params).json()

	def callAPIPetSearch(self,token,petId):
		headers = {
			'Authorization': f'Bearer {token["access_token"]}',
		}
		return requests.get(f'https://api.petfinder.com/v2/animals/{petId}', headers=headers).json()
