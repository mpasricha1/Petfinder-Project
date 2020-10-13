from time import sleep
from OAuth2 import PetfinderAPI
from dataEncoder import encoder

def apiThread(clientID, clientSecret,tokenURL,db, animalType, status):
	recordCount = 0
	
	breeds = db.breedsList() 
	colors = db.colorsList()
	states = db.statesList()

	if status == "adopted":
		maxCalls = 1000
	else:
		maxCalls = 10

	while True:
		if recordCount < maxCalls:
			try:
				pageCount = db.getPageCount(animalType, status)
				print(pageCount)
				authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)
				token = authenticator.generateAccessToken()
				data = authenticator.callAPI(token,pageCount, animalType, status)
				dataEncoder = encoder(data)
				encodedData = dataEncoder.encodeAnimal(breeds, colors, states, pageCount)
				db.insertNewData(encodedData)
				sleep(.10)
				
			except:
				print("Error Skipping Page")
			recordCount+=1
		else:
			False
	return

def apiSearchAnimal(clientId, clientSecret, tokenURL, db, petId):
	breeds = db.breedsList() 
	colors = db.colorsList()
	states = db.statesList()

	authenticator = PetfinderAPI(clientId, clientSecret, tokenURL)
	token = authenticator.generateAccessToken()
	data = authenticator.callAPIPetSearch(token,petId)
	dataEncoder= encoder(data)
	encodedData= dataEncoder.encodeSingleAnimal(breeds,colors,states)
	print(encodedData)

	return 

	

