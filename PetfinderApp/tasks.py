from time import sleep
from OAuth2 import PetfinderAPI
from dataEncoder import encoder

def apiThread(clientID, clientSecret,tokenURL,db, animalType):
	recordCount = 0
	
	breeds = db.breedsList() 
	colors = db.colorsList()
	states = db.statesList()

	while True:
		if recordCount < 1000:
			try:
				pageCount = db.getPageCount(animalType)
				authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)
				token = authenticator.generateAccessToken()
				data = authenticator.callAPIAdopted(token,pageCount, animalType)
				dataEncoder = encoder(data)
				encodedData = dataEncoder.encodeAnimal(breeds, colors, states, pageCount)
				db.insertNewTrainData(encodedData)
				recordCount+=20
				sleep(1)
			except:
				print("Error skipping page")

		else:
			False
