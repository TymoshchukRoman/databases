class GymRepository:
	def __init__(self, connection):
		self.connection = connection

	def delete_gym(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM gyms WHERE gym_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()

		cursor.close()
	
	def insert_gym(self, input):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO gyms (address, area, fee)
												VALUES (%s, %s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()
		cursor.close()

	def update_fee(self, input):
		cursor = self.connection.cursor()
		update_query = """UPDATE gyms SET fee = %s WHERE gym_id = %s"""
		cursor.execute(update_query, input)
		self.connection.commit()
		cursor.close()
	
	def generate_gyms(self, number):
		cursor = self.connection.cursor()
		generate_query = """INSERT INTO gyms (address, area, fee)
							SELECT trunc(random()*(200-1)+1)::int || ', ' ||
							substr(md5(random()::text), 1,20) || ' Street' as address,
							trunc(random()*(20-5)+5)::int as area,
							trunc(random()*(200-50)+5)::int as fee
							FROM generate_series(1,%s)"""
		cursor.execute(generate_query, number)
		self.connection.commit()
		cursor.close()