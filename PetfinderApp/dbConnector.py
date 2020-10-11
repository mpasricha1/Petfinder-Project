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

	def insertNewTrainData(self,data):
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
								   description=row["description"], pet_id=row["pet_id"], adoption_speed=row["adoption_speed"], 
								   test_train=row["test_train"],photo1_small=row["photo1_small"], photo1_med=row["photo1_med"],
								   photo2_small=row["photo2_small"], photo2_med=row["photo2_med"], status=row["status"], 
								   housetrained=row["housetrained"], declawed=row["declawed"], good_with_kids=row["good_with_kids"],
								   good_with_cats=row["good_with_cats"], good_with_dogs=row["good_with_dogs"], url=row["url"]
								)
			session.add(newAnimalData)
			session.commit()
			newId+=1

		# newUserData = UserData(firstname=fName,lastname=lName,zipcode=zipcode, email=email, gender=gender,age=age,
		# 						   income=income, favregion=region,favsport=sport,favalcohol=alcohol,fitness=fit, 
		# 						   marijuanamedical=maryMed, marijuanarec=maryRec, unihealthcare=healthcare, hoursworked=hoursworked, 
		# 						   gdppercap=gdppercapita, socialenv=social, lifechoices=lifechoices,generosity=generosity, govtrust=govTrust)
		# 	session.add(newUserData)
		# 	session.commit()
