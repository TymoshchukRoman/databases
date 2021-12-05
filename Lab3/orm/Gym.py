from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Gym(Base):
    __tablename__ = 'gyms'
    gym_id = Column(Integer, Sequence('gyms_gym_id_seq', increment=1), primary_key=True)
    address = Column(String(100), nullable=False)
    area = Column(Integer, nullable=False)
    fee = Column(Integer, nullable=False)

    visitors = relationship("Abonnement", back_populates="gym")

    def __repr__(self):
        return "<Gym(address = '%s', area = '%s', fee = '%s')>" % (self.address, self.area, self.fee)