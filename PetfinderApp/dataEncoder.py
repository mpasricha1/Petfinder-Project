import pandas as pd
from pprint import pprint
from datetime import datetime

class encoder:
	def __init__(self, data):
		self.data = data 

	def encodeAnimal(self,breeds, colors, states):
		newAnimals = []

		for row in self.data["animals"]:
			animal = {}

			if row["type"] == "Dog":
				animal["type"] = 1
			else: 
				animal["type"] = 2
			animal["name"] = row["name"]
			if row["size"].lower() == "small" or row["size"].lower() == "medium":
				if row["age"].lower() == "baby": 
					animal["age"] = 12
				elif row["age"].lower() == "young": 
					animal["age"] = 3 * 12
				elif row["age"].lower() == "adult": 
					animal["age"] = 6 * 12
				elif row["age"].lower() == "senior": 
					animal["age"] = 10 * 12
			elif row["size"].lower() == "large" or row["size"].lower() == "xlarge":
			 	if row["age"].lower() == "baby":
			 		animal["age"] = 18
			 	elif row["age"].lower() == "young":
			 		animal["age"] = 4 * 12
			 	elif row["age"].lower() == "adult":
			 		animal["age"] = 7 * 12
			 	elif row["age"].lower() == "senior":
			 		animal["age"] = 12 * 12
			for breed in breeds:
				if row["breeds"]["primary"] == None:
					animal["breed1"] = 308
				else:
					if row["breeds"]["primary"] == breed.breed_name: 
						animal["breed1"] = breed.breed_id
					else:
						animal["breed1"] = 308
				if row["breeds"]["secondary"] == None:
 					animal["breed2"] = 308
				else:
					if row["breeds"]["secondary"] == breed.breed_name:
						animal["breed2"] = breed.breed_id
					else:
						animal["breed2"] = 308
			if row["gender"].lower() == "Male":
				animal["gender"] = 1 
			else: 
				animal["gender"] = 2
			for color in colors: 
				if row["colors"]["primary"] == None:
					animal["color1"] = 49
				else:
					if row["colors"]["primary"] == color.color_name:
						animal["color1"] = color.color_code
					else:
						animal["color1"] = 49
				if row["colors"]["secondary"] == None:
					animal["color2"] = 49
				else:
					if row["colors"]["secondary"] == color.color_name:
						animal["color2"] = color.color_code
					else:
						animal["color2"] = 49
				if row["colors"]["tertiary"] == None:
					animal["color3"] = 49
				else:
					if row["colors"]["tertiary"] == color.color_name:
						animal["color3"] = color.color_code
					else:
						animal["color3"] = 49
			if row["size"] == None:
				animal["maturity_size"] = 0
			else:
				if row["size"] == None:
					animal["maturity_size"] = 0
				else:
					if row["size"].lower() == "small": 
						animal["maturity_size"] = 1
					elif row["size"].lower() == "medium":
						animal["maturity_size"] = 2 
					elif row["size"].lower() == "large": 
							animal["maturity_size"] = 3
					elif row["size"].lower() == "xlarge": 
						animal["maturity_size"] = 4
			if row["coat"] == None: 
				animal["furlength"] = 0
			else:
				if row["coat"].lower() == "short":
					animal["furlength"] = 1 
				elif row["coat"].lower() == "medium": 
					animal["furlength"] = 2
				elif row["coat"].lower() == "long": 
					animal["furlength"] = 3 
				elif row["coat"].lower() == "wire":
					animal["furlength"] = 4
				elif row["coat"].lower() == "hairless": 
					animal["furLlength"] = 5
			if row["attributes"]["shots_current"] == True:
				animal["vaccinated"] = 1
			if row["attributes"]["shots_current"] == False:
				animal["vaccinated"] = 2
			if row["attributes"]["shots_current"] == None:
				animal["vaccinated"] = 3
			animal["dewormed"] = 0 	
			if row["attributes"]["spayed_neutered"] == True:
				animal["sterilized"] = 1
			if row["attributes"]["spayed_neutered"] == False:
				animal["sterilized"] = 2
			if row["attributes"]["spayed_neutered"] == None:
				animal["sterilized"] = 3
			if row["attributes"]["special_needs"] == True:
				animal["health"] = 2 
			if row["attributes"]["special_needs"] == False: 
				animal["health"] = 1 
			if row["attributes"]["special_needs"] == None: 
				animal["health"] = 0 
			animal["quantity"] = 1
			animal["fee"] = 0
			for state in states: 
				if row["contact"]["address"]["state"] == state.state_name: 
						animal["state_name"] = state.state_id
				else: 
					animal["state_name"] = 51
			animal["rescuer_id"] = row["organization_id"]
			animal["video_amt"] = len(row["videos"])
			animal["description"] = row["description"]
			animal["pet_id"] = row["id"]
			animal["photo_amt"] = len(row["photos"])
			if row["status"].lower() == "adopted":
				startDate = datetime.strptime(row["published_at"][:10], "%Y-%m-%d")
				endDate = datetime.strptime(row["status_changed_at"][:10], "%Y-%m-%d")
				adoptionSpeed = abs((startDate - endDate).days)
				animal["adoption_speed"] = adoptionSpeed
			animal["test_train"] = "train"
			if len(row["photos"]) > 1:
				animal["photo1_small"] = row["photos"][0]["small"]
				animal["photo1_med"] = row["photos"][0]["medium"]
				animal["photo2_small"] = row["photos"][1]["small"]
				animal["photo2_med"] = row["photos"][1]["medium"]
			elif len(row["photos"]) == 1:
				animal["photo1_small"] = row["photos"][0]["small"]
				animal["photo1_med"] = row["photos"][0]["medium"]
				animal["photo2_small"] = None
				animal["photo2_med"] = None
			animal["status"] = row["status"]
			if row["attributes"]["house_trained"] == True:
				animal["housetrained"] = 1
			if row["attributes"]["house_trained"] == False:
				animal["housetrained"] = 2
			if row["attributes"]["house_trained"] == None:
				animal["housetrained"] = 0
			if row["attributes"]["declawed"] == True:
				animal["declawed"] = 1
			if row["attributes"]["declawed"] == False:
				animal["declawed"] = 2
			if row["attributes"]["declawed"] == None:
				animal["declawed"] = 0
			if row["environment"]["children"] == True:
				animal["good_with_kids"] = 1
			if row["environment"]["children"] == False:
				animal["good_with_kids"] = 2
			if row["environment"]["children"] == None:
				animal["good_with_kids"] = 0
			if row["environment"]["cats"] == True:
				animal["good_with_cats"] = 1
			if row["environment"]["cats"] == False:
				animal["good_with_cats"] = 2
			if row["environment"]["cats"] == None:
				animal["good_with_cats"] = 0
			if row["environment"]["dogs"] == True:
				animal["good_with_dogs"]  = 1
			if row["environment"]["dogs"] == False:
				animal["good_with_dogs"]  = 2
			if row["environment"]["dogs"] == None:
				animal["good_with_dogs"]  = 0
			animal["url"] = row["url"]
 
			newAnimals.append(animal)
			print(animal)

		return newAnimals
			
 
		