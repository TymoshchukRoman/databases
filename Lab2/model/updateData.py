class UpdateData:

	def __init__(self, connection):
		self.connection = connection

	def update_visitor(self, column, id, new_value):
		if(column == "visitor_id"):
			raise Exception("Id changing is not available")
		cursor = self.connection.cursor()
		update_query = f"""UPDATE visitors SET {column} = %s WHERE visitor_id = %s"""
		record_to_update = (new_value, id)
		cursor.execute(update_query, record_to_update)
		self.connection.commit()
		cursor.close()
		self.connection.close()

	def update_fee(self, id, new_fee):
		cursor = self.connection.cursor()
		update_query = """UPDATE gyms SET fee = %s WHERE gym_id = %s"""
		record_to_update = (new_fee, id)
		cursor.execute(update_query, record_to_update)
		self.connection.commit()
		cursor.close()
		self.connection.close()