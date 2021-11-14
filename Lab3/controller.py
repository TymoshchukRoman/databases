import  executeCommands
import time
import view
class Controller:
	def __init__(self, abonnementRepository, gymRepository, simulatorRepository, visitorRepository, view) :
		self.abonnementRepository = abonnementRepository
		self.gymRepository = gymRepository
		self.simulatorRepository = simulatorRepository
		self.visitorRepository = visitorRepository
		self.view = view
		self.command = {}
		self.command["deleteVisitor"] = self. visitorRepository.delete_visitor
		self.command["deleteGym"] = self.gymRepository.delete_gym
		self.command["deleteSimulator"] = self.simulatorRepository.delete_simulator
		self.command["deleteAbonnement"] = self.abonnementRepository.delete_abonnement
		self.command["printSimulatorsByFee"] = self.simulatorRepository.select_simulators_by_fee 
		self.command["printVisitorsWithAbs"] = self.visitorRepository.select_visitors_with_abonnements
		self.command["printAbonnementsByAge"] = self.visitorRepository.select_abonnements_by_age
		self.command["generateVisitors"] = self.visitorRepository.generate_visitors
		self.command["generateGyms"] = self.gymRepository.generate_gyms
		self.command["generateSimulators"] = self.simulatorRepository.generate_simulators
		self.command["updateLastname"] = self.visitorRepository.update_lastname
		self.command["updateFee"] = self.gymRepository.update_fee
		self.command["insertVisitor"] = self.visitorRepository.insert_visitor
		self.command["insertGym"] = self. gymRepository.insert_gym
		self.command["insertSimulator"] = self.simulatorRepository.insert_simulator
		self.command["insertAbonnement"] = self.abonnementRepository.insert_abonnement

	def handleCommand(self, command):
		commands = ["deleteVisitor", "deleteGym", "deleteSimulator", "deleteAbonnement",
				"printSimulatorsByFee", "printVisitorsWithAbs", "printAbonnementsByAge",
				"generateVisitors", "generateGyms", "generateSimulators", "updateLastname",
				"updateFee", "insertVisitor", "insertGym", "insertSimulator", "insertAbonnement"]
		commandName = command.split(' ')[0]
		if commandName not in commands:
			raise Exception("Entered command does not exist")
		
		commandData = executeCommands.get_command_args(command)

		if commandName in ["printSimulatorsByFee", "printAbonnementsByAge", "printVisitorsWithAbs"]:
			start = time.time()
			fetched_data = self.command[commandName](commandData)
			end = time.time()
			self.view.print_table_of_data(fetched_data)
			print(f"The request was performed in {int((end - start)*1000)} ms")
		else:
			self.command[commandName](commandData)
