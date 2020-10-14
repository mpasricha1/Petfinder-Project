import numpy as np 
import pandas as pd
import tensorflow
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


class petfinderNeuralNetwork:
	def __init__(self, data):
		self.data = data
		model = ''

	def trainNetwork(self,trainType): 
		df = pd.DataFrame(self.data)

		df = df.dropna(axis="columns", how="all")
		df.dropna()

		if trainType == True:
			X = df[["type", "age", "breed1", "breed2", "gender", "color1",
			      "color2", "color3", "maturity_size", "furlength", "vaccinated", 
			      "dewormed", "sterilized", "health", "fee"]]
		else:
			X = df[["type", "age", "breed1", "breed2", "gender", "color1",
		      "color2", "color3", "maturity_size", "furlength", "vaccinated", 
		      "dewormed", "sterilized", "health", "fee", "housetrained", 
		      "declawed", "good_with_kids", "good_with_cats", "good_with_dogs"]]
		y = df[["adoption_speed"]]

		X_scaler = MinMaxScaler().fit(X)
		X_train_scaled = X_scaler.transform(X)
		                                   
		y_train_categorical = to_categorical(y)

		self.model = Sequential() 

		self.model.add(Dense(units=200, activation='relu', input_dim=15))
		self.model.add(Dense(units=200, activation="relu"))
		self.model.add(Dense(units=200, activation="relu"))
		self.model.add(Dense(units=200, activation="relu"))
		self.model.add(Dense(units=5, activation="softmax"))


		self.model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

		self.model.fit(X_train_scaled, y_train_categorical, epochs=1, shuffle=True, verbose=2)

	def predict(self, predictData, dfType, predictType):
		if dfType == True:
			df = pd.DataFrame(predictData,  index=[0])
		else:
			df = pd.DataFrame(predictData)

		if predictType == True:
			X = df[["type", "age", "breed1", "breed2", "gender", "color1",
			      "color2", "color3", "maturity_size", "furlength", "vaccinated", 
			      "dewormed", "sterilized", "health", "fee"]]
		else:
			X = df[["type", "age", "breed1", "breed2", "gender", "color1",
		      "color2", "color3", "maturity_size", "furlength", "vaccinated", 
		      "dewormed", "sterilized", "health", "fee", "house_trained", 
		      "declawed", "good_with_kids", "good_with_cats", "good_with_dogs"]]

		X_scaler = MinMaxScaler().fit(X)
		X_test_scaled = X_scaler.transform(X)

		returnData = self.model.predict(X_test_scaled)

		return returnData