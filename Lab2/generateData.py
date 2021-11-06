from psycopg2 import Error

def generate_visitors(connection, number):
	try:
		cursor = connection.cursor()
		generate_query = """INSERT INTO visitors (firstname, lastname, age)
							SELECT 'visitor' || chr(trunc(65+random()*25)::int) ||
									chr(trunc(65+random()*25)::int) as firstname ,
									chr(trunc(65+random()*25)::int) ||
									chr(trunc(65+random()*25)::int) as lastname,
									trunc(random()*(99-5)+5)::int as age
									FROM generate_series(1,%s) """
		cursor.execute(generate_query, number)
		connection.commit()
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()

def generate_gyms(connection, number):
	try:
		cursor = connection.cursor()
		generate_query = """INSERT INTO gyms (address, area, fee)
							SELECT trunc(random()*(200-1)+1)::int || ', ' ||
							substr(md5(random()::text), 1,20) || ' Street' as address,
							trunc(random()*(20-5)+5)::int as area,
							trunc(random()*(200-50)+5)::int as fee
							FROM generate_series(1,%s)"""
		cursor.execute(generate_query, number)
		connection.commit()
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()

# def generate_simulators(connection, number):
# 	try:
# 		cursor = connection.cursor()
# 		generate_query = """INSERT INTO simulators(gym_id, model, weight)
# 							SELECT gym_id from gyms as gym_id,
# 							chr(trunc(65+random()*25)::int) || 
# 							chr(trunc(65+random()*25)::int) ||  
# 							trunc(random()*(99-1)+1)::int as model,
# 							trunc(random()*(50-20)+20)::int as weight
# 							FROM generate_series(1, %s)"""
# 		cursor.execute(generate_query, number)
# 		connection.commit()
# 	except(Exception, Error) as error:
# 		print("Error while working with database", error)
# 	finally:
# 		if connection:
# 			cursor.close()
# 			connection.close()


# generate_query = """INSERT INTO simulators(gym_id, model, weight)

# 							With id_table(gym_id) AS
# 							(
# 								SELECT gym_id from gyms
# 							),
# 							generated_data(model, weight) AS
# 							(
# 								SELECT 
# 								chr(trunc(65+random()*25)::int) || 
# 								chr(trunc(65+random()*25)::int) ||  
# 								trunc(random()*(99-1)+1)::int as model,
# 								trunc(random()*(50-20)+20)::int as weight
# 								FROM generate_series(1, %s)
# 							)

# 							SELECT generated_data.model, id_table.gym_id, 
# 							generated_data.weight from id_table,
# 							generated_data order by random() limit %s"""
