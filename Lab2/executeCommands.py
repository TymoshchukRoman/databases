def get_command_args(command):
	if command.startswith('updateFee') or command.startswith('updateLastname'):
		return get_update_data(command)
	if command.startswith('delete') or command.startswith('generate'):
		return get_number(command)
	if command.startswith('insertVisitor') or command.startswith('insertGym') or command.startswith('insertSimulator'):
		return get_insert_data(command)
	if command.startswith('insertAbonnement'):
		return get_abonnement_data(command)
	if command.startswith('printSimulatorsByFee'):
		return get_fee_query_data(command)
	if command.startswith('printAbonnementsByAge'):
		return get_age_query_data(command)

def get_number(command):
	data = command.split(' ')
	if len(data) != 2:
		raise Exception("Incorrect number of arguments entered")
	id = data[1]
	return (id, )

def get_update_data(command):
	data = command.split(' ')
	if len(data) != 3:
		raise Exception("Incorrect number of arguments entered")
	id = data[2]
	return(data[1], id,)

def get_visitor_data(command):
	data = command.split(' ')
	if len(data) != 4:
		raise Exception("Incorrect number of arguments entered")
	return(data[1], data[2], data[3],)

def get_insert_data(command):
	data = command.split(' ')
	if len(data) != 4:
		raise Exception("Incorrect number of arguments entered")
	return(data[1], data[2], data[3],)

def get_abonnement_data(command):
	data = command.split(' ')
	if len(data) != 3:
		raise Exception("Incorrect number of arguments entered")
	return(data[1], data[2],)

def get_fee_query_data(command):
	data = command.split(' ')
	if len(data) != 3:
		raise Exception("Incorrect number of arguments entered")
	return(data[1], data[2],)

def get_age_query_data(command):
	data = command.split(' ')
	if len(data) != 3:
		raise Exception("Incorrect number of arguments entered")
	return(data[1], data[2],)
	
