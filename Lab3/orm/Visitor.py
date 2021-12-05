from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Visitor(Base):
    __tablename__ = 'visitors'
    visitor_id = Column(Integer, Sequence('visitors_visitor_id_seq', increment=1), primary_key = True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    gyms = relationship("Abonnement", back_populates="visitor")

    def __repr__(self):
        return "<Visitor(firstname = '%s', lastname = '%s', age = '%s')>" % (self.firstname, self.lastname, self.age)