import  executeCommands
import time
class Controller:
	def __init__(self, deleteData, executeQuery, generateData, insertData, updateData, view) :
		self.deleteData = deleteData
		self.executeQuery = executeQuery
		self.generateData = generateData
		self.insertData = insertData
		self.updateData = updateData
		self.view = view
		self.command = {}
		self.command["deleteVisitor"] = self.deleteData.delete_visitor
		self.command["deleteGym"] = self.deleteData.delete_gym
		self.command["deleteSimulator"] = self.deleteData.delete_simulator
		self.command["deleteAbonnement"] = self.deleteData.delete_abonnement
		self.command["printSimulatorsByFee"] = executeQuery.select_simulators_by_fee
		self.command["printVisitorsWithAbs"] = executeQuery.select_visitors_with_abonnements
		self.command["printAbonnementsByAge"] = executeQuery.select_abonnements_by_age
		self.command["generateVisitors"] = generateData.generate_visitors
		self.command["generateGyms"] = generateData.generate_gyms
		self.command["generateSimulators"] = generateData.generate_simulators
		self.command["updateLastname"] = updateData.update_lastname
		self.command["updateFee"] = updateData.update_fee
		self.command["insertVisitor"] = insertData.insert_visitor
		self.command["insertGym"] = insertData.insert_gym
		self.command["insertSimulator"] = insertData.insert_simulator
		self.command["insertAbonnement"] = insertData.insert_abonnement

	def handleCommand(self, command):
		commands = ["deleteVisitor", "deleteGym", "deleteSimulator", "deleteAbonnement",
				"printSimulatorsByFee", "printVisitorsWithAbs", "printAbonnementsByAge",
				"generateVisitors", "generateGyms", "generateSimulators", "updateLastname",
				"updateFee", "insertVisitor", "insertGym", "insertSimulator", "insertAbonnement"]
		commandName = command.split(' ')[0]
		if commandName not in commands:
			raise Exception("Entered command does not exist")
		
		commandData = executeCommands.get_command_args(command)

		if commandName in ["printSimulatorsByFee", "printAbonnementsByAge"]:
			start = time.time()
			fetched_data = self.command[commandName](commandData)
			end = time.time()
			print(f"The request was performed in {int((end - start)*1000)} ms")
			self.view.get_table_of_data(fetched_data)
		elif (commandName == "printVisitorsWithAbs"):
			start = time.time()
			fetched_data = self.command[commandName]
			end = time.time()
			print(f"The request was performed in {int((end - start)*1000)} ms")
			self.view.get_table_of_data(fetched_data)
		else:
			self.command[commandName](commandData)
