class ExecuteQuery:

	def __init__(self, connection):
		self.connection = connection

	def select_simulators_by_fee(self, lower_fee, upper_fee):
		cursor = self.connection.cursor()
		select_query = """select model, area, fee from simulators s 
						full outer join gyms q on q.gym_id = s.gym_id where fee > %s and fee < %s order by fee"""
		record_to_select = (lower_fee, upper_fee)
		cursor.execute(select_query, record_to_select)
		data = cursor.fetchall()
		cursor.close()
		self.connection.close()

		return data
	
	def select_visitors_with_abonnements(self):
		cursor = self.connection.cursor()
		select_query = """SELECT visitors.firstname, visitors.lastname, visitors.visitor_id from 
							visitors inner join abonnements ON 
							visitors.visitor_id = abonnements.visitor_id order by firstname"""
		cursor.execute(select_query)
		data = cursor.fetchall()
		cursor.close()
		self.connection.close()

		return data
				

	def select_abonnements_by_age(self, lower_age, upper_age):
		cursor = self.connection.cursor()
		select_query = """select firstname, lastname, age 
						from visitors v full outer join abonnements q on q.visitor_id = v.visitor_id 
						where age < 80 and age > 60 order by age"""
		record_to_select = (lower_age, upper_age)
		cursor.execute(select_query, record_to_select)
		data = cursor.fetchall()
		cursor.close()
		self.connection.close()

		return data