class DeleteData:

	def __init__(self, connection):
		self.connection = connection

	def delete_visitor(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM visitors WHERE visitor_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()
		
		cursor.close()
	
	def delete_gym(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM gyms WHERE gym_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()
		
		cursor.close()
	
	def delete_simulator(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM simulators WHERE simulator_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()

		cursor.close()

	def delete_abonnement(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM abonnements WHERE visitor_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()
		
		cursor.close()