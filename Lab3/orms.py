from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey


Base = declarative_base()


class Abonnement(Base):
    __tablename__ = 'abonnements'
    visitor_id = Column(Integer, ForeignKey(
        'visitors.visitor_id', ondelete="CASCADE"), nullable=False, primary_key= True)
    gym_id = Column(Integer, ForeignKey(
        'gyms.gym_id', ondelete="CASCADE"), nullable=False, primary_key= True)

    gym = relationship("Gym", back_populates = "visitors")
    visitor = relationship("Visitor", back_populates = "gyms")
    
    def __repr__(self):
        return "Abonnement(visitor_id = '%s', gym_id = '%s')" % (self.visitor_id, self.gym_id)


class Gym(Base):
    __tablename__ = 'gyms'
    gym_id = Column(Integer, Sequence(
        'gyms_gym_id_seq', increment=1), primary_key=True)
    address = Column(String(100), nullable=False)
    area = Column(Integer, nullable=False)
    fee = Column(Integer, nullable=False)

    visitors = relationship("Abonnement", back_populates="gym")

    def __repr__(self):
        return "Gym(address = '%s', area = '%s', fee = '%s')" % (self.address, self.area, self.fee)


class Visitor(Base):
    __tablename__ = 'visitors'
    visitor_id = Column(Integer, Sequence(
        'visitors_visitor_id_seq', increment=1), primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    gyms = relationship("Abonnement", back_populates = "visitor")

    def __repr__(self):
        return "Visitor(firstname = '%s', lastname = '%s', age = '%s')" % (self.firstname, self.lastname, self.age)


class Simulator(Base):
    __tablename__ = 'simulators'
    simulator_id = Column(Integer, Sequence(
        'simulators_simulator_id_seq', increment=1), primary_key=True)
    gym_id = Column(Integer, ForeignKey(
        'gyms.gym_id', ondelete="CASCADE"), nullable=False)
    model = Column(String(50), nullable=False)
    weight = Column(Integer, nullable=False)

    def __repr__(self):
        return "Simulator(gym_id = '%s', model = '%s', weight = '%s')" % (self.gym_id, self.model, self.weight)
