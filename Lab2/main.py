import psycopg2
from config import host, user, password, db_name
from deleteData import delete_visitor_by_id

try:
	#connect to database
	connection = psycopg2.connect(
		host = host,
		user = user,
		password = password,
		database = db_name
	)
	connection.autocommit = True

	k = input()

	delete_visitor_by_id(connection, k)

except Exception as _ex:
	print("[INFO] Error while working with PosgreSQL", _ex)
finally:
	if connection:
		connection.close()
		print("[INFO] PostgreSQL connection closed")