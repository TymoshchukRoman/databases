from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Abonnement(Base):
    table_title = 'abonnements'
    visitor_id = Column(Integer, ForeignKey('visitors.visitor_id', ondelete="CASCADE"), nullable=False)
    gym_id = Column(Integer, ForeignKey('gyms.gym_id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "Abonnement(visitor_id = '%s', gym_id = '%s')" % (self.visitor_id, self.gym_id)