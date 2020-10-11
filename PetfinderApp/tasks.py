from OAuth2 import PetfinderAPI
from dataEncoder import encoder

def apiThread(clientID, clientSecret,tokenURL, number, breeds, colors,states):

	authenticator = PetfinderAPI(clientID, clientSecret, tokenURL)

	token = authenticator.generateAccessToken()
	data = authenticator.callAPI(token,1, "dog")

	dataEncoder = encoder(data)
	dataEncoder.encodeAnimal(breeds, colors, states)
	print(f"In Thread {number}")