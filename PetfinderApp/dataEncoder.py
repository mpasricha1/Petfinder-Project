import pandas as pd
from pprint import pprint

class encoder:
	def __init__(self, data):
		self.data = data 

	def parseAnimal(self):
		newAnimals = []

		for row in self.data["animals"]: 
			animal = {}
			animal = []

		