from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Abonnement(Base):
    __tablename__ = 'abonnements'
    visitor_id = Column(Integer, ForeignKey('visitors.visitor_id', ondelete="CASCADE"), nullable=False)
    gym_id = Column(Integer, ForeignKey('gyms.gym_id', ondelete="CASCADE"), nullable=False)

    gym = relationship("Gym", back_populates="visitors")
    visitor = relationship("Visitor", back_populates="gyms")

    def __repr__(self):
        return "<Abonnement(visitor_id = '%s', gym_id = '%s')>" % (self.visitor_id, self.gym_id)