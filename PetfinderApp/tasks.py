from time import sleep
from OAuth2 import PetfinderAPI
from dataEncoder import encoder

def apiThread(clientID, clientSecret,tokenURL,db, animalType):
	recordCount = 0
	pageCount = 100
	breeds = db.breedsList() 
	colors = db.colorsList()
	states = db.statesList()

	authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)
	token = authenticator.generateAccessToken()
	data = authenticator.callAPI(token,pageCount, animalType)
	dataEncoder = encoder(data)
	encodedData = dataEncoder.encodeAnimal(breeds, colors, states)

	# while True:
	# 	if recordCount < 1000:
	# 		data = authenticator.callAPI(token,pageCount, animalType)
	# 		dataEncoder = encoder(data)
	# 		dataEncoder.encodeAnimal(breeds, colors, states)
	# 		recordCount+=20
	#		pagecount+=
	# 		sleep(1)
	# 	else:
	# 		False
