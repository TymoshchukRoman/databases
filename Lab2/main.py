import psycopg2
import math
import random
from config import host, user, password, db_name
from deleteData import delete_by_id
from executeQuery import select_abonnements_by_age, select_simulators_by_fee, select_visitors_with_abonnements
from generateData import generate_gyms, generate_visitors, generate_simulators
from insertData import insert_abonnement, insert_gym, insert_simulator, insert_visitor
from updateData import update_fee, update_visitor

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


	# a = update_visitor(connection, "lastname", input(), "Druz")
	# print(a)
	# b = update_fee(connection, 1, 85)
	# generate_visitors(connection, [input(),])
	# generate_simulators(connection, [input(),])

	# select_visitors_with_abonnements(connection)
	# select_simulators_by_fee(connection, 60, 100)

	# select_abonnements_by_age(connection, 60, 80)

	# a = [1,2,3,4,5,6]
	# b = math.trunc(a[random.choice([0,1,2,3,4,5])])
	# print(b)
	# print(test(connection))

except Exception as _ex:
	print("[INFO] Error while working with PosgreSQL", _ex)
finally:
	if connection:
		connection.close()
		print("[INFO] PostgreSQL connection closed")
