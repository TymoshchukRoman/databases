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
