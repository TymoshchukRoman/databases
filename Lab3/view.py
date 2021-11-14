class View:

	def print_table_of_data(self, data) :
		for row in data:
			subrow = ""
			for element in row:
				subrow += "{:20}".format(str(element))
			print(subrow)