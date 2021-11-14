class SimulatorRepository:
	def __init__(self, connection):
		self.connection = connection
	
	def delete_simulator(self, id):
		cursor = self.connection.cursor()
		delete_query = """DELETE FROM simulators WHERE simulator_id = %s"""
		cursor.execute(delete_query, id)
		self.connection.commit()

		cursor.close()
	
	def insert_simulator(self, input):
		cursor = self.connection.cursor()
		insert_query = """INSERT INTO simulators (gym_id, model, weight)
												VALUES (%s, %s, %s)"""
		cursor.execute(insert_query, input)
		self.connection.commit()

		cursor.close()

	def generate_simulators(self, number):
		cursor = self.connection.cursor()
		cursor.execute("SELECT gyms.gym_id from gyms ORDER BY random() LIMIT 1")
		a = cursor.fetchone()
		generate_query = f"""INSERT INTO simulators (gym_id, model, weight)
		
							SELECT {a[0]} as gym_id ,
							chr(trunc(65+random()*25)::int) ||
							chr(trunc(65+random()*25)::int) ||
							trunc(random()*(100-1)+1)::int as model,
							trunc(random()*(50-10)+10)::int as weight
							FROM generate_series(1, %s) """
		cursor.execute(generate_query, number)
		self.connection.commit()
		cursor.close()

	def select_simulators_by_fee(self, input):
		cursor = self.connection.cursor()
		select_query = """select model, area, fee from simulators s 
						full outer join gyms q on q.gym_id = s.gym_id where fee > %s and fee < %s order by fee"""
		cursor.execute(select_query, input)
		data = cursor.fetchall()
		cursor.close()

		return data