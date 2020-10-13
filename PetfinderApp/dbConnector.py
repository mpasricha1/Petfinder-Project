from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session

class dbConnector:
	def _init__(self):
		self.engine = ""
		self.Base = ""
		self.Animal = ""
		self.Breed = ""
		self.Color = ""
		self.State = ""

	def establishConnection(self):
		self.engine = create_engine(f"postgresql+psycopg2://postgres:postgres@localhost/adoption_db")
		self.Base = automap_base()
		self.Base.prepare(self.engine,reflect=True)
		self.Animal = self.Base.classes.animal
		self.Breed = self.Base.classes.breed
		self.Color = self.Base.classes.color
		self.State = self.Base.classes.state 

		print("Connection Established")

	def breedsList(self):
		session = Session(self.engine)
		breeds = session.query(self.Breed.breed_id, self.Breed.breed_name).all()
		session.close()
		
		return breeds

	def colorsList(self):
		session = Session(self.engine)
		colors = session.query(self.Color.color_code, self.Color.color_name).all()
		session.close()
		
		return colors

	def statesList(self):
		session = Session(self.engine)
		states = session.query(self.State.state_id, self.State.state_name)
		session.close()

		return states

	def getPageCount(self, animalType, status):
		if animalType == "dog": 
			animalType = 1
		else: 
			animalType = 2
		session = Session(self.engine)
		pageCount = session.query(self.Animal.page).\
							filter(self.Animal.type == animalType).\
							filter(self.Animal.status == status).\
							order_by(self.Animal.id.desc()).first()
		pageCount = pageCount[0]+1
		return pageCount

	def insertNewData(self,data):
		session = Session(self.engine)

		lastId = session.query(self.Animal.id).\
					order_by(self.Animal.id.desc()).first()
		newId = lastId[0]+1
		
		for row in data:
			newAnimalData = self.Animal(id=newId,type=row["type"], name=row["name"], age=row["age"], breed1=row["breed1"], breed2=row["breed2"],
								   gender=row["gender"], color1=row["color1"], color2=row["color2"], color3=row["color3"], 
								   maturity_size=row["maturity_size"], furlength=row["furlength"], vaccinated=row["vaccinated"],
								   dewormed=row["dewormed"], sterilized=row["sterilized"], health=row["health"], quantity=row["quantity"], 
								   fee=row["fee"], state_name=row["state_name"], rescuer_id=row["rescuer_id"], video_amt=row["video_amt"],
								   description=row["description"], pet_id=row["pet_id"], photo_amt=row["photo_amt"], adoption_speed=row["adoption_speed"], 
								   test_train=row["test_train"],photo1_small=row["photo1_small"], photo1_med=row["photo1_med"],
								   photo2_small=row["photo2_small"], photo2_med=row["photo2_med"], status=row["status"], 
								   housetrained=row["housetrained"], declawed=row["declawed"], good_with_kids=row["good_with_kids"],
								   good_with_cats=row["good_with_cats"], good_with_dogs=row["good_with_dogs"], url=row["url"], page=row["page"]
								)
			session.add(newAnimalData)
			session.commit()
			newId+=1

	def getTrainData(self):
		session = Session(self.engine)

		sel = [self.Animal.type, self.Animal.age, self.Animal.breed1, self.Animal.breed2, self.Animal.gender, self.Animal.color1,
			   self.Animal.color2, self.Animal.color3, self.Animal.maturity_size, self.Animal.furlength, self.Animal.vaccinated, 
			   self.Animal.dewormed, self.Animal.sterilized, self.Animal.health, self.Animal.fee, self.Animal.adoption_speed ]

		trainData = session.query(*sel).\
				filter(self.Animal.test_train == 'train').\
				filter(self.Animal.page == None).all()

		session.close()
		return trainData

	def getTestData(self):
		session = Session(self.engine)

		sel = [self.Animal.type, self.Animal.age, self.Animal.breed1, self.Animal.breed2, self.Animal.gender, self.Animal.color1,
			   self.Animal.color2, self.Animal.color3, self.Animal.maturity_size, self.Animal.furlength, self.Animal.vaccinated, 
			   self.Animal.dewormed, self.Animal.sterilized, self.Animal.health, self.Animal.fee, self.Animal.adoption_speed ]
		testData = session.query(*sel).\
						filter(self.Animal.test_train == 'test').\
						filter(self.Animal.adoption_speed == None).all()
		return testData

	def getAnalysisData(self):
		session = Session(self.engine)

		sel = [self.Breed.breed_name, self.Animal.age, self.Animal.adoption_speed, self.Animal.photo_amt, 
			    self.Animal.fee, self.Animal.maturity_size, self.Animal.type, self.Animal.furlength, self.Animal.gender ]

		animalStatsData = session.query(*sel).\
								 filter(self.Animal.breed1 == self.Breed.breed_id).\
								 filter(self.Animal.test_train == "train").\
								 filter(self.Animal.page == None).all()

		return animalStatsData



