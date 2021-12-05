import psycopg2
from config import config
from Session import get_session
from model.abonnementRepository import AbonnementRepository
from model.gymRepository import GymRepository
from model.simulatorRepository import SimulatorRepository
from model.visitorRepository import VisitorRepository
from view import View
from controller import Controller

connection = psycopg2.connect(
	host= config['host'],
	user= config['user'],
	password = config['password'],
	database= config['db_name'],
	port = config['port']
)

session = get_session()
connection.autocommit = True
visitorRepository = VisitorRepository(connection, session)
gymRepository = GymRepository(connection, session)
simulatorRepository = SimulatorRepository(connection, session)
abonnementRepository = AbonnementRepository(connection, session)
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