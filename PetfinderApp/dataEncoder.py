import pandas as pd
from pprint import pprint

class encoder:
	def __init__(self, data):
		self.data = data 

	def parseAnimal(self,breeds, colors):
		newAnimals = []


		for row in self.data["animals"]: 
			print(row["type"][1])
			animal = {}
			
			if row["type"] == "Dog":
				animal["type"] = 1
			else: 
				animal["type"] = 2
			animal["name"] = row["name"]
			#animal["age"]
			for breed in breeds:
				if row["breeds"]["primary"] == breed.breed_name: 
					animal["breed1"] = breed.breed_id
				if row["breeds"]["secondary"] == breed.breed_name:
					animal["breed2"] = breed.breed_id
			for color in colors: 
				if row["colors"]["primary"] == color.color_name:
					animal["color1"] = color.color_id
				if row["colors"]["secondary"] == color.color_name:
					animal["color2"] = color.color_id
				if row["colors"]["tertiary"] == color.color_name:
					animal["color1"] = color.color_id
			if row["size"] == None:
				animal["maturitySize"] = 0
			else:
				if row["size"].lower() == "small": 
					animal["maturitySize"] = 1
				if row["size"].lower() == "medium":
					animal["maturitySize"] = 2 
				if row["size"].lower() == "large": 
						animal["maturitySize"] = 3
				if row["size"].lower() == "xlarge": 
					animal["maturitySize"] = 4
			if row["coat"] == None: 
				animal["furLength"] = 0
			else:
				if row["coat"].lower() == "short":
					animal["furLength"] = 1 
				if row["coat"].lower() == "medium": 
					animal["furLength"] = 2
				if row["coat"].lower() == "long": 
					animal["furLength"] = 3 
				if row["coat"].lower() == "wire":
					animal["furLength"] = 4
				if row["coat"].lower() == "hairless": 
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
			#animal["health"]
			animal["fee"] = 0
			#animal["state"]
			animal["orgId"] = row["organization_id"]
			animal["videoAmt"] = len(row["videos"])
			animal["description"] = row["description"]
			animal["petid"] = row["id"]
			animal["photoAmnt"] = len(row["photos"])

			print(animal)
			
 
		