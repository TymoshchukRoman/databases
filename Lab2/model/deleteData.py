class DeleteData:

	def __init__(self, connection):
		self.connection = connection

	def delete_by_id(self, id, table):
		cursor = self.connection.cursor()
		delete_query = f"""DELETE FROM {table} WHERE visitor_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()
		
		cursor.close()
		self.connection.close()