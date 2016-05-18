
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer

Base = declarative_base()

class PlaybookLocation(Base):
	__tablename__ = 'PLAYBOOK_LOCATION'
	id = Column(Integer, primary_key=True)
	playbooktype = Column(String(40))
	environment = Column(String(80))
	location = Column(String(180))

	def __init__(self, environment, location):
		Base.__init__(self)
		self.environment = environment
		self.location = location

