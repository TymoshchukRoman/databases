import psycopg2
from config import host, user, password, db_name
from model.visitorRepository import VisitorRepository
from model.gymRepository import GymRepository
from model.simulatorRepository import SimulatorRepository
from model.abonnementRepository import AbonnementRepository
from view import View
from controller import Controller

connection = psycopg2.connect(
	host = host,
	user = user,
	password = password,
	database = db_name
)
connection.autocommit = True

visitorRepository = VisitorRepository(connection)
gymRepository = GymRepository(connection)
simulatorRepository = SimulatorRepository(connection)
abonnementRepository = AbonnementRepository(connection)
view = View()

controller = Controller(abonnementRepository, gymRepository, simulatorRepository, visitorRepository, view)

while(True):
	command = input('Enter command \n')
	if command == 'exit':
		break
	try:
		controller.handleCommand(command)
		print(f"Command '{command}' executed")
	except Exception as ex:
		print(ex)
