from orms import Gym

class GymRepository:
	def __init__(self, connection, session):
		self.connection = connection
		self.session = session

	def delete_gym(self, id):
		self.session.delete(self.session.query(Gym).get(id))
		self.session.commit()
	
	def insert_gym(self, input):
		newGym = Gym(address = input[0], area = input[1], fee = input[2])
		self.session.add(newGym)
		self.session.commit()

	def update_fee(self, input):
		newData = self.session.query(Gym).get(input[1])
		newData.fee = input[1]
		self.session.commit()
	
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