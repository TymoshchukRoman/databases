import psycopg2
from config import config
from tmp import host, user, password, db_name
from Session import get_session
from abonnementRepository import AbonnementRepository
from visitorRepository import VisitorRepository
from gymRepository import GymRepository
from simulatorRepository import SimulatorRepository
from view import View
from controller import Controller

connection = psycopg2.connect(
	host= host,
	user= user,
	password = password,
	database= db_name
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
