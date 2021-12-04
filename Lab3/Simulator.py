from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Simulator(Base):
    __tablename__ = 'simulators'
    simulator_id = Column(Integer, Sequence('simulators_simulator_id_seq', increment=1), primary_key=True)
    gym_id = Column(Integer, ForeignKey('gyms.gym_id', ondelete="CASCADE"), nullable=False)
    model = Column(String(50), nullable=False)
    weight = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Simulator(gym_id = '%s', model = '%s', weight = '%s')>" % (self.gym_id, self.model, self.weight)
