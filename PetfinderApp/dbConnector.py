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
