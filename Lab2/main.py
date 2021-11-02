import psycopg2
from config import host, user, password, db_name
from deleteData import delete_by_id
from insertData import insert_abonnement, insert_gym, insert_simulator, insert_visitor

try:
	#connect to database
	connection = psycopg2.connect(
		host = host,
		user = user,
		password = password,
		database = db_name
	)
	connection.autocommit = True

	#int objects does not support indexings

	# tmp = []
	# k = input()
	# tmp.append(k)
	# delete_by_id(connection, tmp, "visitors")

	# insert_visitor(connection, input(), input(), input())
	# insert_gym(connection, input(), input(), input())
	# insert_simulator(connection, input(), input(), input())
	# insert_abonnement(connection, input(), input())

except Exception as _ex:
	print("[INFO] Error while working with PosgreSQL", _ex)
finally:
	if connection:
		connection.close()
		print("[INFO] PostgreSQL connection closed")
