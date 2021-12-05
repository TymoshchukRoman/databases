from orms import Abonnement

class AbonnementRepository:
	def __init__(self, connection, session):
		self.connection = connection
		self.session = session

	def delete_abonnement(self, id):
		self.session.delete(self.session.query(Abonnement).get(id))
		self.session.commit()
	
	def insert_abonnement(self, input):
		newAbonnement = Abonnement(visitor_id = input[0], gym_id = input[1])
		self.session.add(newAbonnement)
		self.session.commit()
