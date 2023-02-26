import os
import re
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pickle as pkl

class Models:
	def __init__(self) -> None:
		self.sets = os.listdir('./models')
		
	def get_names_of_countries(self):
		countrynames = []
		for filename in self.sets:
			countryname = filename.replace('Model.pkl', '')
			countryname = re.sub("[\(\[].*?[\)\]]", "", countryname)
			if 'pkl' in filename and countryname not in countrynames:
				countrynames.append(countryname)
		return countrynames
	def get_specific_model(self, country):
		model_name = f'./models/{country}Model.pkl'
		
		with open(model_name, "rb") as f:
			model = pkl.load(f)
			
		return model