from sqlalchemy import Column, Integer, String
from app.database.session import Base

class PLace(Base):
    __tablename__ = "place"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    image = Column(String)