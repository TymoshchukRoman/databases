class UpdateData:

	def __init__(self, connection):
		self.connection = connection

	def update_lastname(self, input):
		cursor = self.connection.cursor()
		update_query = f"""UPDATE visitors SET lastname = %s WHERE visitor_id = %s"""
		cursor.execute(update_query, input)
		self.connection.commit()
		cursor.close()

	def update_fee(self, input):
		cursor = self.connection.cursor()
		update_query = """UPDATE gyms SET fee = %s WHERE gym_id = %s"""
		cursor.execute(update_query, input)
		self.connection.commit()
		cursor.close()