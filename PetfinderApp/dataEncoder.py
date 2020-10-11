import pandas as pd
from pprint import pprint

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
			#Kristin taking care of
			#animal["age"]
			if row["size"].lower() == "small" or row["size"].lower() == "medium":
				if row["age"].lower() == "baby": 
					animal["age"] == 12
				if row["age"].lower() == "young": 
					animal["age"] == 3 * 12
				if row["age"].lower() == "adult": 
					animal["age"] == 6 * 12
				if row["age"].lower() == "senior": 
					animal["age"] == 10 * 12
			elif row["size"].lower() == "large" or row["size"].lower() == "xlarge":
			 	if row["age"].lower() == "baby":
			 		animal["age"] == 18
			 	elif row["age"].lower() == "young":
			 		animal["age"] == 4 * 12
			 	elif row["age"].lower() == "adult":
			 		animal["age"] == 7 * 12
			 	elif row["age"].lower() == "senior":
			 		animal["age"] == 12 * 12
			else: 
				animal["age"] == 0
			for breed in breeds:
				if row["breeds"]["primary"] == None:
					animal["breed1"] = 0
				else:
					if row["breeds"]["primary"] == breed.breed_name: 
						animal["breed1"] = breed.breed_id
				if row["breeds"]["secondary"] == None:
					animal["breed2"] = 0
				else:
					if row["breeds"]["secondary"] == breed.breed_name:
						animal["breed2"] = breed.breed_id
			if row["gender"].lower() == "Male":
				animal["gender"] = 1 
			else: 
				animal["gender"] = 2
			for color in colors: 
				if row["colors"]["primary"] == None:
					animal["colors1"] = 0
				else:
					if row["colors"]["primary"] == color.color_name:
						animal["color1"] = color.color_code
				if row["colors"]["secondary"] == None:
					animal["color2"] = 0
				else:
					if row["colors"]["secondary"] == color.color_name:
						animal["color2"] = color.color_code
				if row["colors"]["tertiary"] == None:
					animal["color3"] = 0
				else:
					if row["colors"]["tertiary"] == color.color_name:
						animal["color3"] = color.color_code
			if row["size"] == None:
				animal["maturitySize"] = 0
			else:
				if row["size"] == None:
					animal["maturitySize"] = 0
				else:
					if row["size"].lower() == "small": 
						animal["maturitySize"] = 1
					elif row["size"].lower() == "medium":
						animal["maturitySize"] = 2 
					elif row["size"].lower() == "large": 
							animal["maturitySize"] = 3
					elif row["size"].lower() == "xlarge": 
						animal["maturitySize"] = 4
			if row["coat"] == None: 
				animal["furLength"] = 0
			else:
				if row["coat"].lower() == "short":
					animal["furLength"] = 1 
				elif row["coat"].lower() == "medium": 
					animal["furLength"] = 2
				elif row["coat"].lower() == "long": 
					animal["furLength"] = 3 
				elif row["coat"].lower() == "wire":
					animal["furLength"] = 4
				elif row["coat"].lower() == "hairless": 
					animal["furLength"] = 5
			if row["attributes"]["shots_current"] == True:
				animal["vaccinated"] = 1
			if row["attributes"]["shots_current"] == False:
				animal["vaccinated"] = 2
			if row["attributes"]["shots_current"] == None:
				animal["vaccinated"] = 3
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
			animal["fee"] = 0
			for state in states: 
				if row["contact"]["address"]["state"] == state.state_name: 
						animal["state"] = state.state_id
			animal["orgId"] = row["organization_id"]
			animal["videoAmt"] = len(row["videos"])
			animal["description"] = row["description"]
			animal["petid"] = row["id"]
			animal["photoAmnt"] = len(row["photos"])
			animal["testTrain"] = "train"
			if len(row["photos"]) > 1:
				animal["photo1small"] = row["photos"][0]["small"]
				animal["photo1medium"] = row["photos"][0]["medium"]
				animal["photo2small"] = row["photos"][1]["small"]
				animal["photo2medium"] = row["photos"][1]["medium"]
			elif len(row["photos"]) == 1:
				animal["photo1small"] = row["photos"][0]["small"]
				animal["photo1medium"] = row["photos"][0]["medium"]
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
				animal["goodwithkids"] = 1
			if row["environment"]["children"] == False:
				animal["goodwithkids"] = 2
			if row["environment"]["children"] == None:
				animal["goodwithkids"] = 0
			if row["environment"]["cats"] == True:
				animal["goodwithcats"] = 1
			if row["environment"]["cats"] == False:
				animal["goodwithcats"] = 2
			if row["environment"]["cats"] == None:
				animal["goodwithcats"] = 0
			if row["environment"]["dogs"] == True:
				animal["goodwithdogs"]  = 1
			if row["environment"]["dogs"] == False:
				animal["goodwithdogs"]  = 2
			if row["environment"]["dogs"] == None:
				animal["goodwithdogs"]  = 0
			animal["url"] = row["url"]
 
			print(animal)
			
 
		