from psycopg2 import Error

def select_simulators_by_fee(connection, lower_fee, upper_fee):
	try:
		cursor = connection.cursor()
		select_query = """select model, area, fee from simulators s 
						full outer join gyms q on q.gym_id = s.gym_id where fee > %s and fee < %s order by fee"""
		record_to_select = (lower_fee, upper_fee)
		cursor.execute(select_query, record_to_select)
		data = cursor.fetchall()
		return data
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()

def select_visitors_with_abonnements(connection):
	try:
		cursor = connection.cursor()
		select_query = """SELECT visitors.firstname, visitors.lastname, visitors.visitor_id from 
							visitors inner join abonnements ON 
							visitors.visitor_id = abonnements.visitor_id order by firstname"""
		cursor.execute(select_query)
		data = cursor.fetchall()
		return data
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()

def select_abonnements_by_age(connection, lower_age, upper_age):
	try:
		cursor = connection.cursor()
		select_query = """select firstname, lastname, age 
						from visitors v full outer join abonnements q on q.visitor_id = v.visitor_id 
						where age < 80 and age > 60 order by age"""
		record_to_select = (lower_age, upper_age)
		cursor.execute(select_query, record_to_select)
		data = cursor.fetchall()
		return data
	except(Exception, Error) as error:
		print("Error while working with database", error)
	finally:
		if connection:
			cursor.close()
			connection.close()