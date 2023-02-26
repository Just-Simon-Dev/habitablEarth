from datetime import datetime

from pandas import Series
from models.models import Models

class Country:
	def __init__(self):
		self.models = Models()
	def calculate_step(self, end_date:datetime):
		start_date = datetime(2013, 9, 1)
		years = end_date.year - start_date.year
		steps = years*12 + end_date.month - start_date.month
		return steps
	def __get_countries_names(self):
		names = self.models.get_names_of_countries()
		return names
	def predict_temperature_for_country(self, steps, country):
		names = self.__get_countries_names()
		temperatures = {}

		for name in names:
			if(country == name):
				model = self.models.get_specific_model(name)
				temperature = model.get_forecast(steps=steps)
				forec = temperature.predicted_mean
				forec:Series
				
				temp = forec.array[-1]
				temperatures[name] = temp
				return temperatures