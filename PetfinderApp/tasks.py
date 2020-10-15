from time import sleep
from OAuth2 import PetfinderAPI
from dataEncoder import encoder
import numpy as np

def apiThread(clientID, clientSecret,tokenURL,db, animalType, status):
	recordCount = 0
	
	breeds = db.breedsList() 
	colors = db.colorsList()
	states = db.statesList()

	if status == "adopted":
		maxCalls = 1000
	else:
		maxCalls = 100

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
	dataEncoder = encoder(data)
	encodedData = dataEncoder.encodeSingleAnimal(breeds,colors,states)

	return encodedData

def prepDataForProfile(data, db, results): 
	score = np.argmax(results[0], axis=0)
	data["adoption_speed"] = score
	data["age"] = int(data["age"]) / 12
	data["age"] = int(data["age"])

	if data["breed1"] != None:
 		data["breed1"] = db.getBreed(data["breed1"])
	if score == 0:
		data["adoption_speed"] = "Same Day"
	elif score == 1:
		data["adoption_speed"] = "1 to 7 Days"
	elif score == 2:
		data["adoption_speed"] = "8 to 30 Days"
	elif score == 3:
		data["adoption_speed"] = "31 to 90 Days"
	else:
		data["adoption_speed"] = "Over 90 Days"
	if data["type"] == 1:
		data["type"] = "Dog"
	else:
		data["type"] = "Cat"

	return data


