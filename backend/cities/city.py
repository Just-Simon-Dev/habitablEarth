import pandas as pd
from datetime import datetime

class City():
	def __init__(self, name):
		self.name = name
	
	def get_temperature(self, _from:datetime, _to:datetime):
		cities_temperatures = pd.read_csv('./cities/city_temperature.csv')
		temperatures = cities_temperatures[cities_temperatures['City'] == self.name]
		return temperatures