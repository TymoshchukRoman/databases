import psycopg2
from config import host, user, password, db_name
from model.deleteData import DeleteData
from model.executeQuery import ExecuteQuery
from model.generateData import GenerateData
from model.insertData import InsertData
from model.updateData import UpdateData
from view import View
from controller import Controller

connection = psycopg2.connect(
	host = host,
	user = user,
	password = password,
	database = db_name
)
connection.autocommit = True

deleteData = DeleteData(connection)
executeQuery = ExecuteQuery(connection)
insertData = InsertData(connection)
updateData = UpdateData(connection)
generateData = GenerateData(connection)
view = View()

controller = Controller(deleteData, executeQuery, generateData, insertData, updateData, view)

while(True):
	command = input('Enter command \n')
	if command == 'exit':
		break
	try:
		controller.handleCommand(command)
		print(f"Command '{command}' executed")
	except Exception as ex:
		print(ex)