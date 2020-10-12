from time import sleep
from OAuth2 import PetfinderAPI
from dataEncoder import encoder

def apiThreadAdopted(clientID, clientSecret,tokenURL,db, animalType):
	recordCount = 0
	
	breeds = db.breedsList() 
	colors = db.colorsList()
	states = db.statesList()

	while True:
		if recordCount < 1000:
			try:
				pageCount = db.getPageCount(animalType)
				print(pageCount)
				authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)
				token = authenticator.generateAccessToken()
				data = authenticator.callAPIAdopted(token,pageCount, animalType)
				dataEncoder = encoder(data)
				encodedData = dataEncoder.encodeAnimal(breeds, colors, states, pageCount)
				db.insertNewTrainData(encodedData)
				sleep(.10)
				
			except:
				print("Error skipping page")
			recordCount+=1
		else:
			False
