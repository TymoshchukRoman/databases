class AbonnementRepository:
	def __init__(self, connection):
		self.connection = connection

	def delete_abonnement(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM abonnements WHERE visitor_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()

		cursor.close()
	
	def insert_abonnement(self, input):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO abonnements (visitor_id, gym_id)
												VALUES (%s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()
		cursor.close()