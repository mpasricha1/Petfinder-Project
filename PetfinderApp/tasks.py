from time import sleep
from OAuth2 import PetfinderAPI
from dataEncoder import encoder

def apiThread(clientID, clientSecret,tokenURL, breeds, colors,states, animalType):
	recordCount = 0
	pageCount = 1
	authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)
	token = authenticator.generateAccessToken()

	while True:
		if recordCount < 1000:
			data = authenticator.callAPI(token,pageCount, animalType)
			dataEncoder = encoder(data)
			dataEncoder.encodeAnimal(breeds, colors, states)
			recordCount+=20
			sleep(1)
		else:
			False

	
	print(f"In Thread {number}")