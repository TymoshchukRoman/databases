from typing import Counter
from psycopg2 import Error

def update_visitor(connection, column, id, new_value):
	try:
		if(column == "visitor_id"):
			raise Exception("Id changing is not available")
		cursor = connection.cursor()
		update_query = f"""UPDATE visitors SET {column} = %s WHERE visitor_id = %s"""
		record_to_update = (new_value, id)
		cursor.execute(update_query, record_to_update)
		connection.commit()
		count = cursor.rowcount
		return count
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()

def update_fee(connection, id, new_fee):
	try:
		cursor = connection.cursor()
		update_query = """UPDATE gyms SET fee = %s WHERE gym_id = %s"""
		record_to_update = (new_fee, id)
		cursor.execute(update_query, record_to_update)
		connection.commit()
		count = cursor.rowcount
		return count
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()
