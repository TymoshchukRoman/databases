import pandas as pd
class View:
	def get_table_of_data(self, data: dict):
		print(str(pd.DataFrame(data)))