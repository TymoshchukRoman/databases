from psycopg2 import Error

def insert_visitor(connection, first_name, last_name, age):
	try:
		cursor = connection.cursor()
		insert_query = """INSERT INTO visitors (firstname, lastname, age)
												VALUES (%s, %s, %s)"""
		record_to_insert = (first_name, last_name, age)
		cursor.execute(insert_query, record_to_insert)

		connection.commit()
		count = cursor.rowcount
		print(count)
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()
			print("Connection closed")


def insert_gym(connection, address, area, fee):
	try:
		cursor = connection.cursor()
		insert_query = """INSERT INTO gyms (address, area, fee)
												VALUES (%s, %s, %s)"""
		record_to_insert = (address, area, fee)
		cursor.execute(insert_query, record_to_insert)
		connection.commit()
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()


def insert_simulator(connection, gym_id, model, weight):
	try:
		cursor = connection.cursor()
		insert_query = """INSERT INTO simulators (gym_id, model, weight)
												VALUES (%s, %s, %s)"""
		record_to_insert = (gym_id, model, weight)
		cursor.execute(insert_query, record_to_insert)
		connection.commit()
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()


def insert_abonnement(connection, visitor_id, gym_id):
	try:
		cursor = connection.cursor()
		insert_query = """INSERT INTO abonnements (visitor_id, gym_id)
												VALUES (%s, %s)"""
		record_to_insert = (visitor_id, gym_id)
		cursor.execute(insert_query, record_to_insert)
		connection.commit()
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()