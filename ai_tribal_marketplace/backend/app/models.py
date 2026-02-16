from sqlalchemy import Column, Integer, String
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    english = Column(String)
    hindi = Column(String)
    maithili = Column(String)
    konkani = Column(String)

    def __init__(self, english, hindi, maithili, konkani):
        self.english = english
        self.hindi = hindi
        self.maithili = maithili
        self.konkani = konkani
    