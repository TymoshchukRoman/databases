from psycopg2 import Error

def delete_by_id(connection, id, table):
	try:
		cursor = connection.cursor()
		delete_query = f"""DELETE FROM {table} WHERE visitor_id = %s"""
		cursor.execute(delete_query, id)
		connection.commit()
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:	
		if connection:
			cursor.close()
			connection.close()
			print("Connection closed")