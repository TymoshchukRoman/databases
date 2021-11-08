class InsertData:

	def __init__(self, connection):
		self.connection = connection

	def insert_visitor(self, first_name, last_name, age):	
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO visitors (firstname, lastname, age)
												VALUES (%s, %s, %s)"""
		record_to_insert = (first_name, last_name, age)
		cursor.execute(insert_query, record_to_insert)
		self.connection.commit()
		cursor.close()
		self.connection.close()
				
	def insert_gym(self, address, area, fee):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO gyms (address, area, fee)
												VALUES (%s, %s, %s)"""
		record_to_insert = (address, area, fee)
		cursor.execute(insert_query, record_to_insert)
		self.connection.commit()
		cursor.close()
		self.connection.close()

	def insert_simulator(self, gym_id, model, weight):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO simulators (gym_id, model, weight)
												VALUES (%s, %s, %s)"""
		record_to_insert = (gym_id, model, weight)
		cursor.execute(insert_query, record_to_insert)
		self.connection.commit()
	
		cursor.close()
		self.connection.close()

	def insert_abonnement(self, visitor_id, gym_id):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO abonnements (visitor_id, gym_id)
												VALUES (%s, %s)"""
		record_to_insert = (visitor_id, gym_id)
		cursor.execute(insert_query, record_to_insert)
		self.connection.commit()
		cursor.close()
		self.connection.close()