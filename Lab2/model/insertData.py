class InsertData:

	def __init__(self, connection):
		self.connection = connection

	def insert_visitor(self, input):	
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO visitors (firstname, lastname, age)
												VALUES (%s, %s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()
		cursor.close()
				
	def insert_gym(self, input):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO gyms (address, area, fee)
												VALUES (%s, %s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()
		cursor.close()

	def insert_simulator(self, input):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO simulators (gym_id, model, weight)
												VALUES (%s, %s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()
	
		cursor.close()

	def insert_abonnement(self, input):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO abonnements (visitor_id, gym_id)
												VALUES (%s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()
		cursor.close()