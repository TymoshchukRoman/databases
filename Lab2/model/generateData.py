class GenerateData:

	def __init__(self, connection):
		self.connection = connection

	def generate_visitors(self, number):
		cursor = self.connection.cursor()
		generate_query = """INSERT INTO visitors (firstname, lastname, age)
							SELECT 'visitor' || chr(trunc(65+random()*25)::int) ||
									chr(trunc(65+random()*25)::int) as firstname ,
									chr(trunc(65+random()*25)::int) ||
									chr(trunc(65+random()*25)::int) as lastname,
									trunc(random()*(99-5)+5)::int as age
									FROM generate_series(1,%s) """
		cursor.execute(generate_query, number)
		self.connection.commit()
		cursor.close()
		self.connection.close()

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
		self.connection.close()

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
		self.connection.close()