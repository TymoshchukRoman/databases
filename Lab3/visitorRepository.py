from orms import Visitor

class VisitorRepository:
	
	def __init__(self, connection, session):
		self.connection = connection
		self.session = session
	
	def delete_visitor(self, id):
		self.session.delete(self.session.query(Visitor).get(id))
		self.session.commit()
	
	def insert_visitor(self, input):
		newVisitor = Visitor(firstname=input[0], lastname=input[1], age=input[2])
		self.session.add(newVisitor)
		self.session.commit()
	
	def update_lastname(self, input):
		newData = self.session.query(Visitor).get(input[1])
		newData.lastname = input[1]
		self.session.commit()

	def generate_visitors(self, number):
		cursor = self.connection.cursor()
		generate_query = """INSERT INTO visitors (firstname, lastname, age)
							SELECT 'visitor' || chr(trunc(65+random()*25)::int) ||
									chr(trunc(65+random()*25)::int) as firstname ,
									chr(trunc(65+random()*25)::int) ||
									chr(trunc(65+random()*25)::int) as lastname,
									trunc(random()*(99-5)+5)::int as age
									FROM generate_series(1,%s) """
		cursor.execute(generate_query, number)
		self.connection.commit()
		cursor.close()
	
	def select_visitors_with_abonnements(self,data):
		cursor = self.connection.cursor()
		select_query = """SELECT visitors.firstname, visitors.lastname, visitors.visitor_id from 
							visitors inner join abonnements ON 
							visitors.visitor_id = abonnements.visitor_id where visitors.visitor_id > %s order by firstname"""
		cursor.execute(select_query, data)
		data = cursor.fetchall()
		cursor.close()

		return data
	
	def select_abonnements_by_age(self, input):
		cursor = self.connection.cursor()
		select_query = """select firstname, lastname, age 
						from visitors v full outer join abonnements q on q.visitor_id = v.visitor_id 
						where age > %s and age < %s order by age"""
		cursor.execute(select_query, input)
		data = cursor.fetchall()
		cursor.close()

		return data
